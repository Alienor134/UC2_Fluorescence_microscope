"""
  
  Copyright (C) 2022 Sony Computer Science Laboratories
  
  Author(s) Aliénor Lahlou
  
  free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see
  <http://www.gnu.org/licenses/>.
  
"""

import time
import json
import argparse
import pickle

import pandas as pd
import pymmcore
import os.path
import time
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import tempfile
import ipdb

import tifffile
from serial import *

from ingredient_csl_leds import arduino_LED, get_arduino_light
from ingredient_save_folder import save_folder, make_folder
from ControlCamera import ControlCamera


from sacred.observers import MongoObserver
from sacred import Experiment

sec = 1000
min = 60*1000

@arduino_LED.config
def update_cfg(blue_param, purple_param, trigger_param):

    blue_param["offset"] = 5*sec
    blue_param["period"] = 10*min
    blue_param["duration"] = 8*min
    blue_param["analog_value"] = 180#255#//5
    
    
    
    trigger_param["offset"] = 3*sec
    trigger_param["period"] = 1*sec


ex = Experiment('Dronpa2', ingredients=[arduino_LED, save_folder ])
ex.observers.append(MongoObserver())



@ex.config
def cfg(arduino_LED):
        framerate = 1000/arduino_LED['trigger_param']['period']
        exp_duration = 60*250//arduino_LED["blue_param"]["analog_value"]//4
        downscale = 3

@ex.named_config
def Daheng():

    cam_type = "MMConfig/Daheng.json"

    cam_param = {"Exposure(us)": 900000,
                 "Gain": 23,
                 "SensorHeight":2048,
                "SensorWidth":2448,
                "TriggerMode": "On",
                "TriggerSource":"Line0"}

@ex.named_config
def UEye():

    cam_type = "MMConfig/UEye.json" 
    cam_param = {"Frame Rate":1,
                "Exposure": 997,
                 "Gain": 100}

#@ex.capture()
#def open_camera():
#    cam = Camera(cam_type, cam_param, downscale)
#    return cam

@ex.automain
def run(_run, exp_duration, framerate, arduino_LED, cam_type, cam_param, downscale):
    #ipdb.set_trace()
    save_folder =  make_folder(_run)
    ### initialize devices
    ##ARDUINO
    arduino_light = get_arduino_light(arduino_LED['port_arduino'])

    cam = ControlCamera(cam_type, cam_param, downscale)
    #cam.camera_mode = "snap_video"
    #cam.N_im = framerate*exp_duration

    #blue LED
    arduino_light.add_digital_pulse(arduino_LED['blue_param'])

    #camera trigger
    arduino_light.add_digital_pulse(arduino_LED['trigger_param'])

    #purple LED
    #add_primary_digital_pulse(link, purple_param)
    print('It will last ', exp_duration, 'seconds.')

    #cam.start()
    
    arduino_light.start_measurement()

    cam.snap_video(framerate*exp_duration)
    #cam.join()

    result, timing = np.array(cam.video), np.array(cam.timing)
    fname = save_folder + "/video.tiff"
    tifffile.imwrite(fname, result[:,:,:],photometric="minisblack")
            
    fname_t = save_folder + '/video_timing.csv'
    pd.DataFrame(timing).to_csv(fname_t)

    frame = cam.image
    image = np.array(Image.fromarray(np.uint8(frame)))
    if False:
        plt.figure()
        plt.imshow(image)
        #plt.imshow(np.sum(image[:,:,:3], axis = 2))
        plt.axis('off')
        save_name = save_folder + "/image.png"
        plt.savefig(save_name, bbox_inches = 'tight')

        plt.close('all')
        _run.add_artifact(save_name, "image.png")

    #ftmp = tempfile.NamedTemporaryFile(delete=False)
    #fname = ftmp.name + ".pkl"
    #with open(fname,'wb') as f:
    #    pickle.dump(result, f)

    #_run.add_artifact(fname, "video.npy")

    _run.add_artifact(fname, "video.tiff")
    _run.add_artifact(fname, "video_timing.csv")

    for i, frame in enumerate(result):
        _run.log_scalar("Fluorescence", np.mean(frame), i)
        _run.log_scalar("Time", i/framerate, i)

    #make_maps(_run, save_folder, result, timing)

    arduino_light.stop_measurement()

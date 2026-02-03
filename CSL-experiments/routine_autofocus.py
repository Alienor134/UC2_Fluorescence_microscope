"""
  
  Copyright (C) 2023 Sony Computer Science Laboratories
  
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



import os
csl_path = os.environ['CSL_PATH']

import os.path
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import ipdb

import time as TIMING


from serial import *

from ingredient_csl_leds import arduino_LED, get_arduino_light
from ingredient_save_folder import save_folder, make_folder

from ControlCamera import ControlCamera

from ControlMotors import ControlStage


from sacred.observers import MongoObserver
from sacred import Experiment
sec = 1000
min = 60*1000

@arduino_LED.config
def update_cfg(blue_param, purple_param, trigger_param):
    blue_param["offset"] = 0
    blue_param["period"] = 2*min
    blue_param["duration"] = 1*min
    trigger_param["period"] = 1*sec
    blue_param["analog_value"] = 255



ex = Experiment('autofocus', ingredients=[arduino_LED, save_folder])

ex.observers.append(MongoObserver())


@ex.config
def cfg(arduino_LED):


    framerate = 1000/arduino_LED['trigger_param']['period']

    N=10
    step=200

    gears = [1, 100, 1]
    arduino_motors = "COM6"



@ex.named_config
def Daheng():
    cam_type = "MMConfig/Daheng.json"
    cam_param = {"Exposure(us)": 900*1000,
                 "Gain": 10,
                 "SensorHeight":2048,
                "SensorWidth":2448,
                "TriggerMode": "Off",
                "TriggerSource":"Software"}

@ex.named_config
def UEye():
    cam_type ="MMConfig/UEye.json" 
    cam_param = {"Frame Rate":1,
                "Exposure": 900,
                 "Gain": 100, 
                 "Trigger":"internal"}
    
@ex.automain
def run(_run, cam_type, cam_param, N, step, arduino_LED, arduino_motors, gears):
    
    
    def show_images(images, cols = 1, titles = None):
        """Display a list of images in a single figure with matplotlib.
        
        Parameters
        ---------
        images: List of np.arrays compatible with plt.imshow.
        
        cols (Default = 1): Number of columns in figure (number of rows is 
                            set to np.ceil(n_images/float(cols))).
        
        titles: List of titles corresponding to each image. Must have
                the same length as titles.
        """
        assert((titles is None)or (len(images) == len(titles)))
        n_images = len(images)
        if titles is None: titles = ['Image (%d)' % i for i in range(1,n_images + 1)]
        fig = plt.figure()
        for n, (image, title) in enumerate(zip(images, titles)):
            a = fig.add_subplot(cols, np.ceil(n_images/float(cols)), n + 1)
            if image.ndim == 2:
                plt.gray()
            plt.imshow(image)
            a.set_title(title)
        fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
        #plt.show()
    
    save_folder =  make_folder(_run)

    link_LED = get_arduino_light(arduino_LED['port_arduino'])
    stage = ControlStage(arduino_motors, gears)
    cam = ControlCamera(cam_type, cam_param)


    def focus(pos, N, step, link_LED, stage):
        min = -N/2*step
        max = N/2*step
        stage.handle_enable(1)



        link_LED.add_digital_pulse(arduino_LED['blue_param'])

        positions = []
        position = pos + min 
        link_LED.start_measurement()
        images = []
        TIMING.sleep(2)
        stage.move_dz(stage.backlash_neg)
        TIMING.sleep(1)


        stage.move_dz(min)
        TIMING.sleep(5)
        stage.move_dz(stage.backlash_pos)
        TIMING.sleep(1)


        while position < max:
            print(position)
            stage.move_dz(step)
            position += step
            positions.append(position)
            TIMING.sleep(1)
            cam.mmc.snapImage()
            frame = cam.mmc.getImage()
            image = np.array(Image.fromarray(np.uint8(frame)))
            plt.figure()
            plt.imshow(np.sum(image[:,:,:3], axis = 2))
            plt.axis('off')
            save_name = save_folder + "/autofocus_%d.png"%position
            plt.savefig(save_name, bbox_inches = 'tight')

            plt.close('all')
            _run.add_artifact(save_name, "autofocus_%d.png"%position)

            images.append(image)

        stage.move_dz(stage.backlash_neg)
        TIMING.sleep(1)

    
        
        while position > min:
            print(position)
            stage.move_dz(-step)
            position += -step
            positions.append(position)
            TIMING.sleep(1)
            cam.mmc.snapImage()
            frame = cam.mmc.getImage()
            image = np.array(Image.fromarray(np.uint8(frame)))
            images.append(image)
        
        link_LED.stop_measurement()
    
        
        #show_images(images, cols = 3)
        #ipdb.set_trace()
        blurs = []
        plt.figure()
        for i in range(len(images)):
            blur =  cv2.Laplacian(images[i], cv2.CV_64F).var()
            plt.scatter(positions[i], blur)
            blurs.append(blur)
        
        plt.xlabel("Voltage piezo")
        plt.ylabel("Laplacian variance")
        #plt.show()

        
        y = np.argmax(blurs)
        print(y)
        print(positions)
        print(blurs)

        #position at max:
        stage.move_dz(stage.backlash_pos)
        TIMING.sleep(1)

        stage.move_dz(positions[y]- positions[-1])
        TIMING.sleep(5)

        
        stage.handle_enable(0)

        return min//2,  max//2, positions[y], positions, blurs, images

    
    plt.figure()
    voltage_list = []
    blur_list = []
    image_list = []
    pos = 0
    for i in range(4):
        min, max, pos, v, b, im = focus(pos,N, step, link_LED, stage)
        voltage_list.extend(v)
        blur_list.extend(b)
        image_list.extend(im)
        step=step//2
        #ipdb.set_trace()
    #ipdb.set_trace()
        
        
    #with open("G:/DREAM/from_github/PAMFluo/specs/focus_wide.txt", 'w') as f:
    #    f.write('%f' %voltage_list[np.argmax(blur_list)])
    
    pos = voltage_list[-1]
    best_pos = voltage_list[np.argmax(blur_list)]
    
    #ipdb.set_trace()
    for i in range(len(voltage_list)):
            _run.log_scalar("blur", blur_list[i], voltage_list[i])

    plt.xlabel("Voltage (V)")
    plt.ylabel("Laplacian variance")
    fig = plt.plot(np.array(voltage_list), np.array(blur_list), 'ok')
    plt.savefig("autofocus.png")
    _run.add_artifact("autofocus.png")


    #ni.g.save_name = "image_focus"    
    #fig = ni.g.multi(image_list[np.argmax(blur_list)])
    #ni.g.saving(fig)
    #_run.add_artifact(ni.g.save_path + ni.g.extension)

    
    
    
    
    #ref: https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
    #ref: https://github.com/antonio490/Autofocus
    #ref: https://sites.google.com/site/cuongvt101/research/Sharpness-measure
    

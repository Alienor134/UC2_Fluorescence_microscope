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


import threading
import tempfile
import ipdb
import imageio



from serial import *

from ingredient_csl_leds import arduino_LED, get_arduino_light
from ControlCamera import ControlCamera

from ControlMotors import ControlStage, interface_motors


from sacred.observers import MongoObserver
from sacred import Experiment
sec = 1000
min = 60*1000

@arduino_LED.config
def update_cfg(blue_param, purple_param, trigger_param):
    blue_param["offset"] = 0
    blue_param["period"] = 10*min
    blue_param["duration"] = 9*min
    trigger_param["period"] = sec/10
    blue_param["analog_value"] = 255


ex = Experiment('routine_focus', ingredients=[arduino_LED])

ex.observers.append(MongoObserver())


@ex.config
def cfg(arduino_LED):
    x = 0
    y = 0
    z = 0
    gears = [1, 1, 1]

    arduino_motors = "COM6"


@ex.named_config
def Daheng():
    
    cam_type = "MMConfig/Daheng.json" #"MMconfig/UEye.json"    cam_param =  {"TriggerMode": "Off",
    cam_param = { 
        "SensorHeight":2048,
        "SensorWidth":2448,
        "Exposure(us)":1000*1000/5,
        "TriggerMode":"On",
        "TriggerSource": "Line0",
        "Gain":23,
        }

@ex.named_config
def UEye():

    cam_type = "MMConfig/UEye.json" 
    cam_param = {"Trigger":"internal",
        "Exposure": 97,
                 "Gain": 100}
    

@ex.automain
def run(_run, cam_type, cam_param, arduino_LED, arduino_motors, gears):


    
    link_LED = get_arduino_light(arduino_LED['port_arduino'])
    #stage = ControlStage(arduino_motors, gears)

    #blue LED
    link_LED.add_digital_pulse(arduino_LED['blue_param'])

    #camera trigger
    link_LED.add_digital_pulse(arduino_LED['trigger_param'])

    ipdb.set_trace()

    cam = ControlCamera(cam_type, cam_param)

    link_LED.start_measurement()

    cam.camera_mode = "continuous_stream"

    

    motor_thread = threading.Thread(target = interface_motors)#, args=(stage,))
 
    cam.start()
    motor_thread.start()


    cam.join()
    motor_thread.join()
    #ipdb.set_trace()
    
    link_LED.stop_measurement()

    ftmp = tempfile.NamedTemporaryFile(delete=False)
    fname = ftmp.name + ".png"
    imageio.imwrite(fname, cam.image)

    _run.add_artifact(fname, "focus_image.png")
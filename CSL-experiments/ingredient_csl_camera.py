"""
  
  Copyright (C) 2022 Sony Computer Science Laboratories
  
  Author(s) Peter Hanappe, Aliénor Lahlou
  
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

from serial import *


import numpy as np
from sacred import Ingredient

camera = Ingredient('camera')

@camera.named_config
def Daheng():

    cam_type = "C:/Users/alien/Documents/Github/CSL-forge/CSL-camera/MMConfig/Daheng.json"

    cam_param = {"Exposure": 150*1000,
                 "Gain": 23,
                 "SensorHeight":2048,
                "SensorWidth":2448,
                "TriggerMode": "On",
                "TriggerSource":"Line2"}

 
@camera.named_config
def UEye():
    cam_type = "C:/Users/alien/Documents/Github/CSL-forge/CSL-camera/MMConfig/UEye.json" 
    cam_param = {"Frame Rate":1,
                "Exposure": 170,
                 "Gain": 100}



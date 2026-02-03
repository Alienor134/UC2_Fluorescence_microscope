Experimental framework based on Sacred
======
The principle of Sacred is to store the experiment data and metadata in a file  that can be stored in a database. Here we used the noSQL framework with MongoDB. There are numerous aspects to Sacred detailed in the `original publication <https://conference.scipy.org/proceedings/scipy2017/klaus_greff.html>`_ including: 

#. Save code and imported code used to launch the experiment
#. View experiment parameter set
#. Save log
#. Draw graphs in the database and access the raw data (metrics)
#. Save numerous file types (artifacts)
#. Compare experiments: results/code difference/metadata difference


Install Sacred: 
=================

All the information about Sacred are here: `visit Sacred <https://github.com/IDSIA/sacred>`_

Install the database 
=================

Download `MongoDB <https://www.mongodb.com/try/download/community>`_
Create a new database called "sacred" (no caps).

Web interface
=================

All the information about Omniboard are here: `visit Omniboard <https://github.com/vivekratnavel/omniboard>`_)

in the command line type: 

``npm install -g omniboard``


To launch omniboard: 
```omniboard -m 127.0.0.1:27017:sacred```

To open the interface connect to : http://localhost:9000/sacred

![](Images/2023-02-06-10-57-11.png)


Install the database quiery tool: 
=================

All the information about Incense are here: `visit Incense <https://github.com/JarnoRFB/incense>`_)



Example of adaptation of [CSL-lights](XXX)
-------
+-----------------------------------------------+--------------------------------------------------------+
| **Script to control a light source**          | **The same script as Sacred experiment**               |
+===============================================+========================================================+
| .. code:: python                              | .. code:: python                                       |
|                                               |                                                        |
|   from serial import Serial                   |   from serial import Serial                            |
|   import CSLlight                             |   import CSLlight                                      |
|   arduino_port = "COM5"                       |   from sacred.observers import MongoObserver           |
|   sec = 1000 #conversion ms to s              |   from sacred import Experiment                        |
|   LED_param = {'pin':11,                      |   ex = Experiment('blink_LED')                         |
|   'offset':0.5*sec,                           |   ex.observers.append(MongoObserver(db_name = "demo")) |
|   'period': 5*sec,                            |                                                        |
|   'duration': 2*sec,                          |   @ex.config:                                          |
|   'analog_value': 255,                        |   def cfg():                                           |
|   }                                           |     arduino_port = "COM5"                              |
|                                               |     sec = 1000 #conversion ms to s                     |
|   link = Serial(arduino_port)                 |     LED_param = {'pin':11,                             |
|   CSLLight.add_digital_pulse(link, LED_param) |                  'offset':0.5*sec,                     |
|   CSLlight.start_measurement(link)            |                  'period': 5*sec,                      |
|   time.sleep(300)                             |                  'duration': 2*sec,                    |
|   CSLlight.stop_measurement(link)             |                  'analog_value': 255,                  |
|                                               |                  }                                     |
|                                               |   @ex.capture                                          |
|                                               |   def blink():                                         |
|                                               |     link = Serial(arduino_port)                        |
|                                               |     CSLLight.add_digital_pulse(link, LED_param)        |
|                                               |     CSLlight.start_measurement(link)                   |
|                                               |     time.sleep(300)                                    |
|                                               |     CSLlight.stop_measurement(link)                    |
|                                               |                                                        |
|                                               |   @ex.automain                                         |
|                                               |   def run():                                           |
|                                               |     blink()                                            |
|                                               |                                                        |
+-----------------------------------------------+--------------------------------------------------------+

Example of adaptation of [CSL-motors](XXX)
-------

+--------------------------------------------+--------------------------------------------------------+
| **Script to control a motor**              | **The same script as Sacred experiment**               |
+============================================+========================================================+
| .. code:: python                           | .. code:: python                                       |
|                                            |                                                        |
|   from CSLstage.CSLstage import CSLstage   |   from serial import Serial                            |
|                                            |   import CSLlight                                      |
|   arduino_port = "COM6"                    |   from sacred.observers import MongoObserver           |
|   gears = [1,1,1]                          |   from sacred import Experiment                        |
|   stage = CSLstage(arduino_port, gears)    |   ex = Experiment('blink_LED')                         |
|   #gearbox ratio of X, Y and Z axis        |   ex.observers.append(MongoObserver(db_name = "demo")) |
|   stage.handle_enable(1)                   |                                                        |
|   stage.move_dx(10)                        |   @ex.config:                                          |
|   stage.handle_enable(0)                   |   def cfg():                                           |
|   stage.reset()                            |     arduino_port = "COM5"                              |
|                                            |     gears = [1,1,1]                                    |
|                                            |                                                        |
|                                            |   @ex.capture                                          |
|                                            |   def get_stage():                                     |
|                                            |     stage = CSLstage(arduino_port, gears)              |
|                                            |                                                        |
|                                            |   @ex.automain                                         |
|                                            |   def run():                                           |
|                                            |     stage = get_stage()                                |
|                                            |                                                        |
|                                            |     stage.handle_enable(1)                             |
|                                            |     stage.move_dx(10)                                  |
|                                            |     stage.handle_enable(0)                             |
|                                            |     stage.reset()                                      |
|                                            |                                                        |
+--------------------------------------------+--------------------------------------------------------+

Example of adaptation of [CSL-camera](XXX)
-------

+---------------------------------------------------------------------+--------------------------------------------------------------+
| **Script to control a camera**                                      | **The same script as Sacred experiment**                     |
+=====================================================================+==============================================================+
| .. code:: python                                                    | .. code:: python                                             |
|                                                                     |                                                              |
|    from ControlCamera import ControlCamera                          |    from ControlCamera import ControlCamera                   |
|    cam_type = "MMConfig/Daheng.json"                                |                                                              |
|    update_param = {"Exposure": 150*1000,                            |    @ex.config                                                |
|                  "Gain": 23}                                        |    def config():                                             |
|    downscale = 5 #downscale the image to save                       |       cam_type = "MMConfig/Daheng.json"                      |
|    cam = ControlCamera(cam_type, update_param, downscale)           |       update_param = {"Exposure": 150*1000,                  |
|    N_im =  20                                                       |                  "Gain": 23}                                 |
|    cam.snap_video(N_im)                                             |                                                              |
|    video, timing = save_video("save_folder")                        |       downscale = 5 #downscale the image to save             |
|    cam.reset()                                                      |       N_im =  20                                             |
|                                                                     |    @ex.capture                                               |
|                                                                     |    def get_camera():                                         |
|                                                                     |       cam = ControlCamera(cam_type, update_param, downscale) |
|                                                                     |                                                              |
|                                                                     |    @ex.automain                                              |
|                                                                     |    def run(N_im):                                            |
|                                                                     |       cam.snap_video(N_im)                                   |
|                                                                     |       video, timing = save_video(save_folder, _run)          |
+---------------------------------------------------------------------+--------------------------------------------------------------+

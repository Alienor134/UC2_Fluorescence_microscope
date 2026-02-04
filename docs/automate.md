# Software


![thumbnails](/UC2_Fluorescence_microscope/assets/images/software.png)

## Summary of the available software

[ControlSerial](https://github.com/Alienor134/UC2_Fluorescence_microscope) - Python serial interface  
[ControlMotors](https://github.com/Alienor134/UC2_Fluorescence_microscope) - Motor control  
[ControlCamera](https://github.com/Alienor134/UC2_Fluorescence_microscope) - Camera acquisition interface  
[ControlLight](https://github.com/Alienor134/UC2_Fluorescence_microscope) - LED and laser control  


## Install instructions

Begin by installing the packages in a virtual environment. For more information on why virtual environments matter, refer to [this page](https://github.com/Alienor134/Teaching/blob/master/Python/Tutorials/Install_Anaconda_Jupyter.md).

```bash
git clone https://github.com/Alienor134/UC2_Fluorescence_microscope.git
cd UC2_Fluorescence_microscope
git submodule update --init --recursive
conda create -n control python=3.10
conda activate control
cd ControlSerial
pip install -e .
cd ..
cd ControlMotors
pip install -e .
cd ..
cd ControlCamera
pip install -e .
cd ..
cd ControlLight
pip install -e .
```

Install the libraries required for Arduino following the README instructions in [ControlSerial](https://github.com/SonyCSLParis/ControlSerial) and [ControlMotors](https://github.com/SonyCSLParis/ControlMotors).

## [optional]
If you want to install a data management strategy, implement the data management directly at the instrument level using [Sacred](https://sacred.readthedocs.io/en/stable/). Then use the [Altar](https://dreamrepo.github.io/Altar/) suite to interact with the data. 

## Example of use
For an example of project using this software you can refer to [this page](https://alienor134.github.io/UC2_Fluorescence_microscope/docs/example).
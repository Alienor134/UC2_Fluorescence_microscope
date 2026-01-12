## Implement the control libraries

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
If you want to install a data management strategy, implement the data management directly at the instrument level using [Sacred](https://sacred.readthedocs.io/en/stable/). Then use the [Altar](https://alienor134.github.io/Altar/) suite to interact with the data. 


## Example of project

You can find an example of a project using the fluorescence microscope [here](https://github.com/Alienor134/CSL-forge/tree/main). It corresponds to the code used for the project [manuscript - TODO]().

- The folder [CSL-experiments](https://github.com/Alienor134/CSL-forge/tree/main/CSL-experiments) explains how to connect the fluorescence microscope to the database framework [Sacred](https://github.com/IDSIA/sacred) and store the data in MongoDB. It contains several examples of codes used to generate the raw data for the [manuscript - TODO]().

- The folder [CSL-analysis](https://github.com/Alienor134/CSL-forge/tree/main/CSL-analysis) access the database using the Python package [Incense](https://github.com/JarnoRFB/incense) and show how to analyse the data. It corresponds to the data presented in [manuscript - TODO]().


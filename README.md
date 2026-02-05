# Fluorescence microscope adapted with UC2 library

[![License: CERN-OHL-S-2.0](https://img.shields.io/badge/Hardware%20License-CERN--OHL--S--2.0-blue.svg)](LICENSE)
[![License: GPL-3.0](https://img.shields.io/badge/Software%20License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![DOI](https://zenodo.org/badge/974776636.svg)](https://doi.org/10.5281/zenodo.18483954)


An open-source, modular LED-based fluorescence microscope with infinity optics. This system is capable of acquiring time-lapse videos from living cells inside an incubator and supports X/Y/Z/t acquisitions and fluorescent imaging.

**Intended Audience**: Researchers, engineers, microscopists interested in reducing the cost of hardware development for optical systems and produce quick prototypes. 


![alt text](assets/images/optical_table_side.png)

## Documentation

Access the full [documentation website](https://alienor134.github.io/UC2_Fluorescence_microscope/docs)


## Repository Structure

- **Hardware**: CAD files in `INVENTOR/` (source) and `STL/` (3D printing). Specific hardware ca also be found in the submodules, in particular for different motorization options 
- **Software**: Control modules as Git submodules (`ControlCamera`, `ControlLight`, `ControlMotors`, `ControlSerial`)
- **Documentation**: Build guides, automation, and bills of materials in `docs/`

## Quick Start

```bash
# Clone the repository with submodules
git clone https://github.com/Alienor134/UC2_Fluorescence_microscope.git
cd UC2_Fluorescence_microscope
git submodule update --init --recursive
```

The instrument can run without specific software except the camera. The LED control and motor control are optional and can be replaced by manual actions. Still, for detailed setup instructions of the software, see [docs/automate.md](docs/automate.md)

---

## Interested in contributing to the project ? Read the following.


This project follows the [Open Source Hardware Association (OSHWA) definition](https://www.oshwa.org/definition/) of open-source hardware. All design files, documentation, and bills of materials are freely available. Modifications and derivatives are encouraged under the terms of the CERN-OHL-S-2.0 license.

If any file missing, raise an issue in Gtihub repository and we will address it.


### Licenses

#### Hardware License
The hardware designs (CAD files, STL files, and mechanical assemblies) are licensed under the **CERN Open Hardware Licence Version 1 (CERN-OHL-S-1.2)**. See [LICENSE](License.md) for full text. The license is inherited from the OpenUC2 project.

#### Software License
The control software modules are licensed under the **GNU General Public License v3.0 (GPL-3.0)** or later. See individual LICENSE files in each submodule directory.

#### Documentation License
Documentation is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.


### Version Control Practice

- **Repository**: Git-based version control with full commit history
- **Submodule Structure**: This module is part of the UC2 Fluorescence Microscope parent repository
- **Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Releases**: Archived on Zenodo

### Attribution Requirements

When using or modifying this software:

1. **Credit the original authors**: Aliénor Lahlou, Sony Computer Science Laboratories
2. **Maintain license notices**: Keep license-related headers in source files
3. **Document modifications**: Clearly state any changes made
4. **Share derivatives**: Derivatives must be released compatible license

### Contributing

Contributions are tracked through:
- Git commit history (automatic attribution)
- Pull requests on GitHub
- Contributor acknowledgments in release notes

The documentation is automatically generated via Github Pages and should be updated along modifications (folder [docs](https://github.com/Alienor134/UC2_Fluorescence_microscope/tree/main/docs)). Follow these [instructions](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) to verify the changes locally before commit. 

--- 

## Current version

- **Current Version**: 1.0.0
- **Last Updated**: January 2026
- **Git Repository**: https://github.com/Alienor134/UC2_Fluorescence_microscope
- **Zenodo DOI**: https://doi.org/10.5281/zenodo.18483954



## Citation

If you use this microscope design in your research, please cite it properly. We have registered this project on Zenodo for permanent archival with a persistent DOI (https://doi.org/10.5281/zenodo.18483954).


## Acknowledgments

This project builds upon several open-source initiatives:

### Hardware Acknowledgments
- **[OpenUC2](https://github.com/openUC2/UC2-GIT)**: Base modular cube system and optical components.

### Software Acknowledgments
- **[pymmcore-plus](https://pymmcore-plus.github.io/pymmcore-plus/)** to facilitate working with Micro-manager backend in pure Python/C environments.
- **[ROMI project](https://github.com/romi)** (Sony CSL) providing open-source tools to control hardware with Arduino and Python.
- **[Sacred](https://github.com/IDSIA/sacred)** to organise automated experimental runs. 




## Attributions


This project is based on the [UC2 fluorescence microscope](https://github.com/openUC2/UC2_Fluorescence_microscope?tab=readme-ov-file) by OpenUC2, licensed under CERN-OHL-S v2.   
**Modifications**: light source (from laser to LED), motorized focus, software.
**Additions**: dual illumination, optical fiber injection, data management.


*This project is open-source and released under CERN-OHL-S-2.0 (hardware) and GPL-3.0 (software) licenses.*

---



## Cross-References and Navigation

### UC2 Fluorescence Microscope Project

- **Main Repository**: [UC2_Fluorescence_microscope](https://github.com/Alienor134/UC2_Fluorescence_microscope)
- **Documentation Home**: https://alienor134.github.io/UC2_Fluorescence_microscope/docs/
- **Build Instructions**: https://alienor134.github.io/UC2_Fluorescence_microscope/docs/build
- **Bill of Materials**: https://alienor134.github.io/UC2_Fluorescence_microscope/docs/bill_of_materials
- **Automation Guide**: https://alienor134.github.io/UC2_Fluorescence_microscope/docs/automate
- **Examples**: https://alienor134.github.io/UC2_Fluorescence_microscope/docs/example

### Related Control Modules

| Module | Purpose | Documentation |
|--------|---------|---------------|
| [ControlCamera](https://github.com/SonyCSLParis/ControlCamera) | Camera acquisition and control | [README](https://github.com/SonyCSLParis/ControlCamera/README.md) |
| [ControlLight](https://github.com/SonyCSLParis/ControlLight) | Laser and LED control | [README](https://github.com/SonyCSLParis/ControlLight/README.md) |
| [ControlMotors](https://github.com/SonyCSLParis/ControlMotors) | XYZ stage and motor control | [README](https://github.com/SonyCSLParis/ControlMotors/README.md) |
| [ControlSerial](https://github.com/SonyCSLParis/ControSerial)| Arduino-Python communication | [README](https://github.com/SonyCSLParis/ControSerial/README.md) |
| [Altar](https://github.com/DreamRepo/Altar) | Data management and visualization | [Documentation](https://dreamrepo.github.io/Altar/) |


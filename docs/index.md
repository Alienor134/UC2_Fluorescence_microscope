---
layout: default
title: Introduction
nav_order: 1
---



# Introduction

 Reference: *Minimal reproduction and calibration of a fluorescence microscope for single-cell imaging*

![alt text](/UC2_Fluorescence_microscope/assets/images/optical_table_side.png)
*Picture of the final set-up*

## Navigation
- [Introduction](index.md)
- [Bill of Materials](bill_of_materials.md)
- [Build Instructions](build.md)
- [Software](automate.md)

---


# Purpose

Microscopy is a critical experimental tool in life sciences. However, when attempting to reproduce or scale-up a published method, researchers often meet difficulties in implementing specific protocols, often because they do not have full control over the hardware and software. 

To address these challenges, we present a modular open-source hardware and software pipeline that integrates automation and database management. 

We provide comprehensive guidance on building and calibrating the microscope hardware, implementing automation, and data analysis and storage methods. The highly modular Python software we introduce facilitate customization and reusability beyond microscopy, empowering researchers and engineers to adapt components for other scientific applications.

The microscope presented here is a simplified and open-source version of the microscope used in [this publication](https://doi.org/10.1101/2025.01.23.633867). The 3D structure was derived from the [Open-UC2](https://openuc2.com/) library.



In this repository we provide: 
- A [bill of materials](bill_of_materials.md) to reproduce the microscope 
- [Build instructions](build)
- Python packages to use the library: they each have their specific documentation
- [Software](automate.md) summary with support codes

# License

**Hardware License**

The hardware designs (CAD files, STL files, and mechanical assemblies) are licensed under the CERN Open Hardware Licence Version 2 - Strongly Reciprocal (CERN-OHL-S-2.0). See LICENSE for full text.


**Software License**

The control software modules are licensed under the GNU General Public License v3.0 (GPL-3.0) or later. See individual LICENSE files in each submodule directory.

**Documentation License**

Documentation is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

# Attributions

This project is based on the [UC2 fluorescence microscope](https://github.com/openUC2/UC2_Fluorescence_microscope?tab=readme-ov-file) by OpenUC2, licensed under CERN-OHL-S v2.   
**Modifications**: light source (from laser to LED), motorized focus, software.
**Additions**: dual illumination, optical fiber injection, data management.
The original authors do not endorse this version.

# Contributing

The guidelines to contribute to the project (including versionning and attribution statements) are listed in the [README](https://github.com/Alienor134/UC2_Fluorescence_microscope/blob/main/README.md) page of this project. 
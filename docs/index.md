
# Purpose

Microscopy is a critical experimental tool in life sciences. However, when attempting to reproduce or scale-up a published method, researchers often meet difficulties in implementing specific protocols, often because they do not have full control over the hardware and software. 

To address these challenges, we present a modular open-source hardware and software pipeline that integrates automation and database management. 

We provide comprehensive guidance on building and calibrating the microscope hardware, implementing automation, and data analysis and storage methods. The highly modular Python software we introduce facilitate customization and reusability beyond microscopy, empowering researchers and engineers to adapt components for other scientific applications.

The microscope presented here is a simplified and open-source version of the microscope used in [this publication](https://doi.org/10.1101/2025.01.23.633867). The 3D structure was derived from the [Open-UC2](https://openuc2.com/) library.



In this repository we provide: 
- A [bill of materials](bill_of_materials.md) to reproduce the microscope 
- [Build instructions](build)
- Python packages to use the library: they each have their specific documentation
- [Usage example](automate.md) with support codes

# License

Copyright (C) 2025 Sony Computer Science Laboratories 

Author(s) Aliénor Lahlou

You can redistribute it and/or modify  it under the terms of the GNU General Public License as published by   the Free Software Foundation, either version 3 of the License, or   (at your option) any later version.  This project is distributed in the hope that it will be useful, but  WITHOUT ANY WARRANTY; without even the implied warranty of   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU  General Public License for more details.  You should have received a copy of the GNU General Public License  along with this program.  If not, see  <http://www.gnu.org/licenses/>.

This work was supported by the European Innovation Council Pathfinder Open DREAM (grant no. 101046451)
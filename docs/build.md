---
layout: default
title: Build instructions
nav_order: 3
---


# Light sources
### Soldering

 Solder LEDs to star PCB. This first step is the hardest of the tutorial. First tin-coat the electrodes of the LED. Make sure the electrodes are not gated by the tin. Let the PCB star warm to 200&deg;C on a heating plate. Then connect the LED to the PCB star, apply pressure. Take the mounted LED from the plate and let it cool down. Solder the electric wires to PCB.

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/solder_LED.jpeg" width="200"></a>
</p>


### Control
If you do not yet have access to LED drivers(exmaple: [1](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=2616), [2](https://www.thorlabs.us/thorProduct.cfm?partNumber=DC4104).), the first option is to build a minimal LED controller circuit. You will need the RECOM DC/DC converter, a potentiometer and electric wires. Use a regulated power supply to power the RECOM and another for the potentiometer. The second option is to build an LED driver. You can follow the instructions here: XXXXX (fork repo Julie).

>You can follow the instructions in [this repository](https://github.com/SonyCSLParis/CSL-Lights) to control the LEDs.
{: .important}





<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/RECOM_2.png" width="300"></a>
</p>


### Assembly and test

Mount the blue and purple LEDs on the UC2 star holder according to [UC2 documentation](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_LED). Add the lens mounted on the holder in front of the LED, and the filter mounted on the filter holder. 

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_lens_filter.jpeg" width="300"></a>
</p>

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_cube_mounted.jpeg" width="300"></a>
</p>

Make sure that you can observe the image of the chip on a white surface

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_chip_screen.jpeg" width="700"></a>
</p>

Notes: the 3 mounts don't hold still once the base cube it closed. We had to use double-sided tape to fix the LED mount. One other option is to increase the size of the mount slightly to tight it with the screws when closing the cube. The clamp to hold the filter works fine but is not sufficient to hold the lens which has a different geometry. XXXXXXXXXXWe will slightly increase the diameter of the hole to be able to maintain the lens with a Thorlabs 1 inch clamp that we will screw. 


### LED combination

Mount the dichroic filter on the dichroic filter holder accroding to [UC2 documentation](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Dichroic_Beamsplitter)

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/dichroic_filter.jpeg" width="700"></a>
</p>


Combine the two LEDs with the dichroic filter according to this scheme: 

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_scheme.png" width="300"></a>
</p>
 
 With [LED 1](https://www.mouser.fr/ProductDetail/997-LHUV0405A065), [LED 2](https://www.mouser.fr/ProductDetail/997-LXZ1PB01), [F1](https://www.comaroptics.com/components/filters/glass-colour-filters), [F2](https://www.comaroptics.com/components/filters/glass-colour-filters), [D1](https://www.comaroptics.com/components/filters/dichroic-filters/long-pass-dichroic-filters), [lens](https://www.thorlabs.de/thorproduct.cfm?partnumber=ACL25416U).


### Optical fiber injection

 The 2 LEDs are combined, however the size of the light beam is on the centimeter scale, but the optical fiber's aperture is 400µm. We use a microscope objective to reach the spot size required to inject in the fiber. (for now: 40x/0.65)

 Prepare the 3D parts for the fiber injection: XY fine displacement [objective holder](https://github.com/openUC2/UC2_OpenFiberCoupler/blob/main/STL/Application_OpenFiberCoupling_20_Cube_Inser_Flexuremanipulator_v3.stl) and lens holder to hold the [SMA fiber adapter](https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1SMA#ad-image-0). You can find more info on [UC2 documentation for fiber coupler](https://github.com/openUC2/UC2_OpenFiberCoupler). Mount the objective in one cube and the fiber holder in another and assemble them.

 <p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_injection_side.jpeg" width="700"></a>
</p>

 <p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/LED_injection.jpeg" width="700"></a>
</p>

Note: The XY objective holder is great ! The only issue is that the rest position is centered and the screws only allow positive X or Y displacement. We attached an elastic so that the rest position is tight to the corner (minimal X and Y position). That way it is possible to explore the whole X-Y displacement space allowed by the 3D piece with only 2 screws.

 <p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/objective_holder_fine.png" width="200"></a>
</p>


Adjust the focal distances so that the spot from the LEDs matches the entrance of the microscope objective and the output of the objective matches the aperture of the fiber. (TODO: give more details here)


Check the output of the fiber and the homogeneity of the spot. The blue light is brighter so you can play with the potentiometers to see the 2 colors separately. 

 <p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/spot.jpeg" width="300"></a>
</p>

# Imaging


1. Start to build the second part of the microscope : connect the other end of the fiber on an other UC2 cube.


2. Mount a dichroïc filter on a dichroïc holder cube ([UC2 documentation](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Dichroic_Beamsplitter)) and place it after the fiber according to the schema :

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/dichroic_filter_position.png" width="500"></a>
</p>

3. Construct the upper part of the scheme with the objective and the sample holder : we use XY fine displacement [objective holder](https://github.com/openUC2/UC2_OpenFiberCoupler/blob/main/STL/Application_OpenFiberCoupling_20_Cube_Inser_Flexuremanipulator_v3.stl) in one cube followed by [Generic sample holder](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Sample_Holder) in another cube. 

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/objective_sample_part.jpg" width="300"></a>
</p>

4. Combine the dichroïc filter and the objective-sample part. The dichroïc filter transmits light below the cut-off wavelength and reflects ligth above the cut-off. The fluorescence emission has a higher emission wavelength than the excitation. The incomming light from the fiber will be reflected by the dichroïc filtrer and go through the objective. Then the light emitted by the sample will be collected by the objective and pass the dichroïc filter without reflexion.

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/combined_dichroic_sample.jpg" width="300"></a>
</p>

5. Print your camera 3D holder model from the [git](https://github.com/openUC2/UC2-GIT/tree/master/CAD) (Search with Ctrl+F), and mount your camera in it. We use a Daheng MER2-503-36U3C camera with [Camera Cube (Allied Vision Alvium)](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Daheng_Imaging).
On the Daheng camera, the fixation consist on three screws :
<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/Box_Daheng.jpg" width="300"></a>
</p>

Note : We also use an IDS camera, and since there is not a camera holder for it, we use the [Camera Insert Allied Vision Alvium adjustable](https://github.com/openUC2/UC2-GIT/blob/master/CAD/RAW/STL/20_Cube_insert_AlliedVision_Alvium_adjustable_v3.stl).

6. Mount an adapted lens on the camera (we used a focal of f = 150 mm). Position the lens to conjugat it with the camra sensr: to do so, observe a net image of an object positionned 10 meters away from the camera. Then, align the lens and camera with the microscope objective and move the sample along the Z-axis to adjust the focus. To observe the sample, you may need to adjust your's camera parameters, like the exposure time and the gain. 

>You can follow the instructions in [this repository](https://github.com/SonyCSLParis/Motorized-stage) to automate the movement of the sample.
{: .important}

<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/observing_part.jpg" width="300"></a>
</p>
Note : Since the lens is heavy, we put a UC2 cube at the end of it with a lens holder to keep it straight.

The 2nd part of the microscope should look like that :
<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/imaging_part.jpg" width="700" angle="90"></a>
</p>

The final result should be looking like this :
<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/microscope.jpeg" width="700"></a>
</p>

With this microscope, with managed to observe some samples using the software provided by the camera manufacturer :
<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/sample_1.png" width="500"></a>
</p>
<p align="center">
<a> <img src="/UC2_Fluorescence_microscope/assets/images/sample_2.png" width="500"></a>
</p>


>You can follow the instructions in [this repository](https://github.com/SonyCSLParis/CSL-camera) to control the camera using Python.
{: .important}
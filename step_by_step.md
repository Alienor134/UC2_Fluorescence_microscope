# Objective 1: Inject 2 LEDs combined with a dichroic filter into an optical fiber 

## Bill of materials

### Hardware :gear:


| Component|      Quantity      |  Price per unit | Example|  
|----------|:-------------:|------:|------:|  
| High power LED blue 470nm |  1 | 2€ | [Mouser](https://www.mouser.fr/ProductDetail/997-LXZ1PB01)|  
| High power LED purple 405nm|    1   |   6€ | [Mouser](https://www.mouser.fr/ProductDetail/997-LHUV0405A065)|  
| PCB star Luxeon Z|    2   |   1€ | [LED mounting bases](https://led-mounting-bases.com/fr/mcpcb-pour-led/340-star-mcpcb-for-1-led-lumileds-luxeon-z-es.html)|
| Band-pass filter 475 |1 | 27€ | [475 GB 25](https://www.comaroptics.com/components/filters/glass-colour-filters)|  
| Band pass filter 490| 1| 27€ |[390 GB 25](https://www.comaroptics.com/components/filters/glass-colour-filters)|  
| High pass filter 480| 1| 45€ |[480 IY 125](https://www.comaroptics.com/components/filters/dichroic-filters/long-pass-dichroic-filters)| 
| Asphreic condenser lens focal 16mm | 2 |    18€ | [Thorlabs](https://www.thorlabs.de/thorproduct.cfm?partnumber=ACL25416U) |  
| Optical Fiber 400µm 0.5 NA | 1 |    81€ | [Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=M45L02) |  
| Microscope objective | 1 | --€ | [--](--)|  
| LED Driver (to be replaced) | 2 |301€ | [Throlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=LEDD1B])|


### UC2 parts


Link             |  Image of the part
:-------------------------:|:-------------------------:
[Base Plate puzzle](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_Baseplate)  |  [<img src="https://github.com/openUC2/UC2-GIT/blob/master/CAD/ASSEMBLY_Baseplate/IMAGES/10_Base_puzzle_v3_01.png" width=200>](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_Baseplate)
[CUBE Base](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Base)  |  [<img src="https://github.com/openUC2/UC2-GIT/blob/master/CAD/ASSEMBLY_CUBE_Base/IMAGES/Assembly_Cube_empty_IM_v3.png" width=200>](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Base)
[LED Star](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_LED) | [<img src="https://github.com/openUC2/UC2-GIT/blob/master/CAD/ASSEMBLY_CUBE_LED/IMAGES/Assembly_Cube_LED_holder_v3.png" width=200>](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_LED)
[Lens (cylindrical)](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Lens_CYLINDRICAL) | [<img src="https://github.com/openUC2/UC2-GIT/blob/master/CAD/ASSEMBLY_CUBE_Lens_CYLINDRICAL/IMAGES/Assembly_Cube_Lens_Cylindrical__cheap_v3.png" width=200>](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Lens_CYLINDRICAL)
[Dichroic Beam splitter](https://github.com/openUC2/UC2-GIT/tree/master/CAD//ASSEMBLY_CUBE_Dichroic_Beamsplitter) | [<img src="https://github.com/openUC2/UC2-GIT/blob/master/CAD/ASSEMBLY_CUBE_Dichroic_Beamsplitter/IMAGES/Assembly_Cube_Dichroic_Beamsplitter_25x35_v3.png" width=200>](https://github.com/openUC2/UC2-GIT/tree/master/CAD//ASSEMBLY_CUBE_Dichroic_Beamsplitter)
[maybe: fiber coupler](https://github.com/openUC2/UC2_OpenFiberCoupler#logo) | [<img src="https://github.com/openUC2/UC2_OpenFiberCoupler/blob/main/IMAGES/Application_OpenFiberCoupling.png" width=200>](https://github.com/openUC2/UC2_OpenFiberCoupler#logo)




### Assembly

1. Solder LEDs to star PCB (take pictures with Thomas)

<p align="center">
<a> <img src="xxxx" width="300"></a>
</p>


2. Solder the wires to PCB. For now the other extremity is connected to Thorlab's LED driver with banana plugs but this might change. 

<p align="center">
<a> <img src="xxxx" width="300"></a>
</p>

3. Mount the LED on the UC2 star holder according to [UC2 documentation](https://github.com/openUC2/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_LED). Add the lens mounted on the holder in front of the LED, and the filter mounted on the filter holder. 

<p align="center">
<a> <img src="./IMAGES/LED_lens_filter.jpeg" width="300"></a>
</p>

<p align="center">
<a> <img src="./IMAGES/LED_cube_mounted.jpeg" width="300"></a>
</p>

4. Make sure that you can observe the image of the chip on a white surface

<p align="center">
<a> <img src="./IMAGES/LED_chip_screen.jpeg" width="700"></a>
</p>

Notes: the 3 mounts don't hold still once the base cube it closed. We had to use double-sided tape to fix the LED mount. -> we will increase the size of the mount slightly to tight it with the screws when closing the cube. 
the clamp to hold the filter works fine but is not sufficient to hold the lens which has a different geometry. We will slightly increase the diameter of the hole to be able to maintain the lens with a Thorlabs 1 inch clamp that we will screw. 

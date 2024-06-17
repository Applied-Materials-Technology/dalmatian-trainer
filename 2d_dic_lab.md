# 2D DIC Training Laboratory
## Basic Camera Setup and Analysis
The first part of this assignment is focused on the basics of setting up a simple 2D DIC experiment and analysing various characteristics of the DIC measurement system. You will use a speckle pattern target and a translation stage to evaluate the camera and measurement performance. You will present your results as a power point presentation. Where you see the term ‘QU’ you will need to report the answer in your power point. The start of the powerpoint should include a basic explanation of how DIC works targeted at your peers.

**Equipment Required**: capture computer, camera, fixed focal length lens, micro-meter translation stage, speckle pattern target, mounting rail.

**General Setup**:
1. Mount the camera to the rigid rail using the screw mount provided
2. Connect the power cable and ethernet cables to the camera, plug these into the power board and ethernet port on the computer respectively
    - Make sure the lights on the back of the camera ethernet port are flashing to indicate the camera is communicating with the computer
3. Remove the lens caps from the camera and screw in the C to F mount adapter
4. Align the red dot on the lens to the red dot on the F mount adapter and connect the lens by twisting until you hear and/or feel a click
5. Open the MatchID grabber, the camera ‘Manta G504b’ should be listed, select it and press the continue icon.
6. You should now have a display showing you what the camera is seeing, if the image is dark try opening the aperture and/or increasing the exposure time
7. Create a working directory and then use appropriately named sub folders to store each set of images you take: e.g. C:\MatchID_WorkingDirectory\YOUR NAME\Test1_NoiseAnalysis and then C:\MatchID_WorkingDirectory\YOUR NAME\Test2_RigidBodyMotion etc
8. You can use the ‘Single Image’ button to store an image to file in the folder you have specified.

**Experiments**:

1. Magnification
    - Find the minimum focus distance for the lens by iteratively moving the camera closer to the speckle target and refocusing the lens
    - Look up the Sigma 105mm lens and find the minimum focus distance in the data sheet
    - **QU:** What is the minimum focal distance you measure between the camera and the target and how does this compare to the lens specification?
    - **QU:** Calculate the magnification, how does this compare with the lens specification?:
        i. M = f / (So – f), where M is the magnification, f is the focal length of the lens (in this case 105mm) and So is the distance between the camera and object being images (measure it with a long ruler).
    - Take an image of the ruler in front of the target
    - Open MatchID 2D and open the image in the length calibration module and use the line tool to calculate the pixel to mm conversion factor
    - **QU:** What is the image scale factor in mm/pixel for the minimum focal distance?
    - Move the camera back to a more reasonable distance from the target (something between 50cm and 80cm should work well)
2. Lighting
    - Explore how the lighting can be adjusted using the aperture ring on the lens and the exposure time set in the software.
    - **QU:** How else can lighting be adjusted?
    - Adjust the lighting to achieve a histogram that fills most of the grey levels without any saturation
        i. Open the aperture all the way and adjust the exposure from this point
    - **QU:** Why is saturation a problem for DIC?
    - With the aperture fully open focus the camera on the speckle pattern target
        i. HINT: it can be easier to see if the target is in focus by zooming in on the image using the mouse wheel.
3. Speckle Analysis
    - Take an image of the target
    - **QU:** What is the minimum number of pixels per speckle?
    - **QU:** What is the speckle size in pixels for the image you have taken?
4. Grey Level Noise Analysis
    - Take at least two static images
    - Open the images in either ImageJ or Matlab and subtract them from each other
        i. HINT: in Matlab look up the ‘imread’ function. After that you can subract the image arrays from each other directly: imDiff = im1 – im2. Then calculate the standard deviation: imNoise = std(imDiff(:))/sqrt(2).
    - **QU:** How many bits encode the image you have taken? What is the dynamic range for your image in bits?
    - **QU:** What is the grey level noise for this camera as a % of the dynamic range?
5. Length Calibration
    - Take an image of a ruler placed in front of the speckle target.
    - Open this image in the length calibration module of MatchID and use the line tool to obtain the pixel to mm conversion.
    - **QU:** What is the physical speckle size in ‘mm’ for your target?
6. QOI Noise Analysis
    - Take a series of images of the stationary images of the speckle target
    - Open the images in MatchID 2D and perform the correlation
        - Open the reference image first
        - Use the drawing tools to select an appropriate ROI
        - Use the speckle analysis tool to double check you have the required minimum pixels per speckle
        - Open the ‘deformed’ images
        - Set the correlation parameters and run the correlation
        - The mean and standard deviation of the displacement field can be found in the bottom right hand corner.
    - **QU:** What is a noise floor and how is it calculated?
    - **QU:** Plot the displacement noise floor as a function of subset size.
    - **QU:** Calculate the strain noise floor using the standard settings (subset 21, step 10, VSG Q4 element over 15 data points).
7. Rigid Body Motion Test
    - Create a new working folder to save the images called ‘Rigid Body Motion Test’
    - Orientate the micro stage and speckle target so that the target translates horizontally with respect to the camer-
    - Adjust your lighting and focus as necessary and take a single image to double check your speckle size using MatchID 2D
    - Take a length calibration image using the ruler and get your pixel calibration factor in mm/px
    - Take another static image and then translate the target by 0.1, 0.25 and 0.5mm taking an image after each translation. Rename the image files so you know which one is which!
    - Perform the correlation for each set of images using the standard parameters
    - **QU:** How does the mean displacement compare to the value you input on the translation stage?
    - **QU:** What should the strain be for this test and how does this compare to what you calculate in MatchID?
8. Out of Plane Movement Test
    - Create a new working folder to save the images called ‘Out of Plane Movement Test’
    - Orientate the micro stage and target so the target can be moved towards and away from the camer-
    - Adjust your lighting and focus as necessary and take a single image to double check your speckle size using MatchID 2D
    - Take a length calibration image using the ruler and get your pixel calibration factor in mm/px
    - Take another static image (0 translation) and then translate the target by 0.1, 0.25 and 0.5mm taking an image after each translation. Rename the image files so you know which one is which!
    - Perform the correlation for each set of images using the standard parameters and calculate the strains.
    - The strain for this test should be approximately dz/S0 where dz is how far you moved the target and S0 is the working distance (measure it with a ruler).
    - **QU:** How does the mean strain over the field compare with the calculation above?

## Considerations for Your Experiment
There are a variety of questions you need to answer about your own experiment in order to use DIC most effectively to measure what you want (in the DIC guide this is called the Quantity Of Interest or QOI).

1. What is your region of interest (ROI) and required field of view (FOV)?
    - **QU:** What is the difference between ROI and FOV? Why is this important?
    - Example: I have a sample that is a 80x15x2mm rectangle. The top and bottom 30mm of the sample are used to grip the sample so my ROI is 20x15mm. I am loading my sample in tension using an electromechanical machine. My sample has an elastic modulus of 20GPa and a tensile failure stress of 100MPa Therefore the peak strain will be: strain = stress/modulus = 100/200000 = 5 milli-strain. This means my sample will elongate by appox: strain = change in length / original length => change in length = 0.005 x 20 = 0.1mm. So my FOV needs to be at least 20.1x15mm. Let’s pick 21 x 16 mm to be on the safe side.
    - **QU:** What is the size of the ROI and FOV for your experiment?
2. What camera are you using and what are its specifications?
    - Look up the data sheet for the Manta G504b camera (or the camera you will be using),
    - **QU:** How many pixels does the sensor have in each direction (horizontal and vertical) and what is the physical pixels size in micro-meters?
    - Example: Assume I have a 3 mega-pixel camera with 2000x1500 pixels and the sensor pixel size is 3 micron. I orientate my camera so I have 2000 pixels sampling the 21mm of my FOV. This means my image length calibration is 21/2000 = 0.0105 mm/pixel = 10.5 micron/pixel.
3. What lens do I need?
    - There are two lens available: 1) Nikon 50mm fixed focal length and 2) Sigma 105mm fixed focal length. Look up the spec sheets for both lens.
    - **QU:** What is the magnification limit and closest imaging distance for each lens?
    - Example: My magnification is M = pixel size (in micron) / image pixel size (in micron) = 3 / 10.5 = 0.286. The 50mm lens can’t achieve this magnification so let’s pick the Sigma 105mm lens. My approximate imaging distance is S0 = f/M+f, where f is the focal length and M is the magnification. Therefore, S0 = 105/0.286 +105 = 472 mm. Which is about half a meter so it is manageable.
    d. **QU:** What is the magnification and imaging distance for your experiment?
4. What speckle size do I need?
    - Example: I need at least 3 pixels per speckle and I have 0.0105 mm/pixel. So my speckle must be at least 3x0.0105 = 0.0315 mm or 31.5 micron or larger.
    - NOTE: the smallest speckle size that can be achieved with the printer is 60 micron. However, 20 micron can be achieved with an airbrush but the dot size is much less reliable.
    - **QU:** What speckle size do you need for you experiment? How will you make the speckle pattern?
5. Reporting Requirements:
    - Look up the DIC good practice guide and develop a reporting table showing all the DIC parameters you will use for your experiment
    - **QU:** Show and explain your reporting table in your presentation


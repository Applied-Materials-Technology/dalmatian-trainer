# Stereo-DIC Training Laboratory
## Basic Experiment Setup and Analysis
The first part of the Stereo-DIC assignment focuses on the basic setup of a Stereo-DIC experiment and the analysis of various characteristics of the Stereo-DIC measurement system. In this exercise you will use a calibration target and the calibration software to establish the relationship between the cameras and their orientation relative to the specimen.

**Equipment Required**:
1. Capture computer
       
   * MatchID Grabber and MatchID 2D/Stereo installed    
2. Camera

   * Alvium 1800 U-2460 (24Mpx) or Alvium 1800 U-507 (5Mpx) can be used for this exercise
3.  Fixed Focal Length Lenses

    * Nikon 50mm fixed focal length or Sigma 105mm fixed focal length will be used for this exercise

4.  Mounting Equipment (tripods)
5.  Calibration Target
    
    * Select target size relative to the size of your field of view (FOV)
6. Speckle Pattern Target
7. Light source


**General Setup**:

1. Mount the two cameras to the tripod provided. Ensure both cameras are focused on the same region of interest (ROI) of the specimen.  Adjust the stereo angle between the cameras.
2. Connect power cable and ethernet cables to the camera, and plug these into the power board and ethernet port accordingly.

    * To ensure cameras are connected and communicating with the computer, lights on the back of the camera ethernet port should be green.

3. Remove the lens caps from the cameras and screw in the C to F mount adapters  
4. Align the red dot on the lens to the red dot on the F mount adapter and connect the lens by twisting until a click is heard/felt.
5. Open MatchID Grabber, either 'Alvium 1800 U-2460' or 'Alvium 1800 U-507' should be listed. Select the correct one and press the continue icon.
6. A display of what both of the cameras are seeing should be available, if either of the images are dark try opening the aperture and/or increasing exposure time.
7. Create a working directory and then use appropriately named sub folders to store each set of images you take: e.g. C:\MatchID_WorkingDirectory\YOUR NAME\Test1_NoiseAnalysis and then C:\MatchID_WorkingDirectory\YOUR NAME\Test2_RigidBodyMotion etc
8. The 'Single Image' button sotres an image to file in the folder you have specified.


**Specimen Preparation**:
1. Surface Preparation - Ensure the surface of the specimen is clean and dry.
2. Speckle Pattern Application - Apply a high-contrast, random speckle pattern to the surface of the specimen.

**Cross Correlation Check**:

1. Take images and save them to the correct directory and subfolder.
2. Open MatchID 2D software and select your reference image by clicking the 'Reference Image' button.

    * Your reference image will be the first frame taken by the master camera (camera 0).
3. Using the 'Deformed Image' button select your deformed images.   

     * Ensure the selected deformed images are also taken by the master camera. 
4. Select your region of interest (ROI) by clicking on 'Drawing Tools' and outline the shape of your test piece.     
5. By clicking on 'Processing Options' select the required correlation criterion and select 'OK'.
6. To begin the correlation, select the 'Processing' option from the menu bar and click on 'Start Correlation'.

**Calibration**:

<u>Parameters to consider:</u>


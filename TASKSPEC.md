# TASK SPECIFICATION: dalmatian-trainer

## Introduction & Motivation
Welcome to the dalmatian-trainer project. Here we will develop a set of digital and physical resources (including a 3D printable hands on rig) for new starters within our team to be able to teach themselves digital image correlation (DIC).

## Aim & Objectives
The aim of this project is to develop a set of guided laboratory exercises that can be used to train a new team member to use digital image correlation for displacement and strain measurement. The training laboratories will be broken into three parts each being an objective of the project: 1) basics of cameras and 2D-DIC, 2) Calibration and 3D-DIC (stereo), and 3) capstone project identifying the elastic modulus of a material with DIC data.

## Deliverables
**Core deliverables:**
1. Review this task specification by brainstorming anything that could be missing or could improve the training material.
2. Update the readme file to guide the user through the laboratory exercises.
3. Decide on a directory structure for the tutorial materials to be organised in the repo.
4. Review, update and gameify the 2D-DIC laboratory in the file '2d_dic_lab.md'. The laboratory should cover:
    - Pinhole camera model, lenses, magnification limits, lenses and lighting.
    - Speckle patterns and calculations to size or assess the size of speckles.
    - Length calibration for 2D-DIC
    - Rigid body and out of plane motion tests and analysis.
    - Uncertainty quantification: grey level noise analysis and noise analysis for quantities of interest (e.g. displacement / strain).
    - Limitations of 2D-DIC and why we need 3D-DIC
5. Create a 'fun' guided laboratory on 3D-DIC similar to the 2D-DIC tutorial.
    - Include details on camera setup, stereo angle trade-off/calculation and cross correlation checks.
    - A walkthrough for performing calibrations and a check list for parameters to assess calibration quality.
    - Rigid body and out of plane motion tests on a complex surface
    - Uncertainty quantification: grey level noise analysis and noise analysis for quantities of interest (e.g. displacement / strain).
6. Design a 3D printable rig for applying a mechanical loading to a test sample for modulus identification.
    - Integrate a suitable and cheap arduino based load cell
    - Provide full CAD files in FreeCAD for the rig
7. Create a laboratory exercise to use the rig to find the modulus of material.

**Extension deliverables:**
- Create installation and DIC data processing walkthroughs with Sandia's DICE



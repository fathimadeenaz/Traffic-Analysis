# Traffic Analysis

## Objective

Traffic Analysis involves the detection and classification of vehicles and plays a significant role in intelligent transportation systems. Recorded videos of the surveillance cameras of traffic prone areas are input to the application for analysis and the flow sequence of vehicles is monitored, planned and controlled.

The first section of the project involves detection of the vehicles i.e. counting and tracking them in order to calculate the traffic density. By doing so, areas most prone to blockage can be identified and traffic flow in those areas can be regulated and diverted to different lanes.

The second section of the project involves classification of vehicles. This is done in order to identify which kind of vehicles are most responsible for the increase in traffic density and thus allowing the city planners to create new alternative routes for such kinds of vehicles thereby facilitating free road movement.

## Software Requirements

-   Python v3.9.2
-   OpenCV v4.5.3
-   Numpy v1.19.5
-   YOLOv3 pre-trained model weights and config files

## What does the app do?

The user inputs traffic surveillance video saved locally. The algorithm outputs the results on the video as well as the UI. It can also be saved in the form of a csv file depending upon user preference.

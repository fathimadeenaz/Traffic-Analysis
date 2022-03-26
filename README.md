# Traffic Analysis

## Objective

Traffic Analysis involves the detection and classification of vehicles and plays a significant role in intelligent transportation systems. Recorded videos of the surveillance cameras of traffic prone areas are input to the application for analysis and the flow sequence of vehicles is monitored, planned and controlled.

The first section of the project involves detection of the vehicles i.e. counting and tracking them in order to calculate the traffic density. By doing so, areas most prone to blockage can be identified and traffic flow in those areas can be regulated and diverted to different lanes.

The second section of the project involves classification of vehicles. This is done in order to identify which kind of vehicles are most responsible for the increase in traffic density and thus allowing the city planners to create new alternative routes for such kinds of vehicles thereby facilitating free road movement.

## Software Requirements

-   Python v3.9.2
-   YOLOv4 model weights and config files
-   Coco.names file
-   OpenCV v4.5.3
-   Numpy v1.19.5
-   Pandas v1.4.1
-   Tkinter v3.10.2

## Implementation

<div align="center">
  <img src="https://user-images.githubusercontent.com/63476604/160245731-524aa3ba-5354-4426-8abd-eabc35704e0a.png" alt="Home Page">
  <div>When the app is run, the Home Page is displayed</div>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/63476604/160245292-742fde8b-93c8-42ad-9a74-5bbd12fcc176.png" alt="Input Video">
  <div>The user is then prompted to input a video of his choice</div>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/63476604/160245430-c3de3fa9-aa2f-4d6f-96f9-1b0a23122ea7.png" alt="Output Frame">
  <div>Output frame is displayed wherein detection, classification and counting of vehicles in the user selected video takes place</div>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/63476604/160245518-cec0065b-93d5-4d43-ae79-5f10962c9752.png" alt="Results Page">
  <div>Upon exiting the output frame, the results page is displayed with the option of saving the results locally in a CSV file</div>
</div>

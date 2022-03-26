# Import necessary packages

import cv2
import numpy as np
from tracker import *
import os


def foo(path):

    # Initializing Tracker
    tracker = EuclideanDistTracker()

    # Initializing videocapture object
    cap = cv2.VideoCapture(path)

    input_size = 320

    # Initializing detection confidence threshold
    confThreshold = 0.1
    nmsThreshold = 0.1

    font_color = (0, 0, 255)
    font_size = 0.5
    font_thickness = 2

    # Lines
    middle_line_position = 450
    up_line_position = middle_line_position - 15
    down_line_position = middle_line_position + 15

    # Storing Coco Names in a list
    classesFile = os.getcwd() + r"\coco.names"
    classNames = open(classesFile).read().strip().split('\n')

    # Extracting class index of required detection classes
    required_class_index = [2, 3, 5, 7]

    # Model Files
    modelConfiguration = os.getcwd() + r"\yolov3-320.cfg"
    modelWeights = os.getcwd() + r"\yolov3-320.weights"

    # Loading the YOLO network model
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    # Defining random colour for each class
    np.random.seed(42)
    colors = np.random.randint(0, 255, size = (
        len(classNames), 3), dtype = 'uint8')

    # Function for finding the center of a rectangle
    def find_center(x, y, w, h):
        x1 = int(w/2)
        y1 = int(h/2)
        cx = x + x1
        cy = y + y1
        return cx, cy

    # List for storing vehicle count info
    global up_list, down_list
    temp_up_list = []
    temp_down_list = []
    up_list = [0, 0, 0, 0]
    down_list = [0, 0, 0, 0]

    # Function for counting vehicles
    def count_vehicle(box_id, img):

        # box_id contains positional info (x,y,w,h,id,index)
        # img is the current frame

        x, y, w, h, id, index = box_id

        # Finding center of the rectangle for detection
        center = find_center(x, y, w, h)
        ix, iy = center

        # Finding current position of the vehicle

        if (iy > up_line_position) and (iy < middle_line_position):

            if id not in temp_up_list:
                temp_up_list.append(id)

        elif iy < down_line_position and iy > middle_line_position:
            if id not in temp_down_list:
                temp_down_list.append(id)

        elif iy < up_line_position:
            if id in temp_down_list:
                temp_down_list.remove(id)
                up_list[index] = up_list[index] + 1

        elif iy > down_line_position:
            if id in temp_up_list:
                temp_up_list.remove(id)
                down_list[index] = down_list[index] + 1

        # Drawing circle in the middle of the rectangle
        cv2.circle(img, center, 2, (0, 0, 255), -1)

    # Function for finding the detected objects from the network output
    def postProcess(outputs, img):
        height, width = img.shape[:2]
        boxes = []
        classIds = []
        confidence_scores = []
        detection = []
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if classId in required_class_index:
                    if confidence > confThreshold:
                        w, h = int(det[2]*width), int(det[3]*height)
                        x, y = int((det[0]*width)-w/2), int((det[1]*height)-h/2)
                        boxes.append([x, y, w, h])
                        classIds.append(classId)
                        confidence_scores.append(float(confidence))

        # Applying Non-Max Suppression
        indices = np.array(cv2.dnn.NMSBoxes(
            boxes, confidence_scores, confThreshold, nmsThreshold))
        for i in indices.flatten():

            global detected_classNames
            detected_classNames = []

            x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]

            color = [int(c) for c in colors[classIds[i]]]
            name = classNames[classIds[i]]
            detected_classNames.append(name)

            # Drawing classname and confidence score

            if name == 'truck':
                cv2.putText(
                    img, 'VAN' f'{int(confidence_scores[i]*100)}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            else:

                cv2.putText(
                    img, f'{name.upper()} {int(confidence_scores[i]*100)}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            # Drawing bounding rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            detection.append(
                [x, y, w, h, required_class_index.index(classIds[i])])

        # Updating the tracker for each object
        boxes_ids = tracker.update(detection)
        for box_id in boxes_ids:
            count_vehicle(box_id, img)

    def realTime():
        while True:
            success, img = cap.read()

            img = cv2.resize(img, (1056, 627), None, 0.5, 0.5)
            ih, iw, channels = img.shape
            blob = cv2.dnn.blobFromImage(
                img, 1/255, (input_size, input_size), [0, 0, 0], 1, crop = False)

            # Setting the input of the network
            net.setInput(blob)
            layersNames = net.getLayerNames()
            outputNames = [(layersNames[i - 1])
                for i in net.getUnconnectedOutLayers()]
            # Feeding data to the network
            outputs = net.forward(outputNames)

            # Finding the objects from the network output
            postProcess(outputs, img)

            # Drawing the crossing lines

            cv2.line(img, (0, middle_line_position),
                (iw, middle_line_position), (64, 214, 44), 1)
            cv2.rectangle(img, (5, 3), (225, 125), (255, 255, 255), 2)
            # Drawing counting texts in the frame
            cv2.putText(img, "Up", (110, 20), cv2.FONT_HERSHEY_SIMPLEX,
                font_size, (0, 0, 0), font_thickness)
            cv2.putText(img, "Down", (160, 20), cv2.FONT_HERSHEY_SIMPLEX,
                font_size, (0, 0, 0), font_thickness)
            cv2.putText(img, "Car:        " + str(up_list[0]) + "     " + str(
                down_list[0]), (20, 40), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Motorbike:  " + str(up_list[1]) + "     " + str(
                down_list[1]), (20, 60), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Bus:        " + str(up_list[2]) + "     " + str(
                down_list[2]), (20, 80), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Van:        " + str(up_list[3]) + "     " + str(
                down_list[3]), (20, 100), cv2. FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)

            cv2.putText(img, "Press Esc to exit Window", (840, 25),
                cv2. FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), 2)
                
            # Showing the frames
            cv2.imshow('Output', img)

            #Exit code
            if cv2.waitKey(1) == 27:
                global result
                result = up_list + down_list
                cap.release()
                cv2.destroyAllWindows()
                return result

    return realTime()

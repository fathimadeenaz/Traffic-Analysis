# Import necessary packages

import cv2
import numpy as np
from tracker import *

def foo(path) :
    # Initialize Tracker
    tracker = EuclideanDistTracker()

    # Initialize the videocapture object
    cap = cv2.VideoCapture(path)

    input_size = 320

    # Detection confidence threshold
    confThreshold =0.1
    nmsThreshold= 0.1

    font_color = (0, 0, 255)
    font_size = 0.5
    font_thickness = 2

    # Lines
    middle_line_position = 225   
    up_line_position = middle_line_position - 15
    down_line_position = middle_line_position + 15


    # Store Coco Names in a list
    classesFile = r"C:\Users\Deenaz\Documents\Python\MiniPro\code\coco.names"
    classNames = open(classesFile).read().strip().split('\n')

    # class index for our required detection classes
    required_class_index = [2, 3, 5, 7]

    #global detected_classNames

    ## Model Files
    modelConfiguration = r"C:\Users\Deenaz\Documents\Python\MiniPro\code\yolov3-320.cfg"
    modelWeigheights = r"C:\Users\Deenaz\Documents\Python\MiniPro\code\yolov3-320.weights"

    # configure the network model
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)

    # Configure the network backend

    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    # Define random colour for each class
    np.random.seed(42)
    colors = np.random.randint(0, 255, size=(len(classNames), 3), dtype='uint8')


    # Function for finding the center of a rectangle
    def find_center(x, y, w, h):
        x1=int(w/2)
        y1=int(h/2)
        cx = x+x1
        cy=y+y1
        return cx, cy

    # List for store vehicle count information
    global up_list, down_list
    temp_up_list = []
    temp_down_list = []
    up_list = [0, 0, 0, 0]
    down_list = [0, 0, 0, 0]

    # Function for count vehicle
    def count_vehicle(box_id, img):

        x, y, w, h, id, index = box_id

        # Find the center of the rectangle for detection
        center = find_center(x, y, w, h)
        ix, iy = center

        # Find the current position of the vehicle
        if (iy > up_line_position) and (iy < middle_line_position):

            if id not in temp_up_list:
                temp_up_list.append(id)

        elif iy < down_line_position and iy > middle_line_position:
            if id not in temp_down_list:
                temp_down_list.append(id)

        elif iy < up_line_position:
            if id in temp_down_list:
                temp_down_list.remove(id)
                up_list[index] = up_list[index]+1

        elif iy > down_line_position:
            if id in temp_up_list:
                temp_up_list.remove(id)
                down_list[index] = down_list[index] + 1

        # Draw circle in the middle of the rectangle
        cv2.circle(img, center, 2, (0, 0, 255), -1)  # end here
        # print(up_list, down_list)

    # Function for finding the detected objects from the network output
    def postProcess(outputs,img):
        #global detected_classNames
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
                        # print(classId)
                        w,h = int(det[2]*width) , int(det[3]*height)
                        x,y = int((det[0]*width)-w/2) , int((det[1]*height)-h/2)
                        boxes.append([x,y,w,h])
                        classIds.append(classId)
                        confidence_scores.append(float(confidence))

        # Apply Non-Max Suppression
        indices = np.array(cv2.dnn.NMSBoxes(boxes, confidence_scores, confThreshold, nmsThreshold))
        # print(classIds)
        for i in indices.flatten():

            global detected_classNames
            detected_classNames =[]


            x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]
            # print(x,y,w,h)

            color = [int(c) for c in colors[classIds[i]]]
            name = classNames[classIds[i]]
            detected_classNames.append(name)
            # Draw classname and confidence score 
            cv2.putText(img,f'{name.upper()} {int(confidence_scores[i]*100)}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            # Draw bounding rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            detection.append([x, y, w, h, required_class_index.index(classIds[i])])

        # Update the tracker for each object
        boxes_ids = tracker.update(detection)
        for box_id in boxes_ids:
            count_vehicle(box_id, img)


    def realTime():
        while True:
            success, img = cap.read()

            img = cv2.resize(img,(640,380),None,0.5,0.5)
            ih, iw, channels = img.shape
            blob = cv2.dnn.blobFromImage(img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)

            # Set the input of the network
            net.setInput(blob)
            layersNames = net.getLayerNames()
            outputNames = [(layersNames[i[0] - 1]) for i in net.getUnconnectedOutLayers()]
            # Feed data to the network
            outputs = net.forward(outputNames)

            # Find the objects from the network output
            postProcess(outputs,img)

            # Draw the crossing lines

            cv2.line(img, (0, middle_line_position), (iw, middle_line_position), (255, 0, 255), 2)
            cv2.line(img, (0, up_line_position), (iw, up_line_position), (0, 0, 255), 2)
            cv2.line(img, (0, down_line_position), (iw, down_line_position), (0, 0, 255), 2)

            # Draw counting texts in the frame
            cv2.putText(img, "Up", (110, 20), cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Down", (160, 20), cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Car:        "+str(up_list[0])+"     "+ str(down_list[0]), (20, 40), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Motorbike:  "+str(up_list[1])+"     "+ str(down_list[1]), (20, 60), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Bus:        "+str(up_list[2])+"     "+ str(down_list[2]), (20, 80), cv2.  FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
            cv2.putText(img, "Truck:      "+str(up_list[3])+"     "+ str(down_list[3]), (20, 100), cv2. FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)

            # Show the frames
            cv2.imshow('Output', img)

            if cv2.waitKey(1) == ord('q'):
                global result
                result = up_list+down_list
                cap.release()
                cv2.destroyAllWindows()
                return result


            
        # cap.release()
        # cv2.destroyAllWindows()
        
        # return result

    #if __name__ == '__main__':
    # realTime()

    #result = up_list.append(down_list)
    #result = [up_list[0], up_list[1], up_list[2], up_list[3], down_list[0], down_list[1], down_list[2],down_list[3]]
    #return result


    return realTime()

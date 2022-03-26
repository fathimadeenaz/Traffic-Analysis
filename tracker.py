# Import necessary packages

import math

class EuclideanDistTracker:

    # ctr

    def __init__(self):
        # Stores center positions of objects as { id : (cx,cy) }
        self.center_points = {}
        # Keeps count of the IDs and each time a new object is detected, count increases by one
        self.id_count = 0

    # Tracks objects and updates detected objects' current states in each frame

    def update(self, objects_rect):
        # objects_rect is a list containing detected objects' positional info [(x,y,w,h,index)]

        # List containing positional info about the objects that have been detected and are present in current frame
        objects_bbs_ids = []

        # Getting center point of detected objects
        for rect in objects_rect:
            x, y, w, h, index = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Finding out if the object was already detected
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id, index])
                    same_object_detected = True
                    break

            # If new object is detected, assign ID to the object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count, index])
                self.id_count += 1

        # Removing object ids that are not present in the frame anymore

        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id, index = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Updating center_points dictionary
        self.center_points = new_center_points.copy()
        return objects_bbs_ids
import cv2
import time
import numpy as np
from math import atan2
from math import pi
from otto import setServo
MODE = "MPI"

if MODE is "COCO":
    protoFile = "pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "pose/coco/pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

elif MODE is "MPI" :
    protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]


def limitTo(num,min,max):
    if(num < min):
        return min
    elif(num > max):
        return max
    else:
        return num


# POSE_PAIRS2.extend([ { "servo":3,"pair":[8,9] ,"trim":0 ,"factor":1 } ,{ "servo":2,"pair": [11,12] , "trim": 0 ,"factor":1 } ])
# POSE_PAIRS2.extend([ { "servo":3,"pair":[8,9] ,"trim" :0 ,"factor":1 } ,{ "servo":2,"pair": [11,12] , "trim": 0 ,"factor":1 } ])

# 头、脖子、左右手、左右腿、身体中心

inWidth = 368
inHeight = 368
threshold = 0.1


input_source = "sample_video.mp4"
cap = cv2.VideoCapture(input_source)
#cap = cv2.VideoCapture(0)
hasFrame, frame = cap.read()

vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

while cv2.waitKey(1) < 0:
    t = time.time()
    hasFrame, frame = cap.read()
    frameCopy = np.copy(frame)
    if not hasFrame:
        cv2.waitKey()
        break

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                              (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()

    H = output.shape[2]
    W = output.shape[3]
    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        # confidence map of corrESPonding body's part.
        probMap = output[0, i, :, :]

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
            cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)


    POSE_PAIRS2 = [ { "servo":2,"pair":[2,3] ,"trim":0 ,"factor":-1 , 'angle':-1,'rangle':-1 } ,{ "servo":3,"pair": [5,6] , "trim": 180 ,"factor":-1 , 'angle':-1,'rangle':-1} ]
    POSE_PAIRS2.extend( [ { "servo":4,"pair":[3,4] ,"trim":0 ,"factor":-1 , 'angle':-1,'rangle':-1} ,{ "servo":5,"pair": [6,7] , "trim": 180 ,"factor":-1 , 'angle':-1,'rangle':-1} ])
    for idx,item in enumerate(POSE_PAIRS2):
        partA = item['pair'][0]
        partB = item['pair'][1]
        # print(points[partB])
        if points[partA] and points[partB]:
            angle = int(atan2( points[partB][0]-points[partA][0] , points[partB][1]-points[partA][1])/pi*180)
            print((item['servo'],angle))
            # angle = limitTo(angle,10,170)
            print((item['servo'],angle))
            item['rangle'] = angle
            if(item['servo'] %2 == 0 and angle > 90):
                angle = angle - 360 
            elif(item['servo'] %2 != 0 and angle < -90):
                angle = angle + 360
            angle = limitTo(angle,item['trim']-170,item['trim']-10)
            item['angle'] = (angle*item['factor'] + item['trim'])
            # item['angle'] = limitTo(item['angle'],10,170)

            # if(item['servo'] > 3):
            #     item['angle'] = item['angle'] + POSE_PAIRS2[idx - 2]['angle']

    if( len(POSE_PAIRS2) > 2 and POSE_PAIRS2[0]['angle'] > 0 and POSE_PAIRS2[2]['angle'] > 0):
        POSE_PAIRS2[2]['angle'] = POSE_PAIRS2[2]['angle'] + (90 - POSE_PAIRS2[0]['angle'])
        POSE_PAIRS2[2]['angle'] = limitTo(POSE_PAIRS2[2]['angle'],10,170)
    if( len(POSE_PAIRS2) > 2 and POSE_PAIRS2[1]['angle'] > 0 and POSE_PAIRS2[3]['angle'] > 0):
        POSE_PAIRS2[3]['angle'] = POSE_PAIRS2[3]['angle'] + (90 - POSE_PAIRS2[1]['angle'])
        POSE_PAIRS2[3]['angle'] = limitTo(POSE_PAIRS2[3]['angle'],10,170)

    for idx,item in enumerate(POSE_PAIRS2):
            if(item['angle'] < 180 and item['angle'] > 0):
                setServo(item['servo'],item['angle'])
            print((item['servo'],item['angle']))


    cv2.putText(frame, "time taken = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    # cv2.putText(frame, "OpenPose using OpenCV", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    # cv2.imshow('Output-Keypoints', frameCopy)
    cv2.imshow('Output-Skeleton', frame)

    vid_writer.write(frame)

vid_writer.release()

import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np
import torch

import itertools
import time

from src import model
from src import util
from src.body import Body
from src.hand import Hand

body_estimation = Body('model/body_pose_model.pth')
# hand_estimation = Hand('model/hand_pose_model.pth')

print(f"Torch device: {torch.cuda.get_device_name()}")

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

start_time = time.time()
frames_counted = 0
for frame_num in itertools.count():
    ret, oriImg = cap.read()
    candidate, subset = body_estimation(oriImg)
    canvas = copy.deepcopy(oriImg)
    canvas = util.draw_bodypose(canvas, candidate, subset)

    temp_time = time.time()
    if temp_time - start_time >= 1:
        frames = frame_num - frames_counted
        print(f'\r{frames} frames in the past second', end='')
        frames_counted = frame_num
        start_time = temp_time


    # detect hand
    # hands_list = util.handDetect(candidate, subset, oriImg)

    # all_hand_peaks = []
    # for x, y, w, is_left in hands_list:
    #     peaks = hand_estimation(oriImg[y:y+w, x:x+w, :])
    #     peaks[:, 0] = np.where(peaks[:, 0]==0, peaks[:, 0], peaks[:, 0]+x)
    #     peaks[:, 1] = np.where(peaks[:, 1]==0, peaks[:, 1], peaks[:, 1]+y)
    #     all_hand_peaks.append(peaks)

    # canvas = util.draw_handpose(canvas, all_hand_peaks)

    cv2.imshow('demo', canvas)#一个窗口用以显示原视频
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

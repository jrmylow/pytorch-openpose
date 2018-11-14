import sys
sys.path.insert(0, 'python')
import cv2
import model
import util
from hand import Hand
from body import Body
import matplotlib.pyplot as plt
import copy

body_estimation = Body('model/body_pose_model.pth')
hand_estimation = Hand('model/hand_pose_model.pth')

test_image = 'images/demo.jpg'
oriImg = cv2.imread(test_image)  # B,G,R order
candidate, subset = body_estimation(oriImg)
# canvas = util.draw_bodypose(oriImg, candidate, subset)
canvas = copy.deepcopy(oriImg)
# detect hand
hands_list = util.handDetect(candidate, subset, oriImg)

for x, y, w, is_left in hands_list:
    cv2.rectangle(canvas, (x, y), (x+w, y+w), (0, 255, 0), 2, lineType=cv2.LINE_AA)
    cv2.putText(canvas, 'left' if is_left else 'right', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if is_left:
        plt.imshow(oriImg[y:y+w, x:x+w, :][:, :, [2, 1, 0]])
        plt.show()
        # peaks = hand_estimation(oriImg[y:y+w, x:x+w, :])
        # canvas = util.draw_handpose(canvas, peaks, True)

plt.imshow(canvas[:, :, [2, 1, 0]])
plt.show()
# cv2.imwrite('t.jpg', canvas)
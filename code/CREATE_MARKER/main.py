import cv2 as cv
from cv2 import aruco
import numpy as np

# تحديد القاموس المستخدم
marker_dice = aruco.Dictionary_get(aruco.DICT_4X4_50)

MARKER_SIZE = 400

for id in range(20):
    # إنشاء صورة بيضاء لرسم الماركر عليها
    marker_image = np.ones((MARKER_SIZE, MARKER_SIZE), dtype=np.uint8) * 255
    
    # رسم الماركر على الصورة
    marker_image = aruco.drawMarker(marker_dice, id, MARKER_SIZE)
    
    # عرض الصورة
    cv.imshow("Marker ID: " + str(id), marker_image)
    cv.waitKey(0)
    break

cv.destroyAllWindows()

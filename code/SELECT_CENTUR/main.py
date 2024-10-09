# import cv2 as cv 
# from cv2 import aruco
# import numpy as np

# marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# param_markers = aruco.DetectorParameters_create()

# cup = cv.VideoCapture(0)

# while True:
#     ret , frame = cup.read()
#     if not ret:
#         break
#     gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
#     marker_corners , marker_IDs , reject = aruco.detectMarkers(
#         gray_frame,
#         marker_dict,
#         parameters=param_markers
#     )
#     if marker_corners :
#         for ids ,corners in zip(marker_IDs , marker_corners):
#             cv.polylines(frame , [corners.astype(np.int32)] ,True ,(0,255,255) , 4 , cv.LINE_AA)
#             # print(ids , " " , corners) 
#             corners = corners.reshape(4,2)
#             corners = corners.astype(int)
#             top_right = corners[0].ravel()
#             cv.putText( frame,
#                         f"ID : {ids[0]}",
#                         top_right,
#                         cv.FONT_HERSHEY_PLAIN,
#                         1.3,
#                         (200,100,0),
#                         2,
#                         cv.LINE_AA
#                     )

#     cv.imshow("frame",frame)
#     key = cv.waitKey(1)
#     if key == ord('q'):
#         break
# cup.release() 
# cv.destroyAllWindows()

import cv2 as cv 
from cv2 import aruco
import numpy as np

# تحميل قاموس الماركرات
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# إعدادات كشف الماركرات
param_markers = aruco.DetectorParameters_create()

# فتح كاميرا Iriun Webcam (عادةً تكون ID=1)
cup = cv.VideoCapture(1)  # استخدم ID=1 لكاميرا Iriun

while True:
    ret, frame = cup.read()
    if not ret:
        break
    
    # تحويل الإطار إلى الصورة الرمادية
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # اكتشاف الماركرات في الإطار
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame,
        marker_dict,
        parameters=param_markers
    )
    
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            # رسم الخطوط حول الماركرات
            cv.polylines(frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA)
            
            # تحويل الزوايا إلى إحداثيات صحيحة
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            
            # تحديد الزاوية العلوية اليمنى لوضع النص
            top_right = corners[0].ravel()
            cv.putText(frame,
                       f"ID : {ids[0]}",
                       top_right,
                       cv.FONT_HERSHEY_PLAIN,
                       1.3,
                       (255, 255, 255),
                       2,
                       cv.LINE_AA
                       )

            # حساب نقطة المركز
            center = np.mean(corners, axis=0).astype(int)
            
            # رسم دائرة في نقطة المركز
            cv.circle(frame, tuple(center), 5, (0, 0, 255), -1)  # اللون الأحمر
            
    # عرض الإطار
    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    if key == ord('q'):
        break

# إغلاق الكاميرا
cup.release() 
cv.destroyAllWindows()

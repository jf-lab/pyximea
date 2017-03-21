import pyximea as xi
import logging
import cv2
from time import time
logging.basicConfig(level=logging.DEBUG)


print(xi.get_device_count())

cam = xi.Xi_Camera(DevID=0)
cam.set_debug_level("Warning")
ts= time()
cam.set_param('exposure',10.0)
cam.set_param('aeag',1)
cam.set_param('exp_priority',0)
cam.set_binning(4, skipping=False)
print(cam.get_param('framerate',float))
while True:
    dt,ts = time()-ts,time()
    img =  cam.get_image()

    cv2.imshow("test",img)
    k = cv2.waitKey(1)
    if k % 255 == ord("x"):
        break

cam.close()



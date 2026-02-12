import cv2 # capture umage, display image, process image
from pal.products.qcar import QCarRealSense, IS_PHYSICAL_QCAR

myCam = QCarRealSense(mode= "RGB, Depth")
try:
    while True:
        myCam.read_RGB()
        cv2.imshow('My RGB', myCam.imageBufferRGB)

        myCam.read_depth()
        cv2.imshow('My Depth', myCam.imageBufferDepthPX)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("stopping")
            break

except KeyboardInterrupt:
    print("exit")

cv2.destroyAllWindows()

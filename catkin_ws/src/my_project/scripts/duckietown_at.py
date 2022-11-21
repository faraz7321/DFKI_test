# %%
# Import libraries

from dt_apriltags import Detector
import argparse
import cv2

# %%
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="absolute path to input image containing AprilTag")
args = vars(ap.parse_args())

# %%
# using duckietown based apriltags detector

at_detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)

# %%
print("\nTESTING WITH A SAMPLE IMAGE")

img = cv2.imread(args["image"])  # colored image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale image

# %%
tags = at_detector.detect(gray)
print(tags)

# %%
# add tags in image
for tag in tags:

    # draw border lines
    for idx in range(len(tag.corners)):
        cv2.line(img, tuple(
            tag.corners[idx-1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)), (0, 255, 0))

    # add text in image
    cv2.putText(img, "Tag " + str(tag.tag_id),
                org=(tag.center[0].astype(int),
                     tag.center[1].astype(int)),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5,
                color=(0, 255, 0))

# %%
cv2.imshow('Detected tags', img)
cv2.imwrite('output.png', img)

# %%
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

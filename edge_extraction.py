import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def auto_canny(image, sigma=0.33):
	# Compute the median of the single channel pixel intensities
	v = np.median(image)

	# Apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	return cv2.Canny(image, lower, upper)

if __name__ == '__main__':
	images = [cv2.imread(file) for file in glob.glob('simple_images/ghost_test/*')]

	number = 0
	for image in images:
		canny = auto_canny(image)
		# cv2.imshow('canny', canny)
		# img= cv2.resize(canny, (208, 242), interpolation = cv2.INTER_AREA)
		cv2.imwrite('A/{}.png'.format(number), canny)
		number += 1

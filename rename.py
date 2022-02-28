import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

if __name__ == '__main__':
	images = [cv2.imread(file) for file in glob.glob('test_set/*')]

	number = 0
	for image in images:
		cv2.imwrite('B/{}.png'.format(number), image)
		number += 1

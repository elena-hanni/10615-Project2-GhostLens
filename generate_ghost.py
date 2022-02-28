import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
from PIL import Image

# For each image in the background folder, we will create a blank canvas and random ghost shape on it.
mypath = "ghost_generation/bg/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
ghost_path = "ghost_generation/ghost_shape/"
ghost_shapes = [f for f in listdir(ghost_path) if isfile(join(ghost_path, f)) and f != ".DS_Store"]

for filename in onlyfiles:
    bg_img = Image.open(mypath + filename)
    new_name = "ghost_" + filename
    width, height = bg_img.size
    # create white canvas
    whiteFrame = 255 * np.ones((height, width, 3), np.uint8)
    im = Image.fromarray(whiteFrame)
    ghost_num = np.random.randint(len(ghost_shapes))
    ghost_name = ghost_shapes[ghost_num]
    ghost_img = Image.open(ghost_path + ghost_name)
    new_width = np.random.randint(width / 4, high=width * 4 / 5)
    new_height = np.random.randint(height / 4, high=height * 4 / 5)
    newsize = (new_width, new_height)
    resized_ghost = ghost_img.resize(newsize)
    random_width = np.random.randint(low=0,high=width - new_width)
    random_height = np.random.randint(low=0, high=height - new_height)
    im.paste(resized_ghost, (random_width, random_height))
    im.save('ghost_generation/ghost_background/' + new_name)

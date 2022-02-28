import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageFilter

# bg is the folder that holds the background images
mypath = "image_processing/bg/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f != ".DS_Store"]
# good is the folder that holds the best ghost results from pix2pix
layerpath = "image_processing/good/"
layerfiles = [f for f in listdir(layerpath) if isfile(join(layerpath, f)) and f != ".DS_Store"]
# load the ghost background generated by blank image
ghost_bg = Image.open("image_processing/ghost_bg.png")

for filename in onlyfiles:
    if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
        print("Background: " + filename)
        bg_img = Image.open(mypath + filename)
        for layername in layerfiles:
            print("Layer: " + layername)
            current_img = bg_img.copy()
            current_bg = ghost_bg.resize(bg_img.size)
            current_bg.putalpha(127)
            current_img.paste(current_bg, (0,0), current_bg)
            new_name = filename + layername
            layer_img = Image.open(layerpath + layername)
            width, height = bg_img.size
            resized_layer = layer_img.resize(bg_img.size)
            # resized_layer = layer_img.copy()
            resized_layer.putalpha(127)
            current_img = current_img.filter(ImageFilter.GaussianBlur(radius = 3))
            layer_width, layer_height = resized_layer.size
            current_img.paste(resized_layer, (0, 0), resized_layer)
            # bg_img.show()
            current_img.save('final_result/' + new_name)
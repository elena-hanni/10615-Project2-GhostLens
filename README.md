# 10615-Project2-GhostLens
Elena Gong(yezheng), Zixuan Zou(zixuanz)

By training pix2pix models and applying image filters, Ghost Lens provides people with a chance to take a look at ghosts from a different perspective.

**Folders**

ghost_dataset: ghost images for pix2pix model training and testing

traffic: traffic lights images for pix2pix model training and testing

results: output images of pix2pix models mapping from traffic lights to ghosts, ghosts to ghosts, and drawings to ghosts

output: comparing output images of pix2pix models with different sizes

final_result: images that combine the output images from pix2pix and background images

cartoon_ghost_attempt: cute ghost images and fire hydrants that we tried for experiments

ghost_generation: images and outputs for generating random ghosts 

image_processing: images used for combining images and generating final results


**Files**

image_download.py: using simple_image_download to download images with specified keywords

edge_extraction.py: using auto_canny() to extract edges from images

rename.py: renaming all the images files and converting the format

image_augment.py: using Augmentor to apply various augmentations to images

image_resize.py: using Python Pillow Library to resize downloaded images 

generate_ghost.py: using Python Pillow Library and Numpy to randomly generate background image size white canvas with ghosts

combine_image.py: using Python Pillow Library to add the results of pix2pix to background images and generate the final result



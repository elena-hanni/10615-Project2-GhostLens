# 10615-Project2-GhostLens
Elena Gong(yezheng), Zixuan Zou(zixuanz)

By training pix2pix models and applying image filters, Ghost Lens provides people with a chance to take a look at ghosts from a different perspective.

**Folders**

ghost_dataset: ghost images for pix2pix model training and testing

traffic: traffic lights images for pix2pix model training and testing

results: output images of pix2pix models mapping from traffic lights to ghosts, ghosts to ghosts, and drawings to ghosts

output: comparing output images of pix2pix models with different sizes

**Files**

image_download.py: using simple_image_download to download images with specified keywords

edge_extraction.py: using auto_canny() to extract edges from images

rename.py: renaming all the images files and converting the format

image_augment.py: using Augmentor to apply various augmentations to images



from PIL import Image
from os import listdir
from os.path import isfile, join

mypath = "cartoon_ghost_attempt/ghost_cute/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in onlyfiles:
    im = Image.open(mypath + filename)
    new_file_name = "resized_" + filename
    # print(new_file_name)
    newsize = (300, 300)
    im1 = im.resize(newsize)
    if new_file_name.endswith(".gif"):
        filename = filename.split(".", 1)[0]
        im1 = im1.save("resized_ghost/" + filename + ".png", 'png', optimize=True, quality=70)
    else:
        im1 = im1.save("resized_ghost/" + filename)
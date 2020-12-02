''' This function returns an image with the colors that can be used in 
    scribbl.io
    {white, light_grey, red, terracotta, yellow, light_green, light_blue, blue, light_purple, pale_pink, light_brown}
    {black, dark_grey, dark_red, dark_terracotta, dirty_yellow, dark_green, muddy_blue, dark_blue, dark_purple, grey_pink, dark_brown}
    scribbl.io draw size == (835, 624)
'''

# TODO: Implement a cache function, that compares downloaded pictures in pics, .jpg's in jpg and generated pictures in gen
# TODO: 

import os, sys
import time
from PIL import Image, ImageDraw

draw_size = (825, 624)

file = os.path.dirname(os.path.realpath(__file__))
folder_entries = os.listdir(file + '/pics')

all_pics = [pic for pic in folder_entries if "." in pic[-4:]]

for im in all_pics:
    img = Image.open('/jpg/file{}.jpg'.format(im))

"""
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
"""
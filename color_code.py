import os, sys
import numpy
from PIL import Image, ImageDraw

color_map = [['white', (255,255,255)], ['light_grey', (193,193,193)], ['red', (240, 19, 11)], ['terracotta', (255, 113, 1)], 
            ['yellow', (255, 228, 0)], ['light_green', (1, 204, 0)], ['light_blue', (1, 178, 255)], ['blue', (35, 32, 211)], 
            ['light_purple', (173, 0, 185)], ['pale_pink', (211, 124, 169)], ['light_brown', (160, 82, 44)], ['black', (0,0,0)], 
            ['dark_grey', (76, 76, 76)], ['dark_red', (116, 11 , 7)], ['dark_terracotta', (195, 56, 1)], ['dirty_yellow', (231, 162, 0)], 
            ['dark_green', (0, 85, 17)], ['muddy_blue', (0, 85, 158)], ['dark_blue', (13, 8, 100)], ['dark_purple', (84, 0 , 104)], 
            ['grey_pink', (166, 85,117)], ['dark_brown', (98, 48, 13)]]

def map_func(img_name, path, save_path, map):
    ''' img is the image you want to map to scribbl.io colours
        map is the available colors on scribbl.io
    '''
    img = Image.open(path + img_name)
    img = img.copy()
    img.convert('RGB')
    for x in range(img.width):
        for y in range(img.height):
            current_working_pixel = img.getpixel((x,y))
            # print(map[0][1])
            new_pixel = [map[0], 1000]
            for color in map:
                balance = numpy.subtract(current_working_pixel, color[1])
                balance = (abs(balance[0]), abs(balance[1]), abs(balance[2]))
                div = sum(list(balance))
                if new_pixel[1] > div:
                    new_pixel = [color, div]
            img.putpixel((x,y), new_pixel[0][1])

    img.save(save_path + 'qubed_{}'.format(img_name), 'jpeg')


file = os.path.dirname(os.path.realpath(__file__))
jpg_loc = file + '/jpg/'
gen_loc = file + '/gen/'

jpgs = os.listdir(file + '/jpg')

pics = [pic for pic in jpgs]
for pic in pics:
    print(pic)
    map_func(pic, jpg_loc, gen_loc, color_map)
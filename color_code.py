import os, sys
import numpy
import time
import math
from PIL import Image, ImageDraw

color_map = [['white', (255,255,255)], ['light_grey', (193,193,193)], ['red', (240, 19, 11)], ['terracotta', (255, 113, 1)], 
            ['yellow', (255, 228, 0)], ['light_green', (1, 204, 0)], ['light_blue', (1, 178, 255)], ['blue', (35, 32, 211)], 
            ['light_purple', (173, 0, 185)], ['pale_pink', (211, 124, 169)], ['light_brown', (160, 82, 44)],
            ['black', (0,0,0)], ['dark_grey', (76, 76, 76)], 
            ['dark_red', (116, 11 , 7)], ['dark_terracotta', (195, 56, 1)], ['dirty_yellow', (231, 162, 0)], 
            ['dark_green', (0, 85, 17)], ['muddy_blue', (0, 85, 158)], ['dark_blue', (13, 8, 100)], ['dark_purple', (84, 0 , 104)], 
            ['grey_pink', (166, 85,117)], ['dark_brown', (98, 48, 13)]
            ]

def map_func(img_name, path, save_path, map):
    ''' img is the image you want to map to scribbl.io colours
        map is the available colors on scribbl.io
    '''
    red_factor = 0.2
    green_factor = 0.7
    blue_factor = 0.1
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
                balance = (abs(red_factor * balance[0]), abs(green_factor * balance[1]), abs(blue_factor * balance[2]))
                div = sum(list(balance))
                if new_pixel[1] > div:
                    new_pixel = [color, div]
            img.putpixel((x,y), new_pixel[0][1])

    img.save(save_path + 'factor_2_7_10{}'.format(img_name), 'jpeg')


def simple_hex_map(img_name, path, save_path, map):
    # the higher the factor the more important is the value
    red_factor = 0.3
    green_factor = 0.6
    blue_factor = 0.6
    img = Image.open(path + img_name)
    img = img.copy()
    img.convert('RGB')
    for x in range(int(math.floor(img.width/6))):
        for y in range(int(math.floor(img.height/6))):
            pixel = img.getpixel((x*6, y*6))
            new_pixel = [map[0], 1000000]

            for color in map:
                balance = numpy.subtract(pixel, color[1]) # square_variant numpy.subtract(numpy.multiply(current_working_pixel, current_working_pixel), numpy.multiply(color[1],color[1]))
                smallest_diff = [0, 0]
                for i in range(len(balance)):
                    if smallest_diff[0] > balance[i]:
                        smallest_diff[0],smallest_diff[1] = balance[i], i
                balance = (abs(red_factor * balance[0])**2, abs(green_factor * balance[1])**2, abs(blue_factor * balance[2]**2))
                div = 0
                for h in range(len(balance)):
                    div += math.sqrt(balance[h])
                
                #for j in range(3):
                #    if j != i:
                #        div += balance[i]**2
                #    else:
                #        div += balance[i]
                
                if new_pixel[1] > div:
                    new_pixel = [color, div]
                
            for i in range(6):
                for j in range(6):
                    img.putpixel((x*6+i,y*6+j), new_pixel[0][1])

    img.save(save_path + '{}'.format(img_name), 'jpeg')


"""def hexa_map_func(img_name, path, save_path, map):
    ''' img is the image you want to map to scribbl.io colours
        map is the available colors on scribbl.io
        uses the smallest brush size to generate a pic
    '''
    red_factor = 1
    green_factor = 0.2
    blue_factor = 0.40
    img = Image.open(path + img_name)
    img = img.copy()
    img.convert('RGB')
    for x in range(int(math.floor(img.width/6))):
        for y in range(int(math.floor(img.height/6))):
            pixel_map = []
            for i in range(6):# goal is to have a 36 elements matrix in a 6x6 cluster
                pixel_map.append((x * 6 + i , y * 6 + i))
            for z in range(len(pixel_map)):
                input_x, input_y = pixel_map[z]
                new_pixel_map_entity = img.getpixel(pixel_map[z])

            avg = [0,0,0]
            for el in new_pixel_map_entity:
                avg = numpy.add(avg, el)
            current_working_pixel = [round(k/len(new_pixel_map_entity)) for k in avg]            
            new_pixel = [map[0], 1000000]

            for color in map:
                balance = numpy.subtract(current_working_pixel, color[1]) # square_variant numpy.subtract(numpy.multiply(current_working_pixel, current_working_pixel), numpy.multiply(color[1],color[1]))
                smallest_diff = [0, 0]
                for i in range(len(balance)):
                    if smallest_diff[0] > balance[i]:
                        smallest_diff[0],smallest_diff[1] = balance[i], i
                balance = (abs(red_factor * balance[0])**2, abs(green_factor * balance[1])**2, abs(blue_factor * balance[2]**2))
                div = 0
                # for h in range(len(balance)):
                #     div += math.sqrt(balance[h])
                
                for j in range(3):
                    if j == i:
                        div += balance[i]**2
                    else:
                        div += balance[i]
                
                if new_pixel[1] > div:
                    new_pixel = [color, div]
                
            for i in range(6):
                for j in range(6):
                    img.putpixel((x*6+i,y*6+j), new_pixel[0][1])

    img.save(save_path + 'hexa/' + 'simple_biggest_{}'.format(img_name), 'jpeg')
"""

file = os.path.dirname(os.path.realpath(__file__))
jpg_loc = file + '/jpg/'
gen_loc = file + '/gen/'
jpgs = os.listdir(file + '/jpg')
pics = [pic for pic in jpgs]

for pic in pics:
    print(pic)
    start_time = time.time()
    simple_hex_map(pic, jpg_loc, gen_loc, color_map)
    print("--- %s seconds ---" % (time.time() - start_time))
    
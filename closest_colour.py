''' This function returns an image with the colors that can be used in 
    scribbl.io
    {white, light_grey, red, terracotta, yellow, light_green, light_blue, blue, light_purple, pale_pink, light_brown}
    {black, dark_grey, dark_red, dark_terracotta, dirty_yellow, dark_green, muddy_blue, dark_blue, dark_purple, grey_pink, dark_brown}
'''

from PIL import Image, ImageDraw

img = Image.new('RGB', (60,30), color ="red")
img.save('pil_red.jpg')
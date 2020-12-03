import os

def restruc(path, pic_name):
    print(path)
    f = open(path + pic_name, 'r')
    unstruct = f.read()
    f.close()
    print(unstruct)


file = os.path.dirname(os.path.realpath(__file__))
txt_location = file + '/gen/txt/'

for i in os.listdir(txt_location):
    restruc(txt_location, i)

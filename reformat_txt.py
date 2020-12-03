import os

color_map = {'white': (255,255,255),'light_grey': (193,193,193),'red': (240,19,11),'terracotta': (255,113,1),'yellow': (255,228,0),
'light_green': (1,204,0),'light_blue': (1,178,255),'blue': (35,32,211),'light_purple': (173,0,185),'pale_pink': (211,124,169),
'light_brown': (160,82,44),'black': (0,0,0),'dark_grey': (76,76,76),'dark_red': (116,11,7),'dark_terracotta': (195,56,1),
'dirty_yellow': (231,162,0),'dark_green': (0,85,17),'muddy_blue': (0,85,158),'dark_blue': (13,8,100),'dark_purple': (84,0,104),
'grey_pink': (166,85,117),'dark_brown': (98,48,13)}

def restruc(matrix, path, pic_txt):
    print(path)
    f = open(path + pic_txt, 'r')
    unstruct = f.readlines()
    f.close()
    struct = [[x] for x in matrix]
    #print(unstruct)
    # print(struct)
    for el in unstruct:
        form_el = el.split(':')
        form_el[0] = form_el[0].replace('\'','')
        #print('el: ',form_el[0])
        for keys in struct:
            form_keys = keys[0].replace('[', '').replace(']','')
            # print('keys: ',form_keys)
            if form_el[0] == form_keys:
                keys.append(form_el[1][:-1])
                break
    string = ''
    for x in range(len(struct)):
        string += str(struct[x]) + '\n'
    
    g = open(path[:-4] + 'struc/' + pic_txt, 'w')
    g.write(str(string))
    g.close()

def main(map):
    file = os.path.dirname(os.path.realpath(__file__))
    txt_location = file + '/gen/txt/'
    for i in os.listdir(txt_location):
        restruc(map, txt_location, i)


if __name__ == '__main__':
    main(color_map)
import os

def cache(pics, picture_location, file_location):
    # generate
    g = open(file_location + '//cache_jpg.txt', 'w')
    g.write(str(os.listdir(file_location + '/jpg/')))
    g.close()
    h = open(file_location + '/cache_gen.txt', 'w')
    h.write(str(os.listdir(picture_location)))
    h.close()
    

    in_jpg = open(file_location + '/cache_jpg.txt', 'r')
    in_gen = open(file_location + '/cache_gen.txt', 'r')
    baseline_pics = in_jpg.read().strip('[').strip(']').split(',')
    generated_pics = in_gen.read().strip('[').strip(']').split(',')
    # in_jpg.close()
    # in_gen.close()

    uncached = []
    print(baseline_pics)
    print(generated_pics)
    for pic in baseline_pics:
        # print(pic)
        if pic in generated_pics:
            print('{} is already cached.'.format(pic))
        else:
            print('{} has yet to be generated and cached.'.format(pic))
            uncached.append(pic)
    return(uncached)


file_loc = os.path.dirname(os.path.realpath(__file__))
jpg_loc = file_loc + '/jpg/'
gen_loc = file_loc + '/gen/'

files_in_folder = os.listdir(gen_loc)

new_img = cache(files_in_folder, gen_loc, file_loc)
print(new_img)


# TODO: generate new cache after running main.
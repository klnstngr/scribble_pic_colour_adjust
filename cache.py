import os

def cache(pics, file_location):
    # generate
    to_strip=['\'', '[',']']
    g = open(file_location + '//cache_jpg.txt', 'w')
    save = (str(os.listdir(file_location + '/jpg/'))).replace('\'', '').replace('[', '').replace(']', '')
    g.write(save)
    g.close()
    h = open(file_location + '/cache_gen.txt', 'w')
    save = (str(os.listdir(file_location + '/gen'))).replace('\'', '').replace('[', '').replace(']', '')
    h.write(save)
    h.close()
    

    in_jpg = open(file_location + '/cache_jpg.txt', 'r')
    in_gen = open(file_location + '/cache_gen.txt', 'r')
    baseline_pics = in_jpg.read().split(', ')
    generated_pics = in_gen.read().split(', ')
    generated_pics = [item.strip('\'').strip(' ') for item in generated_pics]
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
files_in_folder = os.listdir(file_loc + '/gen/')

new_img = cache(files_in_folder, file_loc)
print(new_img)

if __name__ == '__main__':
    main()
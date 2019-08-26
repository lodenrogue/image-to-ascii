from skimage import color, io
import sys


def run():
    if len(sys.argv) < 2:
        print('Image path is required')
        quit(1)

    original_image = io.imread(sys.argv[1])
    bw_image = color.rgb2gray(original_image)

    result = to_ascii(bw_image)
    print(result)


def to_ascii(bw_image):
    result = ''
    for i in range(len(bw_image)):
        for j in range(len(bw_image[i])):
            pixel = bw_image[i][j]
            if pixel > 0.8:
                result += '@'
            elif pixel > 0.6:
                result += '#'
            elif pixel > 0.4:
                result += '&'
            elif pixel > 0.2:
                result += '%'
            else:
                result += ' '

        result += '\n'
    return result


run()

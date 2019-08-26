import cv2
import sys
import numpy as np


class SmallImageException(Exception):
    pass


def insert_bit(b, data):
    if data % 2 == 1:
        if b % 2 == 0:
            b += 1
    else:
        if b % 2 == 1:
            b -= 1
    return b


def estenografia_c(image, txt):
    old_shape = image.shape
    image = np.reshape(image, (np.prod(image.shape)))
    if len(image) - 32 < len(txt) * 8:
        raise SmallImageException
    txt = txt.encode('utf-8')
    txt_size = len(txt)
    byte_image_index = 0
    while byte_image_index < 32:
        b = image[byte_image_index]
        b = insert_bit(b, txt_size)
        image[byte_image_index] = b
        txt_size = txt_size >> 1
        byte_image_index += 1
    for byte_text_index in range(len(txt)):
        c = txt[byte_text_index]
        for i in range(8):
            b = image[byte_image_index]
            b = insert_bit(b, c)
            image[byte_image_index] = b
            c = c >> 1
            byte_image_index += 1
    return np.reshape(image, old_shape)


def estenografia_d(image):
    image = np.reshape(image, (np.prod(image.shape)))
    txt_size = 0
    txt = bytearray()
    byte_image_index = 0
    while byte_image_index < 32:
        txt_size = txt_size >> 1
        b = image[byte_image_index]
        txt_size += (b % 2) * (2 ** 31)
        byte_image_index += 1
    if len(image) - 32 < txt_size * 8:
        raise SmallImageException
    for byte_text_index in range(txt_size):
        c = 0
        for i in range(8):
            c = c >> 1
            b = image[byte_image_index]
            c += (b % 2) * (2 ** 7)
            byte_image_index += 1
        txt.append(c)
    return txt.decode('utf-8')


def main():
    if (sys.argv[1] == "-d"):
        image = cv2.imread(sys.argv[2], -1)
        txt = estenografia_d(image)
        print(txt)
        open(sys.argv[3], 'w').write(txt)
        print("Done!")
    elif (sys.argv[1] == "-c"):
        image = cv2.imread(sys.argv[2], -1)
        txt = open(sys.argv[3]).read()
        try:
            out = estenografia_c(image, txt)
            cv2.imwrite(sys.argv[4], out)
            print("Done!")
        except SmallImageException:
            print("The image is to small for the size of the text")
    else:
        print("Invalid option, arguments should be [-c, image_path, txt_path, out_path] or [-d, image_path, txt_path]")


if __name__ == '__main__':
    main()

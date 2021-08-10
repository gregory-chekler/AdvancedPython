#!/usr/bin/python
#img_processing.py

'''Holds functions that preform specific tasks related to changin images'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'

from PIL import Image

def inversion(image_path):
    '''Changing each pixel to the opposite value to create an image that is the color inverse of the original

    :param image_path: the initial image path
    :return: the new image
    '''
    # NOTE: open the use the image_path to open the image and store in "image"
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            #Finds the reserse by subtracting the highest value by the origional to get the new value
            r = 255 - red_amt
            g = 255 - green_amt
            b = 255 - blue_amt

            new_image.putpixel((col, row), (r, g, b))

    return new_image

def lighten_darken(image_path, adjust=20):
    """Taking the image and making it lighter or darker as a whole

    :param image_path: the initial image path
    :param adjust: the value that will change the picture to become lighter or darker
    :return: the new image
    """
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            #adjucst each pixels value by the adjust variable to lighten or darken th image as a whole
            r = red_amt + adjust
            g = green_amt + adjust
            b = blue_amt + adjust

            new_image.putpixel((col, row), (r, g, b))

    return new_image


def greyscale(image_path):
    """taking and original image and creating a greyscale version of it

    :param image_path: the initial image path
    :return: the new image
    """
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    #average value to implement greyscale set at 0 to begin with
    avg = 0
    net_avg = 0


    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt


            avg = (r+g+b)//3 #calculation to get the average value
            net_avg = net_avg + avg #this is used for the black_and_white function to save processing time

            new_image.putpixel((col, row), (avg, avg, avg))

    net_avg = net_avg//(width*height)
    return new_image, net_avg #returns both; only the image is used and net_avg is used for next function

def black_and_white(image_path):
    """Creates a black and white image

    :param image_path: the original image path
    :return: the new image
    """

    img = greyscale(image_path)[0]
    net_avg = greyscale(image_path)[1]
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    # average value to implement greyscale set at 0 to begin with
    avg = 0

    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt

            #averages the values and then checks it against the net_avg
            # which determines if the pixel should be black or white
            avg = (r + g + b) // 3

            if avg > net_avg:
                new_image.putpixel((col, row), (255, 255, 255))
            if avg < net_avg:
                new_image.putpixel((col, row), (0, 0, 0))

    return new_image

def filter(image_path, red, green, blue):
    """A filter that will allow the user to change the color of the image to a specific value
    if the image has RGB that are over 128

    :param image_path: the initial image path
    :param red: the desired red value that will be tested against the RGB value
    :param green: the desired green value that will be tested against the RGB value
    :param blue: the desired blue value that will be tested against the RGB value
    :return: the new image
    """
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt

            #Checks if the RGB value is above 128, and if it is, the pixel is assigned with a new values
            if r > 128:
                if g > 128:
                    new_image.putpixel((col, row), (red, green, b))
                    if b > 128:
                        new_image.putpixel((col, row), (red, green, blue))
                elif b > 128:
                    new_image.putpixel((col, row), (red, g, blue))
                new_image.putpixel((col, row), (red, g, b))
            elif g > 128:
                if r > 128:
                    new_image.putpixel((col, row), (red, green, b))
                    if b > 128:
                        new_image.putpixel((col, row), (red, green, blue))
                elif b > 128:
                        new_image.putpixel((col, row), (r, green, blue))
                new_image.putpixel((col, row), (r, green, b))
            elif b > 128:
                if r > 128:
                    new_image.putpixel((col, row), (red, g, blue))
                    if g > 128:
                        new_image.putpixel((col, row), (red, green, blue))
                elif g > 128:
                        new_image.putpixel((col, row), (r, green, blue))
                new_image.putpixel((col, row), (r, g, blue))
            else:
                new_image.putpixel((col, row), (r, g, b))

    return new_image
def reverse(image_path):
    '''taking the origional image and reverse it so that the left side becomes the right and vice-versa

        :param image_path: the initial image path
        :return: the new image
        '''
    # NOTE: open the use the image_path to open the image and store in "image"
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (width, height), "blue")
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt

            #it takes the origional length and then substracts
            # the column - 1 in order to get pixel to the opposite side
            new_image.putpixel((width - col - 1, row), (r, g, b))

    return new_image



def save(image):
    """it saves the image to a folder

    :param image: the initial image
    :return: a saved image
    """
    image.save('new_images/new.png')

def show(image):
    """It displays the image that the functions create

    :param image: the image altered by the functions
    :return: displays it on the screen
    """
    image.show()
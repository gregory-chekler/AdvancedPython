#!/usr/bin/python
#adv_img_processing.py

'''Holds functions that preform specific advanced tasks related to changing images'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'

from PIL import Image
import random

def edge_detection(image_path):
    """detects the edges of an image and then creates a new image
    that gives an outline

    :param image_path: the initial image path
    :return: an image that outlines the initial image
    """
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    diff = 20 #this is the value (compared to avg) that differentiates between edges and continuations

    new_image = Image.new("RGBA", (width-1, height), "blue")
    for col in range(width-1):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt

            avg = (r + g + b) // 3

            current_pixel = img.getpixel((col+1, row))
            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r_prime = red_amt
            g_prime = green_amt
            b_prime = blue_amt

            avg_prime = (r_prime + g_prime + b_prime) // 3

            #this finds the edge by looking at the average value for the first pixel and then
            #average value for the next pixel pixel and then compares
            if abs(avg - avg_prime) >= diff:
                new_image.putpixel((col, row), (0, 0, 0))
            if abs(avg - avg_prime) < diff:
                new_image.putpixel((col, row), (255, 255, 255))

    return new_image

def draw():
    """draws a pattern

    :return: an image with a pattern
    """
    col_coord = 0
    row_coord = 0
    new_image = Image.new("RGBA", (1920, 1080), "blue")
    for col in range(1920):
        for row in range(1080):
            new_image.putpixel((col, row), (255, 255, 255))
    for x in range(6):
        for i in range(8):
            for i in range(100):
                    new_image.putpixel((col_coord + i, row_coord + i), (0, 0, 0))
            for i in range(100):
                    new_image.putpixel(((col_coord + 100) + i, (row_coord + 100) - i), (0, 0, 0))
            col_coord += 200 #this is the distance between the beggining and end of one triangle
        col_coord = 0 #resets the column val so the next row of triagles can be made
        row_coord += 150 #this is the distance from top to bottom of the triangles
    return new_image

def frame(image_path):
    """builds a frame around the image

    :param image_path: the original image
    :return: the framed image
    """
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    dimension = 25 #this is the distance to the edge of the picture to where the frame meets the picture

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

            #creates the frame
            if col <= dimension or col >= width - dimension or row <= dimension or row >= height - dimension:
                new_image.putpixel((col, row), (0, 0, 0))
            else:
                new_image.putpixel((col, row), (r, g, b))

    return new_image

def copies(image_path):
    """takes an image and creates smaller altered copies stacked together

    :param image_path: the original image
    :return: the altered image
    """
    img = Image.open(str(image_path))
    width, height = img.size

    #used for greyscale
    avg = 0

    #altered values to create smaller versions
    width = width//2
    height = height//2
    img = img.resize((width, height))

    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (2*width, 2*height), "blue")

    #top left picture
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt

            new_image.putpixel((col, row), (r, g, b))
    #top right picture
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            #these are random values that create a nice image
            r = red_amt + 100
            g = green_amt - 55
            b = blue_amt - 135

            new_image.putpixel((col + width, row), (r, g, b))

    #bottom left picture
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt
            g = green_amt
            b = blue_amt
            avg = (r + g + b) // 3  # calculation to get the average value

            new_image.putpixel((col, row + height), (avg, avg, avg))
    #bottom right picture
    for col in range(width):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r = red_amt + random.randint(-128, 128) #random number
            g = green_amt + random.randint(-128, 128) #random number
            b = blue_amt + random.randint(-128, 128) #random number

            #it takes the origional length and then substracts
            # the column - 1 in order to get pixel to the opposite side
            new_image.putpixel((width - col - 1 + width, row + height), (r, g, b))
    return new_image

def sepia(image_path):
    """gives a picture a sepia tone

    :param image_path: the original image
    :return: the altered image
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

            #formula for the sepia tone
            newR = int(r*.393 + g*.796 + b*.189)
            newG = int(r*.349 + g*.686 + b*.168)
            newB = int(r*.272 + g*.534 + b*.131)

            new_image.putpixel((col, row), (newR, newG, newB))

    return new_image

def motion_blur(image_path): #this is the advanced function
    img = Image.open(str(image_path))
    rgb = img.convert('RGB')

    width = rgb.size[0]
    height = rgb.size[1]

    new_image = Image.new("RGBA", (width-4, height), "blue")
    for col in range(width - 4):
        for row in range(height):
            current_pixel = img.getpixel((col, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r_left = red_amt
            g_left = green_amt
            b_left = blue_amt

            # this is to the right of the previous pixel
            current_pixel = img.getpixel((col + 1, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r_mid = red_amt
            g_mid = green_amt
            b_mid = blue_amt

            # this is to the right of the previous pixel
            current_pixel = img.getpixel((col + 2, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            r_right = red_amt
            g_right = green_amt
            b_right = blue_amt

            # this is to the right of the previous pixel
            current_pixel = img.getpixel((col + 3, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            #the p at the end stands for prime
            r_rightp = red_amt
            g_rightp = green_amt
            b_rightp = blue_amt

            # this is to the right of the previous pixel
            current_pixel = img.getpixel((col + 4, row))

            red_amt = current_pixel[0]
            green_amt = current_pixel[1]
            blue_amt = current_pixel[2]

            #the two ps at the end stands for double prime
            r_rightpp = red_amt
            g_rightpp = green_amt
            b_rightpp = blue_amt

            #this average for each RGB color helps create the motion blur effect
            r_avg = (r_left + r_right + r_mid + r_rightp + r_rightpp) // 5
            g_avg = (g_left + g_right + g_mid + g_rightp + g_rightpp) // 5
            b_avg = (b_left + b_right + b_mid + b_rightp + b_rightpp) // 5

            new_image.putpixel((col, row), (r_avg, g_avg, b_avg))
    return new_image



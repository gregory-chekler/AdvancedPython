from PIL import Image
import random

width = int(input("Enter width: "))
height = int(input("Enter height: "))


img = Image.open('images/genshin.jpg')

rgb = img.convert('RGB')

w = rgb.size[0]
h = rgb.size[1]

new_image = Image.new("RGBA", (width, height), "blue" )
for col in range(width):
    for row in range(height):
        current_pixel = img.getpixel((col, row))

        red_amt = random.randint(1, 255)
        green_amt = random.randint(1, 255)
        blue_amt = random.randint(1, 255)

        r = red_amt
        g = green_amt
        b = blue_amt

        new_image.putpixel((col, row), (r, g, b))

create = Image.new("RGBA", (1920, 1080), "blue" )
for col in range(1920):
    for row in range(1080):
        current_pixel = img.getpixel((col, row))

        red_amt = 0
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))

for col in range(400, 1000):
    for row in range(900,1000):
        current_pixel = img.getpixel((col, row))

        red_amt = 255
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))

for col in range(400, 500):
    for row in range(400,1000):
        current_pixel = img.getpixel((col, row))

        red_amt = 255
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))

for col in range(400, 1000):
    for row in range(300,400):
        current_pixel = img.getpixel((col, row))

        red_amt = 255
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))

for col in range(900, 1000):
    for row in range(700,1000):
        current_pixel = img.getpixel((col, row))

        red_amt = 255
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))
for col in range(600, 1000):
    for row in range(600, 700):
        current_pixel = img.getpixel((col, row))

        red_amt = 255
        green_amt = 0
        blue_amt = 0

        r = red_amt
        g = green_amt
        b = blue_amt

        create.putpixel((col, row), (r, g, b))

new_image.show()
create.show()


# for col in range(width):
#     for row in range(height):
#         img.putpixel((col, row), (random(1, 255), random(1, 255), random(1, 255)))
# #new_image = not Image.new("RGBA", (width, height), "Red")
#
# img.show()
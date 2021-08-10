from PIL import Image

img = Image.open('images/genshin.jpg')
rgb = img.convert('RGB')
w = rgb.size[0]
h = rgb.size[1]
red1 = 0
blue1 = 0
green1 = 0
red2 = 0
blue2 = 0
green2 = 0

create = Image.new("RGBA", (1920, 1080), "blue" )
for col in range(w):
    for row in range(1, h//2):
        current_pixel = img.getpixel((col, row))

        red_amt = current_pixel[0]
        green_amt = current_pixel[2]
        blue_amt = current_pixel[2]

        red1 += red_amt
        green1 += green_amt
        blue1 += blue_amt

red1 = int(red1/(w*h/2))
green1 = int(green1/(w*h/2))
blue1 = int(blue1/(w*h/2))

for col in range(w):
    for row in range(h//2, h):
        current_pixel = img.getpixel((col, row))

        red_amt2 = current_pixel[0]
        green_amt2 = current_pixel[2]
        blue_amt2 = current_pixel[2]

        red2 += red_amt2
        green2 += green_amt2
        blue2 += blue_amt2

red2 = int(red2/(w*h/2))
green2 = int(green2/(w*h/2))
blue2 = int(blue2/(w*h/2))

new_image = Image.new("RGBA", (1920, 1080), "blue" )
for col in range(w):
    for row in range(1, h//2):
        current_pixel = img.getpixel((col, row))

        new_image.putpixel((col, row), (red1, green1, blue1))

for col in range(w):
    for row in range(h//2, h):
        current_pixel = img.getpixel((col, row))

        new_image.putpixel((col, row), (red2, green2, blue2))

new_image.show()
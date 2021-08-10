from PIL import Image

brightest = 'none'
best = 0
img = Image.open('images/genshin.jpg')
rgb = img.convert('RGB')
w = rgb.size[0]
h = rgb.size[1]
first = 0
red1 = 0
blue1 = 0
green1 = 0

img2 = Image.open('images/Slovakia.jpg')
rgb2 = img2.convert('RGB')
w2 = rgb2.size[0]
h2 = rgb2.size[1]
second = 0
red2 = 0
blue2 = 0
green2 = 0

img3 = Image.open('images/sunface.jpg')
rgb3 = img3.convert('RGB')
w3 = rgb3.size[0]
h3 = rgb3.size[1]
third = 0
red3 = 0
blue3 = 0
green3 = 0

img4 = Image.open('images/Basket.jpg')
rgb4 = img4.convert('RGB')
w4 = rgb4.size[0]
h4 = rgb4.size[1]
fourth = 0
red4 = 0
blue4 = 0
green4 = 0

for col in range(w):
    for row in range(h):
        current_pixel = img.getpixel((col, row))

        red_amt = current_pixel[0]
        green_amt = current_pixel[2]
        blue_amt = current_pixel[2]

        first = first + red_amt + green_amt + blue_amt
        red1 += red_amt
        green1 += green_amt
        blue1 += blue_amt

if red1 > green1 and red1 > blue1:
    print("In first image, red is the strongest")
elif green1 > red1 and green1 > blue1:
    print("In first image, green is the strongest")
else:
    print("In first image, blue is the strongest")

first = first/(w*h)

for col in range(w2):
    for row in range(h2):
        current_pixel = img2.getpixel((col, row))

        red_amt = current_pixel[0]
        green_amt = current_pixel[2]
        blue_amt = current_pixel[2]

        red2 += red_amt
        green2 += green_amt
        blue2 += blue_amt

        second = second + red_amt + green_amt + blue_amt

if red2 > green2 and red2 > blue2:
    print("In second image, red is the strongest")
elif green2 > red2 and green2 > blue2:
    print("In second image, green is the strongest")
else:
    print("In second image, blue is the strongest")

second = second/(w2*h2)

for col in range(w3):
    for row in range(h3):
        current_pixel = img3.getpixel((col, row))

        red_amt = current_pixel[0]
        green_amt = current_pixel[2]
        blue_amt = current_pixel[2]

        red3 += red_amt
        green3 += green_amt
        blue3 += blue_amt

        third = third + red_amt + green_amt + blue_amt

if red3 > green3 and red3 > blue3:
    print("In third image, red is the strongest")
elif green3 > red3 and green3 > blue3:
    print("In third image, green is the strongest")
else:
    print("In third image, blue is the strongest")

third = third/(w3*h3)

for col in range(w4):
    for row in range(h4):
        current_pixel = img4.getpixel((col, row))

        red_amt = current_pixel[0]
        green_amt = current_pixel[2]
        blue_amt = current_pixel[2]

        red4 += red_amt
        green4 += green_amt
        blue4 += blue_amt

        fourth = fourth + red_amt + green_amt + blue_amt

if red4 > green4 and red4 > blue4:
    print("In fourth image, red is the strongest")
elif green4 > red4 and green4 > blue4:
    print("In fourth image, green is the strongest")
else:
    print("In fourth image, blue is the strongest")

fourth = fourth/(w4*h4)

if first > second and first > third and first > fourth:
    print("First image is brightest")
elif second > first and second > third and second > fourth:
    print("Second image is brightest")
elif third > second and third > first and third > fourth:
    print("Third image is brightest")
else:
    print("Fourth image is brightest")

if first < second and first < third and first < fourth:
    print("First image is darkest")
elif second < first and second < third and second < fourth:
    print("Second image is darkest")
elif third < second and third < first and third < fourth:
    print("Third image is darkest")
else:
    print("Fourth image is darkest")



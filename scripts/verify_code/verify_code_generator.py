from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# random character
def rndChar():
    return chr(random.randint(65, 90))


# random color 1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# random color 2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# resulution:240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# create Font object
font = ImageFont.truetype('C:\Windows\Fonts\SourceCodePro-Regular.otf', 36)

# create Draw object
draw = ImageDraw.Draw(image)

# fill pixels
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# output text
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# blur
image = image.filter(ImageFilter.BLUR)

# save
image.save('code.jpg', 'jpeg')

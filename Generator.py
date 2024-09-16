

from PIL import Image, ImageDraw, ImageFont
import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|(){}[]?-_+~<>i!1I;:,\"^`'.'`"[::-1]
chars = "#@&%WO/|!;:-. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

ScaleFactor = 0.5

OneCharWidth = 8;
OneCharHeight = 18;

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

im= Image.open("Sample.jpg")

width, height = im.size
im = im.resize((int(ScaleFactor*width), int(ScaleFactor*height*(OneCharWidth/OneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()


print(width, height)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j,i]
        print(r)
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))

    text_file.write('\n')

im.save("output.png")

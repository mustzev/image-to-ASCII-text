from PIL import Image

im = Image.open("girl.png")
im = im.resize((int(im.width / 2), int(im.height / 4)))

width, height = im.size

ASCII_char = ['#', '$', '@']
ASCII_text = ''

max_brightness = 0
min_brightness = 255


for w in range(width):
    for h in range(height):
        rgb = im.getpixel((w, h))
        brightness = (rgb[0] + rgb[1] + rgb[2])/3

        if brightness > max_brightness:
            max_brightness = brightness

        if brightness < min_brightness:
            min_brightness = brightness


for h in range(height):
    for w in range(width):
        rgb1 = im.getpixel((w, h))
        brightness1 = (rgb1[0] + rgb1[1] + rgb1[2])/3

        if brightness1 < min_brightness + (max_brightness - min_brightness)/3*1:
            ASCII_text += ASCII_char[0]
        elif brightness1 < min_brightness + (max_brightness - min_brightness)/3*2:
            ASCII_text += ASCII_char[1]
        else:
            ASCII_text += ASCII_char[2]
        
        if w == width-1:
            ASCII_text += '\n'

print(ASCII_text)



from PIL import Image

# Replace "girl.png" with your image within the directory.
im = Image.open("girl.png")
im = im.resize((int(im.width / 2), int(im.height / 4)))

width, height = im.size

# ASCII text is gonna be created using #, $, and @.
# You can change these to any symbols you want for customization.
ASCII_char = ['#', '$', '@']
ASCII_text = ''

max_brightness = 0
min_brightness = 255

# Here we are finding the brigthest, and the darkest pixel's brightness in the given image.
# So later we can assign the each ASCII symbols to a pixel depending on it's relative brightness.
for w in range(width):
    for h in range(height):
        rgb = im.getpixel((w, h))
        brightness = (rgb[0] + rgb[1] + rgb[2])/3

        if brightness > max_brightness:
            max_brightness = brightness

        if brightness < min_brightness:
            min_brightness = brightness

# Here comes the creating ASCII text part.
# If the given pixel is darker lets assign the first ASCII symbol. And so on ...
# Also adding a new line to the ASCII text everytime the loop is at the end of a width.
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

# Printing the ASCII text to the terminal.
print(ASCII_text)



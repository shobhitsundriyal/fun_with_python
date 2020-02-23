from PIL import Image
import math
import numpy as np

def getAverageL(image):
    
    # convert image to numpy array
    im = np.array(image)
    # get the dimensions
    w,h = im.shape
    # get the average
    return np.average(im.reshape(w*h))


def covertImageToAscii(fileName, cols, scale, moreLevels):
    
    grayscale1 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`". ' #70 Level
    grayscale2 = "@%#*+=-:. " #10 levels
    
    image = Image.open(fileName).convert('L')
    # store the image dimensions
    width, height = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (width, height))
    
    w = width/cols
    h = w/scale
    # compute number of rows to use in the final grid
    rows = int(height/h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > width or rows > height:
        print("Image too small for specified cols!")
        exit(0)

    # an ASCII image is a list of character strings
    aimg = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct the last tile
        if j == rows-1:
            y2 = height
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
            # correct the last tile
            if i == cols-1:
                x2 = width
            # crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # get the average luminance
            avg = int(getAverageL(img))
            # look up the ASCII character for grayscale value (avg)
            if moreLevels:
                gsval = grayscale1[int((avg*69)/255)]
            else:
                gsval = grayscale2[int((avg*9)/255)]
            # append the ASCII character to the string
            aimg[j] += gsval

    return aimg
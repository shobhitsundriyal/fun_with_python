import sys, random, argparse
import math
from convert import covertImageToAscii


def main():
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    #parser.add_argument('--display', dest='display', required=False)
    #parser.add_argument('--morelevels', dest='moreLevels', action='store_true')

    args = parser.parse_args()
    print('-------------------')
    imgFile = args.imgFile
    
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
    # set scale default as 0.43, which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('Just a sec..')
    
    aimg = covertImageToAscii(imgFile, cols, scale, True)
    print(aimg)
    
    f = open(outFile, 'w')
    for row in aimg:
        f.write(row + '\n')
    f.close()
    print("ASCII art written to %s" % outFile)


if __name__ == '__main()__':
    main()


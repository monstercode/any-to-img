from PIL import Image
import binascii
from math import ceil

from os import listdir
from os.path import isfile, join
from optparse import OptionParser

img_types = ['png', 'bmp', 'jpeg']

# Parse the OptionParser
parser = OptionParser(usage="usage: %prog [options] SOURCE DEST \n\nTransforms any file to a square image")
parser.add_option("-t", "--type", dest="img_type", metavar="TYPE", default=img_types[0],
                  help="Image type. Possible values: " + ', '.join(img_types) +' [Default: %default]')

(options, args) = parser.parse_args()
if len(args) < 2:
	parser.print_help()
	quit()

src_file = args[0]
dst_file = args[1]
img_type = options.img_type


# Generate Image from Raw binary file
m = open(src_file,'rb') 
data = m.read();
square_side = ceil((len(data)/3.)**(1/2.))
img = Image.new( 'RGB', (square_side,square_side), "black") # Create a new black image

pixels = img.load() # Create the pixel map
data_index = 0
for i in range(0,square_side):    # For every pixel:
    for j in range(0,square_side):
        if data_index < len(data)-3:
            pixels[i,j] = (data[data_index], data[data_index+1], data[data_index+2]) # Set the colour accordingly
            data_index = data_index + 3
        else:
            pixels[i,j] = (0, 0, 0)
        #print('.',end='')

img.save( dst_file, img_type)
print('Saved as '+dst_file)
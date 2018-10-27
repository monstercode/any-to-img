from PIL import Image
from math import ceil
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog SOURCE DEST\n\nTransforms back an image generated with the other script to the original file")
(options, args) = parser.parse_args()
if len(args) < 2:
	parser.print_help()
	quit()

src_file   = args[0]
dst_file   = args[1]

im = Image.open(src_file) # Can be many different formats.
pix = im.load()
newFileBytes = []
for x in range(0,im.size[0]):
	for y in range(0,im.size[1]):
		rgb = pix[x,y]
		newFileBytes.append(rgb[0])
		newFileBytes.append(rgb[1])
		newFileBytes.append(rgb[2])

newFileByteArray = bytearray(newFileBytes)
newFile = open(dst_file,'wb') 
newFile.write(newFileByteArray)	

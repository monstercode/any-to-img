# mp3toimg
Transform any file an to image and vice versa


Install Pillow

```bash
sudo pip3 install pillow
```

Usage:

```bash
python3 anytoimg.py myfile.mp3 myfile.transformed.png
python3 imgtoany.py myfile.transformed.png myfile.transformed-back.mp3
```
 
This script takes a file and generates an image taking the raw binary data as bytes to generate the RGB pixels sequence.
It cant transforms it back with the imgtoany.py script. The image is padded with black pixels, so it may add some garbage to the end of the file. 

The idea of the project is to show that files are just bytes and can be interpreted as you want.
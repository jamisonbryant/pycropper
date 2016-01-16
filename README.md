# PyCropper

**THIS IS A PYTHON 3.X SCRIPT. IT WILL NOT WORK ON PYTHON 2.X. YOU HAVE BEEN WARNED.**

PyCropper is a smart image cropping script that I wrote to help me with a project at work. This task involved cropping
images, lots and LOTS of them. Originally I was cropping these images in batches using IrfanView, but since IrfanView
doesn't have a fuzzy-select utility I was selecting the area to crop by hand for each batch of images. As a result, I
found that some images were being cropped rather poorly. Some had too much padding, some had too little. The fact was, 
my eyes weren't good enough for me to select the area to crop accurately. So I wrote a Python script to do it for me!

## How it Works
PyCropper works by pixel sampling and comparison. It determines the color of the padding (the area to be cropped) and 
then searches for pixels that are notably different in color from the background color (call these target pixels), 
starting from the edges and working its way inward. As soon as it encounters a target pixel, it stores the pixel's x-
or y-value (depending on which direction it is scanning from) and determines that row/column of pixels to be an edge.
When all four edges are found, the image is cropped to those dimensions and saved into an output directory!

## Installation
PyCropper itself has no installation requirements, other than being cloned/downloaded to your computer. However, it
has the following dependencies that must be installed prior to running:

* Python 3.x
* [Pillow](https://python-pillow.github.io) (install with `pip install pillow`)

**NOTE:** Pillow CANNOT co-exist with PIL (another Python image processing library). You must uninstall PIL before 
installing Pillow. For more info, see the [Pillow docs](http://pillow.readthedocs.org/en/3.0.x/installation.html).

## Usage
To use PyCropper, simply `cd` into its directory and run it with `./cropper.py`. Make sure it's executable first.

**NOTE:** PyCropper was developed on and intended for use on Windows. It's 99% cross-platform, but there is a line of
code or two that will only work on Windows. These lines are primarily used by me only for debugging purposes, and thus
are commented out by default. If you go fiddling around with the source code and uncomment those lines on a non-Windows 
platform, the script will crash. So, don't do that.

## Examples
There is a directory called `examples` that contains some sample images which PyCropper can be run against to allow you 
to get a feel for how it works. To use them, rename `examples` to `img` (or change `INPUT_DIR` to `examples`) and run 
the script.

## FAQs
### What types of images does PyCropper work on?
Any image file with the extension JPEG, JPG, or PNG. Adding support for other images types is probably pretty easy, but 
I didn't need to support any other image types, so I didn't implement them. If you need them, fork the repo or message
me and I'll see what I can do.

### Does PyCropper alter the original image?
No. The original image is stored into memory, and *that* image is cropped and saved into the output directory.

### PyCropper is cropping too much/too little of my image!
There's a constant in the script called `TOLERANCE`. Basically, it defines how different a pixel has to be from the 
background color in order to be considered a target pixel. Increase or decrease its value to increase or decrease the 
size of the cropped area, respectively.

### How do I change the input/output directories?
There are constants called `INPUT_DIR` and `OUTPUT_DIR` in the script. Change them to suit your needs. FYI, the output
directory doesn't have to be present in order to run the script. If it is not there, the script will create it. 

If you're using git and you change the input/output dirs, don't forget to update the `.gitignore` file!

## Credits
**Jamison Bryant**, Principal Developer

Implemented using [Pillow, the friendly PIL fork](https://python-pillow.github.io)

## License
The MIT License (MIT)
Copyright (c) 2015 Jamison Bryant

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




 
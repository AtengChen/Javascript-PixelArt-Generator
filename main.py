"""
// Please don't click inside here, please: {
var Pixels = %s;

var color_map = %s;
//}, because it's very messy

var Art = function (x, y){
    for (var i = 0; i < Pixels.length; i++) {
        var arrayColors = Pixels[i];
        for (var c = 0; c < Pixels[i].length; c += 1){
            noStroke();
            var w = %s;
            var h = %s;
            var px = arrayColors[c];
            var color = [0, 0, 0];
            for (var ch in color_map){
                if (px === ch) {
                    var color = color_map[ch];
                    break;
                }
            }
            fill(color[0], color[1], color[2]);
            rect((c * w) + x, (i * h) + y, w, h);
        }
    }
};
Art(0,0);
"""

from PIL.Image import open as open_im
from pprint import pprint
from json import dumps
from pyperclip import copy
from math import floor

image = open_im(input("Path: "))


if image.height > image.width:
    th = int(input("height: "))
    tw = int(image.width * (th / image.height))
else:
    tw = int(input("width: "))
    th = int(image.height * (tw / image.width))

print(tw, th)
image = image.resize((tw, th))
pixel_w = floor(400 / image.width)
pixel_h = floor(400 / image.height)

dct = {}
mat = []

for y in range(image.height):
    row = ""
    for x in range(image.width):
        char = chr(len(dct))
        row += dct.setdefault(image.getpixel((x, y)), char)
    mat.append(row)

_dct = {}
for k, v in dct.items():
    _dct[v] = list(k)

dct = _dct
del _dct

dct, mat = dumps(dct, indent=4), dumps(mat, indent=4)
script = __doc__ % (mat, dct, pixel_w, pixel_h)
print(script)
copy(script)

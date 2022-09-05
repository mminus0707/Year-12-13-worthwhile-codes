from PIL import Image
import numpy

myarray = [
  [
    [255, 0, 0],
    [255, 0, 0],
    [255, 0, 0]
  ],
  [
    [0, 255, 0],
    [0, 255, 0],
    [0, 255, 0]
  ],
  [
    [0, 0, 255],
    [0, 0, 255],
    [0, 0, 255]
  ]
]


data = numpy.array(myarray, dtype=numpy.uint8)
img = Image.fromarray(data, 'RGB')
img.save('red.png')
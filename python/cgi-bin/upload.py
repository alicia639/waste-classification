#!/usr/bin/python3

from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
      # strip leading path from file name to avoid
          # directory traversal attacks
  fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
  open('/tmp/' + fn, 'wb').write(fileitem.file.read())
  message = 'The file "' + fn + '" was uploaded successfully'
                     
else:
  message = 'No file was uploaded'

from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import efficientnet.tfkeras as efn 
import tensorflow.keras.layers as L
from tensorflow.keras.models import Model



# building the complete model
model = load_model('~/python/cgi-bin/trained_model.h5')

from PIL import Image
import numpy as np
from skimage import transform
import matplotlib.pyplot as plt

def load(filename):
  np_image = Image.open(filename)
  np_image = np.array(np_image).astype('float32')/255
  np_image = transform.resize(np_image, (64, 64, 3))
  np_image = np.expand_dims(np_image, axis=0)
  return np_image


def prediction(result):
    if result == 3:
        prediction = "Cardboard: Goes Into Blue Box"
    elif result == 1:
        prediction = "Glass: Goes Into Blue Box"
    elif result == 5:
        prediction = "Metal: If can, blue box.  Else, bring to depot."
    elif result == 2:
        prediction = "Paper: Goes Into Yellow Bag"
    elif result == 4:
        prediction = "Plastic: Goes Into Blue Box"
    elif result == 6:
        prediction = "Trash: Garbage"
    else:
        prediction = "Error"
    return prediction


def total(filename):
  image = load(filename)
  pred = model.predict(image)
  result = np.argmax(pred, axis=1)
  return prediction(result)
  

print("Content-Type: text/html")
print()
print ("<html><style> body {text-align: center; background: lightblue url('/pawel-czerwinski-RkIsyD_AVvc-unsplash.jpg'); background-size: cover; position: static} p{font-size: 40px; background-color: white} </style><body>")
print("<p>Thank you for uploading a file!</p>")

print("<p>" + message + "</p>")

#new_model.summary()
prediction = total("/tmp/" + fn)
print("<p>"+  prediction + "</p>")



print("</body></html>")

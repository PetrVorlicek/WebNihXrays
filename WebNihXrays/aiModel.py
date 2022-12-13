#Imports
from PIL import Image
from pathlib import Path
import sys
import tensorflow as tf
import numpy as np

folder_path = Path(__file__).parent
model = tf.keras.models.load_model(folder_path.resolve() / 'example_model')
media_folder = folder_path.parent.resolve() / 'media'
size = 300,300

def img_to_arr(name, media_folder = media_folder):
    
    img = Image.open(media_folder / name).resize(size).convert('RGB')
    arr = np.asarray(img)
    print(arr)
    #image to 1D array
    arr = list(map(lambda x: list(map(lambda y: int(sum(y))/765.0, x)), arr))
    return arr




  
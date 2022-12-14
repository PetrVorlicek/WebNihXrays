from PIL import Image
from pathlib import Path
import tensorflow as tf
import numpy as np

SIZE = 300,300

#Folders placement
folder_path = Path(__file__).parent
media_folder = folder_path.parent.resolve() / 'media'

#Load model at server startup
#Tf tries to load GPU, but fails - what to do about it?
model = tf.keras.models.load_model(folder_path.resolve() / 'example_model')

#Model takes 1D array with 300*300=90000 items
def img_to_arr(path, media_folder = media_folder, size = SIZE):
    
    img = Image.open(media_folder / path).resize(size).convert('RGB')

    arr = np.asarray(img)
    #Image to 1D array
    arr = list(map(lambda x: list(map(lambda y: int(sum(y))/765.0, x)), arr))
    return arr

#Take file as argument instead of path
def file_to_arr(file, size = SIZE):

    img = Image.open(file).resize(size).convert('RGB')

    arr = np.asarray(img)
    #Image to 1D array
    arr = list(map(lambda x: list(map(lambda y: int(sum(y))/765.0, x)), arr))
    return arr



  
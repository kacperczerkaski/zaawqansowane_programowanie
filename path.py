import os
from detection import detection


def read_data():

    data_format = [".jpg"]
    path = 'images/'
    for (path, dirs, data) in os.walk(path):
        for img in data:
            if img.endswith(tuple(data_format)):
                print(img)
                image = path + img
                detection(image)

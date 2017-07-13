
'''
Reference: https://www.tensorflow.org/programmers_guide/reading_data

A typical pipeline for reading records from files has the following stages:

    1) The list of filenames
    2) Optional filename shuffling
    3) Optional epoch limit
    4) Filename queue
    5) A Reader for the file format
    6) A decoder for a record read by the reader
    7) Optional preprocessing
    8) Example queue

'''

import json
import numpy as np
import os
import tensorflow as tf

def print_comments_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file) #deserialize to python object
        for comment in data:
            print(comment["commentText"])

if __name__ == '__main__':
    directory = '/home/s4x5/Documents/github/yt-comments-topics'
    file_name = 'comments_5.json'
    file_path = os.path.join(directory, file_name)
    print_comments_from_json(file_path) 


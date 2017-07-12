
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

import tensorflow as tf

filename_queue = tf.train.string_input_producer(["comments.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [[1], [1], [1], [1], [1]]
col1, col2, col3, col4, col5 = tf.decode_csv(
    value, record_defaults=record_defaults)
features = tf.stack([col1, col2, col3, col4])

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(1200):
    # Retrieve a single instance:
    example, label = sess.run([features, col5])

  coord.request_stop()
  coord.join(threads)


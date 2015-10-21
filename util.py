__author__ = 'dennis'

import os, sys
import numpy as np
import PIL.Image as Image


def read_images(path, sz=None):
    c = 0
    X, y = [], []

    for d_name, d_names, filenames in os.walk(path):
        for sub_d_name in d_names:
            pic_path = os.path.join(d_name, sub_d_name)
            for pic_name in os.listdir(pic_path):
                try:
                    im = Image.open(os.path.join(pic_path, pic_name))
                    im = im.convert("L")  # convert to black and white

                    # resize if given
                    if sz is not None:
                        im = im.resize(sz, Image.ANTIALIAS)
                    X.append(np.array(im, dtype=np.uint8))
                    y.append(c)
                except IOError:
                    print "I/O error"
                except:
                    print "Unexpected error:"
                    raise
            c += 1
    return X, y


def stack_as_rows(X):
    if len(X) == 0:
        return np.array([])
    return np.vstack([pic.reshape((1, -1)) for pic in X])


def stack_as_cols(X):
    if len(X) == 0:
        return np.array([])
    return np.hstack([pic.reshape((-1, 1)) for pic in X])


if __name__ == '__main__':

    X, y = read_images('data')
    X_row = stack_as_cols(X)
    print X_row.shape

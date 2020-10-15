#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Generate a text file with names of all images in Content Image folder
'''

__author__ = 'Sneh Sagar'
__copyright__ = None
__credits__ = ['Sneh Sagar']
__license__ = 'GPL'
__version__ = '1.0.1'
__email__ = 'snehsagarajput@gmail.com'
__status__ = 'Production'

import os


def generator():

    # Getting the current work directory (cwd)

    thisdir = os.path.dirname(os.path.realpath(__file__)) \
        + '/Content Images'

    images = []

    # r=root, d=directories, f = files

    for (r, d, f) in os.walk(thisdir):
        for file in f:
            images.append(file)
    images.sort()

    def itemName(item):
        name = ''
        for i in item:
            if i == '.':
                break
            name += i
        return name

    f = open('style_image_list.txt', 'w')

    for item in images:
        f.write(itemName(item))
        f.write('\n')

    f.close()



			

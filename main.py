#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Flask Server
'''

__author__ = 'Sneh Sagar'
__copyright__ = None
__credits__ = ['Sneh Sagar']
__license__ = 'GPL'
__version__ = '1.0.1'
__email__ = 'snehsagarajput@gmail.com'
__status__ = 'Production'





import time
from flask import Flask, request, render_template, send_from_directory, \
    jsonify, send_file, make_response
import os
import sys
from PIL import ImageEnhance
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import sys
from server import run_with_ngrok
from model import load_img, tensor_to_image, model

DEBUG_PRINT = False or sys.argv[1] == 'True' or sys.argv[1] == True
BUILD_PATH = '/content/build/build/'  # end with /
UPLOAD_DIRECTORY = '/content/sample_data/'
repo = '/content/build/'

app = Flask(__name__, static_folder=BUILD_PATH + 'static/',
            template_folder=BUILD_PATH)

run_with_ngrok(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def getImages():
    req = request.form
    file1 = request.files['content']
    file1.save(os.path.join(UPLOAD_DIRECTORY, 'content.jpg'))
    if req['type'] == 'upload':
        file2 = request.files['style']
        file2.save(os.path.join(UPLOAD_DIRECTORY, 'style.jpg'))
        file2 = os.path.join(UPLOAD_DIRECTORY, 'style.jpg')
    else:
        file2 = os.path.join(repo + 'Content Images',
                             req['styleDropdown'])
    try:
        if DEBUG_PRINT:
            print("In try block....")
        results = model(os.path.join(UPLOAD_DIRECTORY, 'content.jpg'),
                        file2)
        results.save(os.path.join(UPLOAD_DIRECTORY, 'styled.jpg'))
        if DEBUG_PRINT:
            print ('Success....Sending response')
        return send_from_directory(UPLOAD_DIRECTORY, 'styled.jpg',
                                   as_attachment=False)
    except Exception as e:
        if DEBUG_PRINT:
            print ("\n\nIn except block....\n\nCheck for following error:")
            print (e, file=sys.stderr)
        response = make_response('Some Error', 400)
        response.mimetype = 'text/plain'
        return response


@app.route('/output/<junk>')
def download_file(junk):
    mode = False
    if junk[:4] == 'True':
        mode = True
    return send_from_directory(UPLOAD_DIRECTORY, 'styled.jpg',
                               as_attachment=mode)


@app.route('/getStyleImagesList')
def imageList():
    f = open('style_image_list.txt', 'r')
    imagesList = f.readlines()
    imagesList = [name[:-1] for name in imagesList]
    f.close()
    if DEBUG_PRINT:
        print imagesList
    return jsonify(data=imagesList)

app.run()

			

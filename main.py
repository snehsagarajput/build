import time
from flask import Flask, request, render_template, send_from_directory, redirect, send_file, make_response
import os, sys
from PIL import ImageEnhance
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import sys
from server import run_with_ngrok
from model import load_img, tensor_to_image, model


DEBUG_PRINT = False or sys.argv[1]=="True" or sys.argv[1]==True
BUILD_PATH = "/content/build/build/"  #end with /
UPLOAD_DIRECTORY = "/content/"


app = Flask(__name__, static_folder= BUILD_PATH+'static/',
            template_folder=BUILD_PATH)

run_with_ngrok(app)

@ app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def getImages():
    file1 = request.files['content']
    file2 = request.files['style']
    file1.save(os.path.join(UPLOAD_DIRECTORY, "content.jpg"))
    file2.save(os.path.join(UPLOAD_DIRECTORY, "style.jpg"))
    try:
        if DEBUG_PRINT:
            print("\n\nIn try block....\n\n")
        results = model(os.path.join(UPLOAD_DIRECTORY, "content.jpg"),
                        os.path.join(UPLOAD_DIRECTORY, "style.jpg"), DEBUG_PRINT)
        results.save(os.path.join(UPLOAD_DIRECTORY, "styled.jpg"))
        if DEBUG_PRINT:
            print("Success....Sending response")
        return send_from_directory(UPLOAD_DIRECTORY,
                                   "styled.jpg", as_attachment=False)
    except Exception as e:
        if DEBUG_PRINT:
            print("\n\nIn except block....\n\nCheck for following error:\n\n")
            print(e, file = sys.stderr)
            print("\n\n")
        response = make_response("Some Error", 404)
        response.mimetype = "text/plain"
        return response

@app.route('/output/<junk>')
def download_file(junk):
    mode = False
    if junk[:4] == "True":
        mode = True
    return send_from_directory(UPLOAD_DIRECTORY,
                               "styled.jpg", as_attachment=mode)
    
app.run()
			

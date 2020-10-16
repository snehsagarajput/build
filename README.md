# <img src="https://i.ibb.co/FBCrvVP/logo-jpg.png" alt="Logo of the project" align="right">

# Neural Style Transfer WebApp 
![last-commit](https://img.shields.io/github/last-commit/snehsagarajput/nst-app) ![repo-size](https://img.shields.io/github/repo-size/snehsagarajput/nst-app) ![lang-count](https://img.shields.io/github/languages/count/snehsagarajput/nst-app) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> WebApp for Tensorflow based Neural Style Transfer

Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.


# <img src="https://i.ibb.co/GCNKxCy/example.jpg" alt="Example" align="right">


## Getting started

[Google Colab](https://colab.research.google.com/) provides the virtual environment to run a Flask based Web-App which is tunneled to Internet with the help of [Ngrok](https://ngrok.com/). **A Bare Minimum Setup :wink:**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://bit.ly/nst-tf)

## Developing

### Built With
* [ReactJS](https://reactjs.org/)
* [Tensorflow 2.0](https://www.tensorflow.org/overview/) 
* [Open-CV](https://opencv.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Ngrok](https://ngrok.com/)

### Setting up Dev

Required setup is provided in the Colab Notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://bit.ly/nst-tf) but for developing the project further follow the commands in colab environment:

```shell
!git clone https://github.com/snehsagarajput/nst-app # Clone the Repo
!python /content/nst-app/environment_setup.py # List the missing Python libraries from requirements.txt if any
!pip install -r /content/create_req_file.txt # Install the missing libraries
```

### Deploying / Publishing
To host the Web-App on Internet through tunneling from LocalHost :

```shell
Debug = False # Print the logs = Off 
!python /content/nst-app/main.py {Debug} # Deploying the Web-App
```

It will print the ngrok.io extended URL for the Web-App.

## Web-App Interface

# <img src="https://i.ibb.co/Qf2NhR7/Interface.png" alt="WebApp Interface" align="right">

## Licensing
Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Sneh Sagar - [_snehsagarajput@gmail.com_](mailto:snehsagarajput@gmail.com)

Project Link: [https://github.com/snehsagarajput/nst-app](https://github.com/snehsagarajput/nst-app)

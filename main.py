from styleTransfer import fastStyleTransfer

import fastStyleTransfer.fastStyleTransfer.neural_style.transferFunction.StyleClass as StyleClass
from styleTransfer.fastStyleTransfer.fastStyleTransfer.neural_style import utils

import os
import sys
import torch
from torchvision import transforms


cwd = os.getcwd()

images_dir = cwd+'/styleTransfer/fastStyleTransfer/neural_style/images'
models_dir = cwd+'/styleTransfer/fastStyleTransfer/neural_style/saved_models'
sys.path.append(images_dir)
sys.path.append(models_dir)


modelpath = models_dir+'candy.pth'
styleClass = StyleClass(modelpath)

imagepath = images_dir+'/content-images/amber.jpg'
image = utils.load_image(imagepath)

transform = transforms.ToTensor()
tensor_image = transform(image)

output = styleClass.stylize(tensor_image)
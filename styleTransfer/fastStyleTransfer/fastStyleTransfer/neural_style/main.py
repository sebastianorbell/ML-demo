"""
Name : main.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 14:40
Desc:
"""

import os
import sys

import numpy as np
import torch
from torchvision import transforms

from transferFunction import StyleClass
from utils import load_image
from openCV import online

cwd = os.getcwd()

images_dir = cwd+'/images/'
models_dir = cwd+'/saved_models/'
sys.path.append(images_dir)
sys.path.append(models_dir)

styles = ['candy.pth', 'mosaic.pth', 'rain_princess.pth', 'udnie.pth']

modelpath = models_dir+styles[2]

styleClass = StyleClass(modelpath)

function = lambda x: np.moveaxis(styleClass.stylize(torch.from_numpy(np.moveaxis(x, -1, 0).astype(np.float32))).numpy(),0,-1)

online(function)
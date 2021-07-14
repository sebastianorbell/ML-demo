"""
Name : transferFunction.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 12:23
Desc:
"""

import argparse
import os
import sys
import time
import re

import torch
from torchvision import transforms

# from fastStyleTransfer.neural_style import utils
# from fastStyleTransfer.neural_style import TransformerNet
# from fastStyleTransfer.neural_style import Vgg16

import utils
from transformer_net import TransformerNet
from vgg import Vgg16

import sys
import os

cwd = os.getcwd()
sys.path.append(cwd+'/images')
sys.path.append(cwd+'/saved_models')

class StyleClass():
    def __init__(self, model, scale=None, device=torch.device("cpu")):
        self.model = model
        self.scale = scale
        self.content_transform = transforms.Compose([
            transforms.Lambda(lambda x: x.mul(255))
        ])
        self.device = device

    def stylize(self, image):
        # content_image = utils.resize_image(image, scale=self.scale)
        # content_image = self.content_transform(content_image)
        content_image = image
        content_image = content_image.unsqueeze(0).to(self.device)
        # print('content image', content_image)
        with torch.no_grad():
            style_model = TransformerNet()
            state_dict = torch.load(self.model)
            # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
            for k in list(state_dict.keys()):
                if re.search(r'in\d+\.running_(mean|var)$', k):
                    del state_dict[k]
            style_model.load_state_dict(state_dict)
            style_model.to(self.device)
            output = style_model(content_image).cpu()
        return output[0]
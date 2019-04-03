# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 16:16
# @Author  : dzzxjl@126.com

from __future__ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random

import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
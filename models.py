import mido
import numpy as np
import torch
import torch.nn as nn
from tqdm import tqdm
from typing import Optional, Union, Tuple, List, Sequence, Iterable
import math
import matplitlib.pyplot as plt

class MIDItoTab(nn.Module):
    
    def __init__(self, )
import copy
import os
import time

import numpy as np
import torch

from torch.utils.data import DataLoader
from tqdm import tqdm

from src.utils.datasets import get_dataset


class Tracker(object):
    def __init__(self, cfg, args, slam
                 ):
        
        self.idx = slam.idx
        self.nice = slam.nice
        self.output = slam.output
        self.verbose = slam.verbose
        self.device = cfg['tracking']['device']

        self.frame_reader = get_dataset(
            cfg, args, self.scale, device=self.device)
        self.n_img = len(self.frame_reader)
        self.frame_loader = DataLoader(
            self.frame_reader, batch_size=1, shuffle=False, num_workers=1)



    def run(self):
        device = self.device
        self.c = {}
        if self.verbose:
            pbar = self.frame_loader
        else:
            pbar = tqdm(self.frame_loader)

        
        
        






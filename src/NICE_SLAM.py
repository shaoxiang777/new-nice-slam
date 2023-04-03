import os
import time

import numpy as np
import torch
import torch.multiprocessing
import torch.multiprocessing as mp

from src import config
from src.Mapper import Mapper
from src.Tracker import Tracker




class NICE_SLAM():
    '''
    NICE_SLAM main class.
    Mainly allocate shared resouces, and dispatch mapping and tracking process.
    '''

    def __init__(self, cfg, args):

        self.cfg = cfg
        self.args = args
        self.nice = args.nice

        self.verbose = cfg['verbose']
        self.dataset = cfg['dataset']

        self.mapper = Mapper(cfg, args, self, coarse_mapper=False)
        if self.coarse:
            self.coarse_mapper = Mapper(cfg, args, self, coarse_mapper=True)


        self.mapping_first_frame = torch.zeros((1)).int()

        self.tracker = Tracker(cfg, args, self)

        


    def print_output_desc(self):

        pass

    def update_cam(self):
        """
        Update the camera intrinsics according to pre-processing config, 
        such as resize or edge crop.
        """

        pass

    def load_bound_():

        pass


    def load_pretrain(self, cfg):

        pass

    def grid_init(self, cfg):

        pass

    def tracking(self, rank):
        '''
        Tracking Thread.

        Args:
            rank (int): Thread ID.
        '''

        # should wait until the mapping of first frame is finished
        while (1):
            if self.mapping_first_frame[0] == 1:
                break
            time.sleep(1)
        
        self.tracker.run()

    def mapping(self, rank):
        '''
        Mapping Thread. (updates middle, fine, and color level)

        Args:
            rank (int): Thread ID.
        '''

        self.mapper.run()

    def coarse_mapping(self, rank):
        '''
        Coarse mapping Thread. (update coarse level)

        Args:
            rank (int): Thread ID.
        '''

        self.coarse_mapper.run()

    def run(self):
        '''
        Dispatch Threads.
        '''

        processes = []
        for rank in range(3):
            if rank == 0:
                p = mp.Process(target=self.tracking, args=(rank, ))
            elif rank == 1:
                p = mp.Process(target=self.mapping, args=(rank, ))
            elif rank == 2:
                if self.coarse:
                    p = mp.Process(target=self.coarse_mapping, args=(rank, ))
                else:
                    continue
            p.start()  # make the process run, if now there is another process coming, they can run parallel!
            processes.append(p)
        for p in processes:
            p.join()   # join this process in main function. Make sure, after runing this function, can continue. Otherwise, all subfunctions(child function) and main function(parent function) will run parallel.

          
# This part is required by torch.multiprocessing
if __name__ == '__main__':
    pass

    

    

    
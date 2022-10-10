# -*- coding: utf-8 -*-
# Copyright © 2021 Li Auto. All rights reserved.

"""Obstacle data structure"""

import json
from enum import Enum
import math
import logging
from typing import Dict, List, Tuple

import numpy as np
import re 

class ObstacleType(Enum):
    VISION = 1
    LIDAR = 2
    RADAR = 3
    DEFAULT = 4


class PredictObstacle(object):
    """Obstacle class
    """

    def __init__(self, obstacle_info):
        """Init

        Args:
            obstacle_info: obstacle basic info from raw data
            mode: insert obstacle mode, eg: predicted, ground_truth
        """
        logging.info(obstacle_info)

        self.id_info: int = obstacle_info['id']
        self.id: int = None
        self.id_time = None 
        self.timestamp: int = int(float(obstacle_info["stamp"])*1000)
        self.label: float = obstacle_info["label"]
        self.cutin_adc: int = None
        self.position_x: float = obstacle_info["pose"]["position"]["x"]
        self.position_y: float = obstacle_info["pose"]["position"]["y"]
        self.obstacle_type: int = obstacle_info['type']
        
    
    def get_id_time(self):
        if len(self.id_info) !=  0:
            id , id_time = self.id_info.rsplit("_",1)[0],self.id_info.rsplit("_",1)[1]
            if  id_time in ['0s', '1s' , '2s' , '3s']:
                self.id , self.id_time = id , id_time
                # return 

    def get_cutin_adc(self):
        # cutin_flag = self.label.split(' ')
        cutin_flag = re.split(r"[ ]+", self.label)
        if 'is_cutin_adc:0' in cutin_flag :
            self.cutin_adc = 0 
        elif 'is_cutin_adc:1' in cutin_flag:
            self.cutin_adc = 1


class SyncPredictObstacle(object):     

    def __init__(self, obs_number):
        """Init

        Args:
            obstacle_info: obstacle basic info from raw data
            mode: insert obstacle mode, eg: predicted, ground_truth
        """ 
        self.obs_number = obs_number
        self.sync_pred_obs_zero = None
        self.sync_pred_obs_one = None
        self.sync_pred_obs_two = None
        self.sync_pred_obs_three = None
        self.sync_timestamp = None 
        self.sync_id = None

    def add_predict_obs(self,predictobs):
        if predictobs.id_time =='0s':
            self.sync_pred_obs_zero = predictobs
        if predictobs.id_time =='1s':
            self.sync_pred_obs_one = predictobs
        if predictobs.id_time =='2s':
            self.sync_pred_obs_two = predictobs
        if predictobs.id_time =='3s':
            self.sync_pred_obs_three = predictobs

    def get_sync_timestamp(self):
        if self.sync_pred_obs_zero.timestamp == self.sync_pred_obs_one.timestamp == self.sync_pred_obs_two.timestamp \
         == self.sync_pred_obs_three.timestamp:
            self.sync_timestamp = self.sync_pred_obs_one.timestamp
        else :
            pass

    def get_sync_id(self):
        if self.sync_pred_obs_zero.id == self.sync_pred_obs_one.id == self.sync_pred_obs_two.id \
         == self.sync_pred_obs_three.id:
            self.sync_id = self.sync_pred_obs_one.id
        else :
            pass



        
        # self.sync_ptred_obs.append(predictobs)




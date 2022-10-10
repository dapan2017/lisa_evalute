# -*- coding: utf-8 -*-
# Copyright © 2021 Li Auto. All rights reserved.

"""Obstacle data structure"""

import json
from enum import Enum
import math
import logging
from typing import Dict, List, Tuple

import numpy as np

class ObstacleType(Enum):
    VISION = 1
    LIDAR = 2
    RADAR = 3
    DEFAULT = 4


class Obstacle(object):
    """Obstacle class
    """

    def __init__(self, obstacle_info):
        """Init

        Args:
            obstacle_info: obstacle basic info from raw data
            mode: insert obstacle mode, eg: predicted, ground_truth
        """
        logging.info(obstacle_info)

        self.id: int = obstacle_info['id']
        self.yaw: float = obstacle_info['world_info']['yaw']
        self.height: float = obstacle_info['world_info']['height']
        self.length: float = obstacle_info['world_info']['length']
        self.width: float = obstacle_info['world_info']['width']
        self.position_x: float = obstacle_info['world_info']['position']['x']
        self.position_y: float = obstacle_info['world_info']['position']['y']
        self.vx :float = obstacle_info['world_info']['vel_abs_world']['vx']
        self.vy :float = obstacle_info['world_info']['vel_abs_world']['vy']
        self.obstacle_type: int = obstacle_info['type']

        # Polygon points is head_left, head_right, tail_right, tail_left
        # self._polygon: List[Tuple(float)] = self.get_polygon_points(type)

    # def get_polygon_points(self, type: ObstacleType) -> List[Tuple[float]]:
    #     """Get polygon points of obstacle"""
    #     rotation_matrix: np.ndarray = np.array([[math.cos(self._yaw), -1 * math.sin(self._yaw)],
    #                                             [math.sin(self._yaw), math.cos(self._yaw)]])

    #     # Convert position xy into obstacle centroid
    #     if type == ObstacleType.VISION:
    #         if abs(self.normalize_angle(self._yaw)) < math.pi * 0.5:
    #             self._position_x += 0.5 * self._length * math.cos(self._yaw)
    #             self._position_y += 0.5 * self._length * math.sin(self._yaw)
    #         else:
    #             self._position_x += - 0.5 * self._length * math.cos(self._yaw)
    #             self._position_y += - 0.5 * self._length * math.sin(self._yaw)
    #     elif type == ObstacleType.LIDAR:
    #         pass
    #     else:
    #         raise TypeError

    #     polygon = []
    #     pos_pt: np.ndarray = np.array([self._position_x, self._position_y])
    #     rotate_pt: np.ndarray = np.matmul(rotation_matrix, np.transpose(pos_pt))
    #     # Head-Left
    #     corner_pt: np.ndarray = np.array([0.5 * self._length, 0.5 * self._width])
    #     rotate_pt: np.ndarray = np.matmul(rotation_matrix, np.transpose(corner_pt))
    #     polygon.append((rotate_pt[0] + pos_pt[0], rotate_pt[1] + pos_pt[1]))
    #     # Head-Right
    #     corner_pt: np.ndarray = np.array([0.5 * self._length, -0.5 * self._width])
    #     rotate_pt: np.ndarray = np.matmul(rotation_matrix, np.transpose(corner_pt))
    #     polygon.append((rotate_pt[0] + pos_pt[0], rotate_pt[1] + pos_pt[1]))
    #     # Tail-Right
    #     corner_pt: np.ndarray = np.array([-0.5 * self._length, -0.5 * self._width])
    #     rotate_pt: np.ndarray = np.matmul(rotation_matrix, np.transpose(corner_pt))
    #     polygon.append((rotate_pt[0] + pos_pt[0], rotate_pt[1] + pos_pt[1]))
    #     # Tail-Left
    #     corner_pt: np.ndarray = np.array([-0.5 * self._length, 0.5 * self._width])
    #     rotate_pt: np.ndarray = np.matmul(rotation_matrix, np.transpose(corner_pt))
    #     polygon.append((rotate_pt[0] + pos_pt[0], rotate_pt[1] + pos_pt[1]))

    #     return polygon

    # @property
    # def yaw(self):
    #     return self._yaw

    # @property
    # def height(self):
    #     return self._height

    # @property
    # def length(self):
    #     return self._length

    # @property
    # def width(self):
    #     return self._width

    # @property
    # def position_x(self):
    #     return self._position_x

    # @property
    # def position_y(self):
    #     return self._position_y

    # @property
    # def polygon(self):
    #     return self._polygon

    # def normalize_angle(self, angle: float) -> float:
    #     """Convert angle (rad) into [-pi, pi)"""
    #     while angle > math.pi:
    #         angle -= 2 * math.pi
    #     while angle < -math.pi:
    #         angle += 2 * math.pi

    #     return angle

class Obstacles(object):
    def __init__(self,obs):
        self.obs = obs
        self.obs_list = []

    def choose_obs(self):
        for obs in self.obs:
            # print(obs)
            self.obs_list.append(Obstacle(obs))




if __name__ == '__main__':
    json_path = "/Users/panjiqing/Downloads/test_framework_v0.1/exampledata/line4.json"
    with open(json_path, 'r') as f:
        data = json.load(f)
        obs_info = data['obstacle']
        # print(post_lines_info)
        all_obs = Obstacles(obs_info)
        all_obs.choose_obs()
        obs0 = all_obs.obs_list[0] 
        print(obs0.id)
        print(obs0.yaw)
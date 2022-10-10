# -- coding:UTF-8 --<code>

import json

from enum import Enum

class LineType(Enum):
    # line position
    LineType_Line_Left = 0x1
    LineType_Line_Right = 0x2
    LineType_Line_Left_Left = 0x4
    LineType_Line_Right_Right = 0x8
    #line types
    LineType_Line_Ramp = 0x100;     #256
    LineType_Line_Double = 0x200;     #512
    LineType_Line_Dash = 0x400;   #1024
    LineType_Line_Solid =0x800;    #2048
    # line color
    LineType_Line_White = 0x1000;     #4096
    LineType_Line_Yellow = 0x2000;      #8192
    LineType_Line_Blue = 0x4000;     #16384,reserved
    LineType_Line_Green = 0x8000;    #reserved

    LineType_Line_Fence = 0x10000;            # 1 << 16, for fence
                                                        # and road boundary(side walk, Terran, etc)
    LineType_Line_Road_Height = 0x20000;     # Road Height (1 << 17)
    LineType_Line_Diversion_Inside = 0x40000; # Diversion line inside (1 << 18)
    # fence properties
    LineType_Line_Barrier = 0x80000;            # Barrier:栅栏 (1 << 19)
    LineType_Line_Diversion_Outside = 0x100000; # Diversion line outside (1 << 20)
    # line source
    LineType_Line_Perception = 0x200000;        # from perception (1 << 21)
    LineType_Line_Tracking = 0x400000;         # from tracking (1 << 22)
    # line model type
    LineType_Line_Raw = 0x800000;              # original line (1 << 23)
    LineType_Line_Road = 0x1000000;            # road model (1 << 24)
    LineType_Line_Pole = 0x2000000;            # pole tracking (1 << 25)
    LineType_Line_Road_Unparallel = 0x4000000;  # road model switch to raw (1 << 26)

    LineType_Line_Type_Path = 0x20000000;     # center (1 << 29)

class Line(object):
    """Lines class
    """

    def __init__(self,lines_info):
        """Init

        Args:
            obstacle_info: obstacle basic info from raw data
            mode: insert obstacle mode, eg: predicted, ground_truth
        """

        self.coeffs = lines_info['coeffs']
        self.end_point = lines_info['end_points'][0]
        self.start_point = lines_info['end_points'][1]
        self.type = self.get_lines_type(lines_info['type'])    
  

    def get_lines_type(self,line_type):
        # 车道线类型由数据类型中的type和LineType按位与计算
        return [val.name[val.name.rfind('_', 1) + 1:] for val in LineType if line_type & val.value !=0]


class Lines(object):
    def __init__(self,lines):
        self.lines = lines
        self.left = None
        self.right = None

    def chose_line(self):
        for single_line in self.lines:
            post_Line = Line(single_line)
            if 'Road' in post_Line.type:
                if 'Left' in post_Line.type:
                    self.left = post_Line
                elif 'Right' in post_Line.type:
                    self.right = post_Line
                        
                    

if __name__ == '__main__':
    post_json = "/Users/panjiqing/Downloads/test_framework_v0.1/exampledata/line1.json"
    print(Lines.__mro__)
    with open(post_json, 'r') as f:
        data = json.load(f)
        post_lines_info = data['lines']
        # print(post_lines_info)
        lines = Lines(post_lines_info)
        lines.chose_line()
        print(lines.left.coeffs)
        
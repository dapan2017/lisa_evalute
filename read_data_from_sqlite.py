# -*- coding: utf-8 -*-
# @Author  : bedeyoux@gmail.com
# @Time    : 2022/7/26 下午5:49
# @Function: sqlite 数据读取
import sqlite3
import json
import pandas as pd
import csv

# 所有topic
'''['_Fusion_SafetyFunc_ObstacleFramePart@0', '_VAL_Lidar_0_PointCloud@0', '_VAL_Radar_SGU_Objects@0', 
'_Val_ActuatorStatus@0', '_Val_Navigation_Gnss@0', '_Val_Navigation_Imu@0', '_Val_Navigation_Ins@0', 
'_Val_Navigation_Odom@0', '_Val_VehicleStatus@0', '_fusion_adapter_obstacles@0', '_rt_envfrontlines_asafety@0', 
'_rt_envrearlines_asafety@0', '_rt_hmi_debug@0', '_rt_hmi_hu_traffic@0', '_rt_hmi_noa_info@0', 'NDM_Location@0', 
'Perception_CameraObstacles@0', 'Perception_EnvStaticObject@0', 'Perception_LaneLine@0', 'Perception_LaneLineSurround@0',
 'Perception_LidarObstacles@0', 'Perception_MovableObject@0', 'Perception_Object@0', 'Perception_PerceptionRaw@0', 
 'Perception_VehicleSinCamObject@0', 'Topic_FsdWarningInfo@0', 'liodometry@0', 'rt_chart_behaviors@0', 
 'rt_env_fusion_map@0', 'rt_env_pilot_context@0', 'rt_env_pilot_context_profile@0', 'rt_env_model_lanes@0',
  'rt_env_model_obstacles@0', 'rt_func_driver_interaction@0', 'rt_func_func_report@0', 'rt_fusion_odometry_obstacles@0',
   'rt_pnc_control_actuator@0', 'rt_pnc_control_command@0', 'rt_pnc_control_debug@0', 'rt_pnc_pilot_planning_result@0', 
'rt_situation_situation_assessments@0']'''

def read_data_from_sqlite(data_path , save_path , topic_list):
    
    
    dbc = sqlite3.connect(data_path)    # 连接数据库
    cursor = dbc.cursor()   # 建立游标

    cursor.execute("select name from sqlite_master where type='table' ")
    table_cols = 'rti_json_sample'
    print(type(table_cols))
    for table_name in cursor.fetchall():
        topic_name =table_name[0].replace('/' , '_').split("@")[0]
        print(topic_name)
        if topic_name in topic_list:
            data_pd = pd.DataFrame()
            print(topic_name )
            for data in cursor.execute("select %s from %s" % (table_cols ,'{1}{0}{1}'.format(str(table_name[0]),"'"))):
                # print(type(data))
                try:
                    
                    js = json.loads(data[0])
                    js = json.dumps(js)
                    # print(js["timestamp"])
                    
                    data_pd = data_pd.append([[js]])
                except:
                    print("data is wrong!")
            data_pd.columns = [topic_name]
            data_pd.to_csv( save_path + str(topic_name) + ".csv" , quoting=csv.QUOTE_NONE , escapechar ='\x20' , index=None)

    cursor.close()  # 关闭句柄
    dbc.close()  # 关闭数据连接

    


if __name__ == '__main__':

    # data_path = './data/test_data/json_recording/rti_recorder_default.dat'
    # save_path = "./data/test_data/"
    # data_path = './data/AEB_data/rti_recorder_default_converted.dat'
    # save_path = "./data/AEB_data/"
    data_path = '/Users/panjiqing/Desktop/licode/data/parking_data/rti_recorder_default.dat'
    save_path = "/Users/panjiqing/Desktop/licode/data/parking_data/"
    # topic_list = ['Perception_LaneLine','Perception_CameraObstacles' , 'Perception_LidarObstacles']
    # topic_list =['_viz_prediction_pred_obstacles']
    topic_list = ['rt_parking_raw']
    read_data_from_sqlite(data_path , save_path , topic_list)
    

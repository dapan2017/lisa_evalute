import pandas as pd
import json
from predictobstacle import PredictObstacle
from predictobstacle import SyncPredictObstacle
import queue

data_path = "/Users/panjiqing/Desktop/licode/data/predict_data/new/_viz_prediction_pred_obstacles.csv"

with open(data_path, 'r',encoding='utf-8-sig') as f:
    label_dict = {}
    maxsize = 4
    for line in f:
        if line != '_viz_prediction_pred_obstacles\n':
            # print(json.loads(line)["markers"])
            data = json.loads(line)["markers"]
            if len(data) > 0:
                syncobs = SyncPredictObstacle(4)
                for obs in data:
                    pred_obs = PredictObstacle(obs)
                    pred_obs.get_id_time()
                    pred_obs.get_cutin_adc()
                    if pred_obs.id_time == None :
                        del pred_obs
                        continue
                    else:
                        syncobs.add_predict_obs(pred_obs)
                if syncobs.sync_pred_obs_zero != None: 
                    syncobs.get_sync_timestamp()
                    syncobs.get_sync_id()
                    if syncobs.sync_pred_obs_zero.cutin_adc == 1:
                        print('groudtrouth cutin label : {}  timestamp : {}  obs_id : {} '.format(syncobs.sync_pred_obs_zero.cutin_adc,syncobs.sync_timestamp,syncobs.sync_id))
                    if syncobs.sync_pred_obs_one.cutin_adc == 1:
                        print('predict one cutin label : {}   timestamp : {}  obs_id : {} '.format(syncobs.sync_pred_obs_one.cutin_adc ,syncobs.sync_timestamp,syncobs.sync_id ))
                        print('predict two cutin label : {}   timestamp : {}  obs_id : {} '.format(syncobs.sync_pred_obs_two.cutin_adc ,syncobs.sync_timestamp,syncobs.sync_id ))
                    if syncobs.sync_id not in label_dict.keys():
                        label_dict[syncobs.sync_id] = queue.Queue(maxsize)
                    # print("length of queue:" , label_dict[syncobs.sync_id].qsize())
                    if label_dict[syncobs.sync_id].qsize() == maxsize:
                        label_dict[syncobs.sync_id].get()
                    label_dict[syncobs.sync_id].put(syncobs)


    print(label_dict)



import json

parking_path = "/Users/panjiqing/Desktop/licode/data/parking_data/rt_parking_raw.csv"

timestamp_list = []
with open(parking_path, 'r',encoding='utf-8-sig') as f:
  
    for line in f:
        # print(line)
        if line != 'rt_parking_raw\n':
            data = json.loads(line)
            print(data["pub_timestamp"])
            timestamp_list.append(data["pub_timestamp"])

print(timestamp_list)

timestamp_gap = timestamp_list[-1] - timestamp_list[0]

fps = 1000/(timestamp_gap/len(timestamp_list))
print(fps)

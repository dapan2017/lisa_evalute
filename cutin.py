from obstacle import Obstacles
from lines import Lines
import json



post_json = "/Users/panjiqing/Downloads/test_framework_v0.1/exampledata/line1.json"
with open(post_json, 'r') as f:
    data = json.load(f)
    post_lines_info = data['lines']
    # print(post_lines_info)
    lines = Lines(post_lines_info)
    lines.chose_line()
    # print(lines.left.coeffs)

json_path = "/Users/panjiqing/Downloads/test_framework_v0.1/exampledata/line4.json"
with open(json_path, 'r') as f:
    dbaata = json.load(f)
    obs_info = data['obstacle']
    # print(post_lines_info)
    all_obs = Obstacles(obs_info)
    all_obs.choose_obs() 
    
for obs in all_obs.obs_list:
    print(obs.id)
    print(obs.position_y)
    if obs.position_y > lines.left.coeffs[0] or  obs.position_y < lines.right.coeffs[0]:
        print("CUTIN")


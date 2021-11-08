'''
Input file format (.csv):
If the player is TTST, the third column should be Yes (or any other string)
Example: 
電機一,張伯倫
土木二,錢德勒,Yes
光電碩一,李嘉圖
生傳三,吳郭魚
高分子碩二,胡迪
醫學六,羅斯福,Yes
園藝一,高斯
'''

def file_reader(filename, PLAYERS_IN_ONE_GROUP, PLAYERS_IN_ONE_GROUP_OTHERWISE):
    with open(filename, "r") as f:
        data = f.read().split()
    
    player_num = len(data)
    if PLAYERS_IN_ONE_GROUP < PLAYERS_IN_ONE_GROUP_OTHERWISE:
        group_num = player_num // PLAYERS_IN_ONE_GROUP
        group_num_abnormal = player_num % PLAYERS_IN_ONE_GROUP
    else:
        group_num = player_num // PLAYERS_IN_ONE_GROUP_OTHERWISE
        group_num_abnormal = player_num % PLAYERS_IN_ONE_GROUP_OTHERWISE
    group_num_normal = group_num - group_num_abnormal

    return data, group_num_normal, group_num_abnormal

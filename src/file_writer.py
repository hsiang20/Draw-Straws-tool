'''
Output file format (.txt):
Example
參賽選手 7 人，共 2 組

第 1 組：
醫學六,羅斯福,Yes
光電碩一,李嘉圖
生傳三,吳郭魚

第 2 組：
土木二,錢德勒,Yes
電機一,張伯倫
高分子碩二,胡迪
園藝一,高斯
'''

def file_writer(filename, result):
    player_num = 0
    group_num = len(result)
    for i in range(group_num):
        player_num += len(result[i])

    with open(filename, "w") as f:
        f.write("參賽選手 %d 人，共 %d 組\n" % (player_num, group_num) )
        for i in range(len(result)):
            f.write("\n")
            f.write("第 %d 組：" % (i+1))
            f.write("\n")
            for player in result[i]:
                f.write(player)
                f.write("\n")
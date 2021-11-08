# Schedule Arranger

## Introduction
The project is for tabletennis school team of National Taiwan University.\n
It can help arranging the schedules of the contests, giving the data of the players.\n

## Usage
'''
$ python src/main.py [INPUTFILE_NAME] [OUTPUTFILE_NAME]
'''
Note that the input file should be a .csv file. The output file would be a .txt file.

## File Format
### Input
The first column is the departments of the players.
The second column is the players' names.
If the player is TTST, the third column should be Yes (or any other string).
Example: 
電機一,張伯倫
土木二,錢德勒,Yes
光電碩一,李嘉圖
生傳三,吳郭魚
高分子碩二,胡迪
醫學六,羅斯福,Yes
園藝一,高斯
### Output
Example:
參賽選手 7 人，共 2 組

第 1 組： 
電機一,張伯倫
土木二,錢德勒,Yes
光電碩一,李嘉圖

第 2 組：
生傳三,吳郭魚
高分子碩二,胡迪
醫學六,羅斯福,Yes
園藝一,高斯

## Variables
* DEPARTMENT: If True, the players of the same department would be seperated to different groups. Default True.
* TTST: If True, the players of the tabletennis school team would be seperated to different groups. Default True.
* PLAYERS_IN_ONE_GROUP: The number of players in one group. Default 3.
* PLAYERS_IN_ONE_GROUP_OTHERWISE: If the remainder is not 0, the number of the remain players in one group. Default 4.
> The difference of these two variables must be 1.
> For example, 
> If number of players is 32, 
> PLAYERS_IN_ONE_GROUP = 3
> PLAYERS_IN_ONE_GROUP_OTHERWISE = 4
> Then there will be 8 groups containing 3 players and 2 groups 
> containing 4 players.
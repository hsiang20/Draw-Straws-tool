import random
import sys
from file_reader import file_reader

'''
Variables:
1. DEPARTMENT
    When True, players in the same department will not be arranged to 
    the same group.
2. TTST
    When True, the members of TTST will not be arranged to the same 
    group.
3. PLAYERS_IN_ONE_GROUP and PLAYERS_IN_ONE_GROUP_OTHERWISE
    The difference of these two variables must be 1.
    For example, 
    If number of players is 32, 
    PLAYERS_IN_ONE_GROUP = 3
    PLAYERS_IN_ONE_GROUP_OTHERWISE = 4
    Then there will be 8 groups containing 3 players and 2 groups 
    containing 4 players.

'''

DEPARTMENT = True
TTST = True
PLAYERS_IN_ONE_GROUP = 3
PLAYERS_IN_ONE_GROUP_OTHERWISE = 4


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: \npython main.py [INPUTFILE]")
        sys.exit()

    filename = sys.argv[1]
    if filename[-3:] != "csv":
        print("ERROR: Input file must be .csv file.")
        sys.exit()
    
    assert abs(PLAYERS_IN_ONE_GROUP - PLAYERS_IN_ONE_GROUP_OTHERWISE) == 1, ""\
        "Difference of PLAYERS_IN_ONE_GROUP and PLAYERS_IN_ONE_GROUP_OTHERWISE "\
        "should be 1."

    data, group_num_normal, group_num_abnormal = file_reader(filename, PLAYERS_IN_ONE_GROUP, PLAYERS_IN_ONE_GROUP_OTHERWISE)

    

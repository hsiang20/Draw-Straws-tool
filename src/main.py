import random
import sys
from file_reader import file_reader
from file_writer import file_writer
from arranger import Arranger

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
    if len(sys.argv) < 3:
        print("Usage: \npython main.py [INPUTFILE] [OUTPUTFILE_NAME]")
        sys.exit()

    filename = sys.argv[1]
    if filename[-3:] != "csv":
        print("ERROR: Input file must be .csv file.")
        sys.exit()
    
    assert abs(PLAYERS_IN_ONE_GROUP - PLAYERS_IN_ONE_GROUP_OTHERWISE) == 1, ""\
        "Difference of PLAYERS_IN_ONE_GROUP and PLAYERS_IN_ONE_GROUP_OTHERWISE "\
        "should be 1."

    data, group_num_normal, group_num_abnormal = file_reader(filename, 
                                                             PLAYERS_IN_ONE_GROUP, 
                                                             PLAYERS_IN_ONE_GROUP_OTHERWISE)
    
    if (group_num_normal < 0 or group_num_abnormal < 0):
        print("Error: Cannot arrange schedule using given variables.\n"\
              "Try to change PLAYER_IN_ONE_GROUP and PLAYER_IN_ONE_GROUP_ABNORMAL.")
        sys.exit()

    Arranger = Arranger(data, 
                        PLAYERS_IN_ONE_GROUP, 
                        group_num_normal, 
                        PLAYERS_IN_ONE_GROUP_OTHERWISE, 
                        group_num_abnormal, 
                        DEPARTMENT=DEPARTMENT, 
                        TTST=TTST)

    result = Arranger.get_result()
    filename_out = sys.argv[2]
    file_writer(filename_out, result)


    

import random
import sys
from file_reader import file_reader
from file_writer import file_writer
from arranger import Arranger
import argparse
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
parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
parser.add_argument("-d", "--department", help="When True, players in the same department will not be arranged to the same group.", default=True)
parser.add_argument("-t", "--ttst", help="When True, the memebers of TTST will not be arranged to the same group.", default=True)
parser.add_argument("-p", "--players_per_group", help="Players per group", default=3)
parser.add_argument("-o", "--players_per_group_other", help="Players per group (if remained)", default=4)
args = parser.parse_args()

DEPARTMENT = args.department
TTST = args.ttst
PLAYERS_IN_ONE_GROUP = args.players_per_group
PLAYERS_IN_ONE_GROUP_OTHERWISE = args.players_per_group_other


if __name__ == "__main__":
    '''
    if len(sys.argv) < 3:
        print("Usage: \npython main.py [INPUTFILE] [OUTPUTFILE_NAME]")
        sys.exit()
    '''

    filename = args.inputfile
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
    filename_out = args.outputfile
    file_writer(filename_out, result)


    

from random import randint
import sys

class Arranger:
    def __init__(self, data, player_normal, group_normal, 
                 player_abnormal, group_abnormal, 
                 DEPARTMENT=True, 
                 TTST=True):
        self.data = data
        self.players = len(data)
        self.groups = group_normal + group_abnormal
        self.player_normal = player_normal
        self.player_abnormal = player_abnormal
        self.group_normal = group_normal
        self.group_abnormal = group_abnormal
        self.department = DEPARTMENT
        self.ttst = TTST
        self.result = list()
        for i in range(self.groups):
            self.result.append([])
        if self.department:
            self.department_list = self.department_data()
        if self.ttst:
            self.ttst_list = self.ttst_data()
        self.variable_check()
        self.print_info()

    def variable_check(self):
        if self.department:
            self.player_department = self.department_data()
            if len(list(self.player_department.values())[0]) > self.groups:
                print("ERROR: The number of players in %s is more than the number of groups."
                      % (list(self.player_department.keys())[0]))
                sys.exit()
        if self.ttst:
            self.player_ttst = self.ttst_data()
            if len(self.player_ttst) > self.groups:
                print("ERROR: The number of players in ttst is more than the number of groups.")
                sys.exit()

    def department_data(self):
        department_dict = dict()
        for i in range(len(self.data)):
            player_data = self.data[i].split(',')
            if player_data[0][0:2] in department_dict:
                department_dict[player_data[0][0:2]].append(i)
            else:
                department_dict[player_data[0][0:2]] = list()
                department_dict[player_data[0][0:2]].append(i)
        department_dict = dict(sorted(department_dict.items(), key=lambda item: len(item[1]), reverse=True))
        return department_dict

    def ttst_data(self):
        ttst_list = list()
        for i in range(len(self.data)):
            player_data = self.data[i].split(',')
            try:
                if player_data[2] != '':
                    ttst_list.append(i)
            except:
                pass
        return ttst_list

    def print_info(self):
        print(""\
        "--------------------------------------------\n"\
        "Number of players: %d\n"\
        "Number of %d-player groups: %d\n"
        "Number of %d-player groups: %d\n"
        "--------------------------------------------" %
        (len(self.data), self.player_normal, self.group_normal, 
        self.player_abnormal, self.group_abnormal))

    def print_result(self):
        print(""\
        "              Arrange Complete!\n"\
        "--------------------------------------------")

    def check_full(self, group):
        assert group < self.groups
        if group < self.group_normal:
            return len(self.result[group]) == self.player_normal
        else:
            return len(self.result[group]) == self.player_abnormal

    def arrange(self):
        data_old = list()
        for i in range(len(self.data)):
            data_old.append(self.data[i])
        data_new = []
        for player_data in data_old:
            data_new.append(player_data.split(','))

        if self.ttst:
            for player in self.ttst_list:
                while True:
                    group = randint(0, self.groups - 1)
                    if len(self.result[group]) != 0:
                        continue
                    else:
                        self.result[group].append(player)
                        data_old.remove(self.data[player])
                        break
        
        if self.department:
            for department in self.department_list:
                remain_group = [i for i in range(self.groups)]
                for player in self.department_list[department]:
                    if self.data[player] in data_old:
                        while True:
                            if len(remain_group) == 0:
                                return False
                            group = randint(0, self.groups - 1)
                            if group in remain_group and not self.check_full(group):
                                remain_group.remove(group)
                                self.result[group].append(player)
                                break
                            else:
                                continue
                    else:
                        for i in range(self.groups):
                            if player in self.result[i]:
                                remain_group.remove(i)
                                break

        else:
            for player in range(len(self.data)):
                if self.data[player] in data_old:
                    while True:
                        group = randint(0, self.groups - 1)
                        if not self.check_full():
                            self.result[group].append(player)
                            break
                        else:
                            continue
            
        return self.result
                    
    def get_result(self):
        while True:
            if self.arrange() != False:
                self.print_result()
                break
        result = [[] for i in range(self.groups)]
        for i in range(self.groups):
            for player in self.result[i]:
                result[i].append(self.data[player])
        return result
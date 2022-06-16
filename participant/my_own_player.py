import random
from . import participant as part
import copy


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('name of your team', 'team num')
        # you can change everything in this code file!!
        # also, you can define your own variables here or in the overriding method
        # Any modifications are possible if you follows the rules of Squid Game


    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        # you can override this method in this sub-class
        # this method must contain 'self.initialize_params()' which is for initializing some essential variables
        # you can initialize what you define
        self.initialize_params()
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be the number of marbles bet (> 0)!
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        return random.randint(playground_marbles.MIN_HOLDING, my_current_marbles)

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!
        answer = bool(random.randint(0, 1))
        return self.set_statement(answer)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        # you can override this method in this sub-class
        # you can refer to an object of 'glass_stepping_stones', named as 'playground_glasses'
        # the return should be 0 or 1 (int)!
        if self.position == 0:
            self.temp_list = copy.deepcopy(playground_glasses._players_steps)  # 상대방것도 복사
        length = len(self.temp_list)
        if self.previous_player != 'None' and self.temp_list != []:
            if self.position < length - 1:  # 카피 한 것보다 앞에 있으면
                print(self.temp_list)
                # print('chk1')
                return self.temp_list[self.position]  # 내가 갔던 곳으로
            else:
                if self.position == length - 1:
                    # print('chk2')
                    if self.temp_list[self.position] == 0:
                        return 1
                    else:
                        return 0
                else:
                    # print('chk3')
                    return random.randint(0, 1)
        return 'error'
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        # you can override this method in this sub-class
        # this method gathers your members for the tug of war game
        # you only can change the configuration of the numbers of person types
        # there are 4 types of persons
        # type1 corresponds a ordinary person who has standard stats for the game
        # type2 corresponds a person with great height
        # type3 corresponds a person with a lot of weight
        # type4 corresponds a person with strong power
        # the return should be a tuple with size of 4, and the sum of the elements should be 10
        # only for computer, it is allowed to set 12 members
        com_max_rate = 15
        # 컴퓨터 전략상 발휘할 수 있는 최대 stamina : 15
        com_max_force = (com_max_rate / 100) * 27000
        # forces = [(left_player_rate / 100) * self.__player_strength[0],
        #           (right_player_rate/ 100) * self.__player_strength[1]] (main.py 115-116줄)
        # 컴퓨터 전략상 발휘할 수 있는 최대 힘 : 4050
        global z
        z = 0
        # 아래 act_tugging_strategy에서 최적 opt_s 탐색 알고리즘이 한 게임당 1회만 돌아가도록 하기 위한 fake variable.
        global opt_n
        for opt_n in range(0,11):
            player_static_force =  0.2 * (opt_n * 110 + 78 * (10 - opt_n)) * 9.8 * 2.5
            # static_f_force = 0.2 * weight * self.__GRAVIT_ACCEL * self.__STATIC_FRICTION[condition_id] (main.py 87줄)
            # 플레이어가 넘어지지 않는 경우 self.__STATIC_FRICTION[condition_id] 값이 2.5로 고정됨
            # 팀의 무게에 따라 팀의 정지 마찰력이 달라짐
            if player_static_force > com_max_force:
                # 팀의 정지 마찰력이 컴퓨터의 발휘할 수 있는 최대힘보다 크도록 무게를 구성하면, 어떠한 경우에도 컴퓨터는 줄을 당길 수 없다.
                # 위의 조건을 만족하면서 strength를 최대화 할 수 있도록 팀을 구성하는 i를 찾음.
                break
        # print(' □ : 최적 조합은 무거운 사람 {}명, 힘 센 사람을 {}명 조합이다.'.format(opt_n, 10-opt_n))
        # 사실상 컴퓨터 전략이 바뀌지 않기에, 조합은 (0,0,2,8)로 고정된다
        # 즉, 내 플레이어의 정지 마찰력이 4135.6
        # 컴퓨터의 전략이 바뀌는 경우 코드의 일반화를 위해 최적 조합 탐색 알고리즘 작성함.
        return (0, 0, opt_n, 10-opt_n)

    def act_tugging_strategy(self, playground_tug_of_war):
        # you can override this method in this sub-class
        # you can refer to an object of 'tug_of_war', named as 'playground_tug_of_war'
        # the return should be a float value in [0, 100]!
        # note that the float represents a stamina-consuming rate for tugging
        if playground_tug_of_war.player_expression['Computer'] in ['best', 'well']:
            return 0
            # 컴퓨터 전략 상 'best' 나 'well'인 상황에는 stamina를 1-15까지 중 한 값으로 상대적으로 높게 사용하기 때문에, 굳이 상대해주지 않음.
            # return 값이 0 이어도 위의 팀 구성 단계에서 애초에 끌려갈 수 없도록 설계함.
        else:
            if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                player_tug_range = ((opt_n * 162 + (10 - opt_n) * 165) / 10) * 0.35 * 0.01
                # 0.5754 m
                # 이 때, 도출된 Distance(d)가 내 tugging range (height * 0.35) = 0.5754m 보다 높게 나오면 넘어짐
                # (main.py 196-218 줄)
                # 넘어지는 상황을 방지하기 하면서, 최대 힘을 낼 수 있는 stamina consume rate 인 opt_s 찾는 것을 목표로 함.
                com_min_rate = 1
                # 컴퓨터는 전략상 이 때에 1,2,3 중 하나의 값을 return 하기 때문에 1로 설정
                com_weight = 936
                team_weight = 844
                total_weight = com_weight + team_weight
                com_static_force = 0.2 * com_weight * 9.8 * 2.5
                com_strength = 12 * 5 * 450
                com_min_force = (com_min_rate / 100) * com_strength
                player_opt_strength = 5 * (opt_n * 300 + (10 - opt_n) * 450)
                global opt_s, z
                while z == 0 :
                    for opt_s in range(101,1,-1):
                        sum_force = player_opt_strength * (opt_s / 100) - com_min_force
                        a = (sum_force - com_static_force) / total_weight
                        v = a * 0.2
                        d = v + 0.5 * a * 0.2 * 0.2
                        if d < player_tug_range :
                            z +=1
                            break
                return opt_s
                # opt_s = 45

            else:
                return 0
                # 내 플레이어의 stamina 상태가 회복될 때 까지 대기함.
                # return 값이 0 이어도 위의 팀 구성 단계에서 애초에 끌려갈 수 없도록 설계함.
    # ================================================================================= for tug_of_war game

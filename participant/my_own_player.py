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

        return (0, 0, 0, 10)
        # 수적 열세인 상황에서 일반적인 힘겨루기로는 승리 가능성이 낮다 전망, 넘어진 상태를 최대한 활용하여 승리 모색
        # 후술할 set.condition 메서드를 통해 넘어진 상태를 강제로 일으킬 수 있으므로 tugging range는 고려 X(tall person 의미 X)
        # computer 진영을 넘어뜨려야 하기에, 상대가 높은 stamina를 return할 때 최대한 많이 끌려가야 함(heavy person 비효율적)
        # 상대를 넘어뜨린 이후 최대한 많이 끌어와야 하므로 비슷한 몸무게 조건에서 힘이 더 쎈 사람 필요함(ordinary person 비효율적)

    def act_tugging_strategy(self, playground_tug_of_war):
        # you can override this method in this sub-class
        # you can refer to an object of 'tug_of_war', named as 'playground_tug_of_war'
        # the return should be a float value in [0, 100]!
        # note that the float represents a stamina-consuming rate for tugging

        opponent_con = playground_tug_of_war.player_condition["Computer"]
        myself_con = playground_tug_of_war.player_condition[self.name]
        opponent_exp = playground_tug_of_war.player_expression["Computer"]
        myself_exp = playground_tug_of_war.player_expression[self.name]

        if myself_con == False:
            super().set_condition(True) # 넘어진 상태에서 participant 클래스의 메서드를 활용해 강제로 일으키기
            return 5 # computer 측은 우리 진영을 넘어진 상태로 인식하고 있으므로 최저의 return으로 넘어짐 유도
        else:
            if opponent_con == False:
                return 40 # 상대가 넘어졌을 때 최대한 끌어오기
            else:
                if opponent_exp in ['best', 'well']:
                    return 0 # 일반적인 경우에서의 힘겨루기는 수적 열세로 인해 승리 확률 낮으므로 stamina 보전 목적
                else:
                    return 15 # 상대의 stamina가 낮을 때 반환되는 return이 적을 것으로 예상, configuration 특징 활용해 승부
     # ================================================================================= for tug_of_war game
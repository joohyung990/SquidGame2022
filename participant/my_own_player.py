import random
from . import participant as part
import copy


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('no one', 'team D')
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

        return 1

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!

        if playground_marbles._marbles_in_hand % 2 == 0:
            answer = False
        else:
            answer = True
        return self.set_statement(answer)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    real_answer = []    # 내 경로가 저장될 list
    def step_toward_goal_strategy(self, playground_glasses):
        # you can override this method in this sub-class
        # you can refer to an object of 'glass_stepping_stones', named as 'playground_glasses'
        # the return should be 0 or 1 (int)!

        if playground_glasses._round == 1:
            self.real_answer = []
            first_step = random.randint(0, 1)
            self.real_answer.append(first_step)
            return first_step   # 첫 번째 징검다리는 random
        else:
            if len(self.real_answer) < len(playground_glasses._players_steps):
                self.real_answer = copy.deepcopy(playground_glasses._players_steps)
                # 상대가 나보다 많이 진행했을 경우 상대의 경로 복사
            length = len(self.real_answer)
            length_com = len(playground_glasses._players_steps)
            if self.position < length - 1:
                return self.real_answer[self.position]  # 상대가 떨어지기 전 단계까지는 똑같이 진행
            elif self.position == length - 1:
                if self.real_answer[self.position] == 0:
                    self.real_answer[self.position] = 1
                else:
                    self.real_answer[self.position] = 0
                return self.real_answer[self.position]  # 상대가 떨어졌던 곳에서 다른 징검다리 선택
            elif self.position == length:
                self.real_answer.append(random.randint(0, 1))
                if length >= length_com:    # 내가 상대보다 멀리 진행했을 경우
                    if self.real_answer[0] == 0:
                        playground_glasses._players_steps[0] = 1
                    else:
                        playground_glasses._players_steps[0] = 0    # 상대가 참고할 내 경로의 출발지점을 바꿔버리기
                return self.real_answer[self.position]  # 그 이후는 random
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

        return (0, 1, 0, 9)
        # 수적 열세인 상황에서 일반적인 힘겨루기로는 승리 가능성이 낮다 전망, 넘어진 상태를 최대한 활용하여 승리 모색
        # computer 진영을 넘어뜨려야 하기에, 상대가 높은 stamina를 return할 때 최대한 많이 끌려가야 함(heavy person 비효율적)
        # 상대를 넘어뜨린 이후 최대한 많이 끌어와야 하므로 비슷한 몸무게 조건에서 힘이 더 쎈 사람 필요함(ordinary person 비효율적)
        # tall person 1명 추가함으로써 전체적인 strength에 크게 영향이 없는 선에서 tugging range, maximum dragging distance 증가

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
            return 0 # 넘어진 상태에서는 stamina 투자에 따른 net force 기댓값이 현저히 낮으므로 stamina 보전 목적
        else:
            if opponent_con == False:
                return 40 # 상대가 넘어졌을 때 최대한 끌어오기
            else:
                if myself_exp == 'worst':
                    if opponent_exp in ['best', 'well']:
                        return 0 # stamina 회복 및 상대의 넘어짐 유도
                    else:
                        return 10 # 상대의 stamina가 낮을 때 반환하는 return이 적을 것으로 예상, configuration 특징 활용해 승부
                elif myself_exp == 'bad':
                    if opponent_exp in ['best', 'well']:
                        return 0 # stamina 회복 및 상대의 넘어짐 유도
                    else:
                        return 20 # 상대의 stamina가 낮을 때 반환하는 return이 적을 것으로 예상, configuration 특징 활용해 승부
                else:
                    return 10 # bad, worst 상태가 될 때까지 stamina를 지속적으로 소모함
    # ================================================================================= for tug_of_war game
import random
from . import participant as part

class computer(part.Participant):
    def __init__(self):
        super().__init__('Computer', 0)

    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles): # return should be the number of marbles bet
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        if(my_current_marbles > 7) :
            temp = list(range(1, int(my_current_marbles/4), 2))
            temp = temp[random.randint(0, len(temp) - 1)]
            temp += round((random.uniform(0, 70) + 30) / 100)
        else:
            temp = random.randint(0, my_current_marbles)
        return temp

    def declare_statement_strategy(self, playground_marbles):
        answer = bool(round((random.uniform(0, 70) + 30)/100))
        self.__statement = answer
        return answer
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        if self.position == 0:
            self.temp_list = playground_glasses._players_steps.copy()
        length = len(self.temp_list)
        if self.previous_player != 'None' and self.temp_list != []:
            if self.position < length - 1:
                return self.temp_list[self.position]
            else:
                return random.randint(0, 1)
        return random.randint(0, 1)
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        return (0, 0, 0, 12)

    def act_tugging_strategy(self, playground_tug_of_war):
        if playground_tug_of_war.player_expression[self.name] in ['worst', 'bad']:
            return random.randint(1, 3)
        else:
            return random.randint(1, 15)
    # ================================================================================= for tug_of_war game
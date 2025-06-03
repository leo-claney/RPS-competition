import random
from rps-ai import RPSAI

class RandomBot(RPSAI):
    def make_choice(self):
        """
        Make a random choice from the available moves.
        :return: A random move from the list of possible moves.
        """
        return random.choice(['rock', 'paper', 'scissors'])
    
    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)
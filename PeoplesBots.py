import random
from RPSAI import RPSAI
import config as cfg

class MomBotUseUnused(RPSAI):
    """
    A bot that uses the move that was not used in the last round.
    If the last round was a draw, it keeps the same move.
    """
    NAME = "MomBotUseUnused"
    def make_choice(self):
        """
        Use the move that was not used last round.
        :return: The unused move.
        """
        if len(self.own_history) == 0:
            return random.choice(cfg.CHOICES)
        
        own_last_move = self.own_history[-1]
        opp_last_move = self.opp_history[-1]
        if own_last_move == opp_last_move:
            # If the last round was a draw, keep the same move
            return own_last_move
        unused_move = [move for move in cfg.CHOICES if move != own_last_move and move != opp_last_move]
        return unused_move[0] if unused_move else random.choice(cfg.CHOICES)


# class MomBotAggregateStrategies(RPSAI):
#     """
#     A bot that aggregates strategies from other bots.
#     """
#     NAME = "MomBotAggregateStrategies"

#     def __init__(self, bots):
#         super().__init__()
#         self.bots = bots

#     def make_choice(self):
#         """
#         Aggregate strategies from other bots to make a choice.
#         :return: The aggregated move.
#         """
#         bot_idx = random.randint(0, len(self.bots) - 1)
#         return self.bots[bot_idx].make_choice()

#     def update_history(self, own_move, opp_move):
#         """
#         Update the history of moves for all bots.
#         :param own_move: The move made by the AI.
#         :param opp_move: The move made by the opponent.
#         """
#         for bot in self.bots:
#             bot.update_history(own_move, opp_move)
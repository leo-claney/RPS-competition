from RPSAI import RPSAI
import config as cfg
import random

class RollingAveragesBot(RPSAI):
    """
    A bot that uses rolling averages of the opponent's moves to predict their next move.
    """
    NAME = "RollingAveragesBot"

    def __init__(self):
        super().__init__()
        self.opponent_history = []

    def make_choice(self):
        """
        Predict the opponent's next move based on rolling averages.
        :return: The predicted move.
        """
        if not self.opponent_history:
            return random.choice([cfg.ROCK, cfg.PAPER, cfg.SCISSORS])
        
        # Calculate the most common move in the opponent's history
        most_common_move = max(set(self.opponent_history), key=self.opponent_history.count)
        
        # Predict the next move based on the most common move
        if most_common_move == cfg.ROCK:
            return cfg.PAPER  # Paper beats Rock
        elif most_common_move == cfg.PAPER:
            return cfg.SCISSORS  # Scissors beat Paper
        else:
            return cfg.ROCK  # Rock beats Scissors

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)
        self.opponent_history.append(opp_move)

class InverseRollingAveragesBot(RollingAveragesBot):
    """
    A bot that uses inverse rolling averages of the opponent's moves to predict their next move.
    """
    NAME = "InverseRollingAveragesBot"

    def make_choice(self):
        """
        Predict the opponent's next move based on inverse rolling averages.
        :return: The predicted move.
        """
        if not self.opponent_history:
            return random.choice([cfg.ROCK, cfg.PAPER, cfg.SCISSORS])
        
        # Calculate the least common move in the opponent's history
        least_common_move = min(set(self.opponent_history), key=self.opponent_history.count)
        
        # Predict the next move based on the least common move
        if least_common_move == cfg.ROCK:
            return cfg.SCISSORS  # Scissors beat Rock
        elif least_common_move == cfg.PAPER:
            return cfg.ROCK  # Rock beats Paper
        else:
            return cfg.PAPER  # Paper beats Scissors

class ConsistencyBot(RPSAI):
    """
    A bot that uses the opponent's last move to predict their next move.
    """
    NAME = "ConsistencyBot"

    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def make_choice(self):
        """
        Predict the opponent's next move based on their last move.
        :return: The winning move based on their opponents last move.
        """
        if self.last_opponent_move is None:
            return random.choice([cfg.ROCK, cfg.PAPER, cfg.SCISSORS])
        
        # Predict the next move based on the last opponent's move
        if self.last_opponent_move == cfg.ROCK:
            return cfg.PAPER  # Paper beats Rock
        elif self.last_opponent_move == cfg.PAPER:
            return cfg.SCISSORS  # Scissors beat Paper
        else:
            return cfg.ROCK  # Rock beats Scissors

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)
        self.last_opponent_move = opp_move

class ConfidentWinner(RPSAI):
    """
    A bot that uses the same hand if it just won, otherwise it uses the opponent's last move.
    Uses a random move if the last result is unknown or a draw.
    """
    NAME = "ConfidentWinner"

    def __init__(self):
        super().__init__()
        self.last_result = None

    def make_choice(self):
        """
        Predict the next move based on the last result.
        :return: The winning move based on the last result.
        """
        if self.last_result == None:
            return random.choice(cfg.CHOICES)

        elif self.last_result == cfg.WIN:
            return self.own_history[-1]
        elif self.last_result == cfg.LOSS:
            return self.opp_history[-1]
        else:
            return random.choice(cfg.CHOICES)
        

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves and the last result.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)
        self.last_result = self.evaluate_hand(own_move, opp_move)
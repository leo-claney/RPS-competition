from RPSAI import RPSAI
import config as cfg
import random

class RollingAveragesBot(RPSAI):
    """
    A bot that uses rolling averages of the opponent's moves to predict their next move.
    """
    NAME = "RollingAveragesBot"

    def make_choice(self):
        """
        Predict the opponent's next move based on rolling averages.
        :return: The predicted move.
        """
        if not self.opp_history:
            return random.choice(cfg.CHOICES)
        
        # Calculate the most common move in the opponent's history
        most_common_move = max(set(self.opp_history), key=self.opp_history.count)
        
        # Predict the next move based on the most common move
        if most_common_move == cfg.ROCK:
            return cfg.PAPER  # Paper beats Rock
        elif most_common_move == cfg.PAPER:
            return cfg.SCISSORS  # Scissors beat Paper
        else:
            return cfg.ROCK  # Rock beats Scissors

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
        if not self.opp_history:
            return random.choice(cfg.CHOICES)
        
        # Calculate the most common move in the opponent's history
        least_common_move = min(set(self.opp_history), key=self.opp_history.count)
        
        # Predict the next move based on the most common move
        if least_common_move == cfg.ROCK:
            return cfg.PAPER  # Paper beats Rock
        elif least_common_move == cfg.PAPER:
            return cfg.SCISSORS  # Scissors beat Paper
        else:
            return cfg.ROCK  # Rock beats Scissors

class ConsistencyBot(RPSAI):
    """
    A bot that uses the opponent's last move to predict their next move.
    """
    NAME = "ConsistencyBot"

    def make_choice(self):
        """
        Predict the opponent's next move based on their last move.
        :return: The winning move based on their opponents last move.
        """
        if len(self.opp_history) == 0:
            return random.choice(cfg.CHOICES)
        
        # Predict the next move based on the last opponent's move
        if self.opp_history[-1] == cfg.ROCK:
            return cfg.PAPER  # Paper beats Rock
        elif self.opp_history[-1] == cfg.PAPER:
            return cfg.SCISSORS  # Scissors beat Paper
        else:
            return cfg.ROCK  # Rock beats Scissors

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

class UnconfidentWinner(RPSAI):
    """
    This bot uses the same hand if it just lost, otherwise it uses a different move than it just played.
    Uses a random move if the last result is unknown or a draw.
    """
    NAME = "UnconfidentWinner"

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
            return random.choice([move for move in cfg.CHOICES if move != self.own_history[-1]])
        elif self.last_result == cfg.LOSS:
            return self.own_history[-1]
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

class StealerBot(RPSAI):
    """
    A bot that steals the opponent's last move.
    """
    NAME = "StealerBot"

    def make_choice(self):
        """
        Steal the opponent's last move.
        :return: The opponent's last move.
        """
        if not self.opp_history:
            return random.choice(cfg.CHOICES)
        
        return self.opp_history[-1]

class SwitcherBot(RPSAI):
    """
    A bot that switches its move to cycle through the choices
    """
    NAME = "SwitcherBot"

    def __init__(self):
        super().__init__()
        self.last_result = None

    def make_choice(self):
        """
        Switch the move based on the last result.
        :return: The winning move based on the last result.
        """
        if self.last_result is None or self.last_result == cfg.DRAW:
            return random.choice(cfg.CHOICES)
        else:
            # Cycle through the choices
            current_index = cfg.CHOICES.index(self.own_history[-1])
            next_index = (current_index + 1) % len(cfg.CHOICES)
            return cfg.CHOICES[next_index]

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves and the last result.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)
        self.last_result = self.evaluate_hand(own_move, opp_move)

class ReverseSwitcherBot(SwitcherBot):
    """
    A bot that switches its move to cycle through the choices in reverse order.
    """
    NAME = "ReverseSwitcherBot"

    def make_choice(self):
        """
        Switch the move based on the last result in reverse order.
        :return: The winning move based on the last result.
        """
        if self.last_result is None or self.last_result == cfg.DRAW:
            return random.choice(cfg.CHOICES)
        else:
            # Cycle through the choices in reverse order
            current_index = cfg.CHOICES.index(self.own_history[-1])
            next_index = (current_index - 1) % len(cfg.CHOICES)
            return cfg.CHOICES[next_index]
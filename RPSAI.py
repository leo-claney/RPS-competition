from abc import ABC, abstractmethod
import config as cfg

class RPSAI(ABC):
    NAME = "BaseRPSAI"
    def __init__(self):
        self.own_history = []
        self.opp_history = []
        self.name = self.__class__.NAME

    @abstractmethod
    def make_choice(self):
        '''
        Make a choice based on the history of moves.
        This method should be implemented by subclasses.
        '''
        pass

    def update_history(self, own_move, opp_move):
        '''
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        '''
        self.own_history.append(own_move)
        self.opp_history.append(opp_move)

    def evaluate_hand(self, own_move, opp_move):
        '''
        Evaluate the outcome of a hand.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        :return: 1 if AI wins, -1 if AI loses, 0 if it's a draw.
        '''
        if own_move == opp_move:
            return 0
        elif (own_move == cfg.ROCK and opp_move == cfg.SCISSORS) or \
             (own_move == cfg.PAPER and opp_move == cfg.ROCK) or \
             (own_move == cfg.SCISSORS and opp_move == cfg.PAPER):
            return 1
        else:
            return -1


def main():
    print("RPSAI base class is ready to be extended by AI implementations.")
    base_ai = RPSAI()
    result = base_ai.evaluate_hand(cfg.ROCK, cfg.SCISSORS)
    print(f"Evaluating hand: ROCK vs SCISSORS -> Result: {result} (1 means win, -1 means loss, 0 means draw)")

if __name__ == "__main__":
    main()
class RPSAI:
    def __init__(self):
        self.own_history = []
        self.opp_history = []

    @abstractmethod
    def make_choice(self):
        '''''
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
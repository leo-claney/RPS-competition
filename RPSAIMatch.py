import config as cfg
# Import the necessary AI classes
from RPSAI import RPSAI
from SimpleBots import RandomBot, AlwaysPaper, AlwaysRock, AlwaysScissors
from PredictiveBots import *

class RPSAIMatch:
    def __init__(self, player_1, player_2, first_to:int=100):
        """
        Initialize the match with two players and the winning score.
        :param player_1: The first player (AI).
        :param player_2: The second player (AI).
        :param first_to: The number of wins required to win the match.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.first_to = first_to
        self.scores = {player_1.NAME: 0, player_2.NAME: 0}
        self.max_rounds = first_to * 5  # Set a maximum number of rounds to avoid infinite loops

    def play_hand(self, headless=False):
        """
        Play a single hand of Rock-Paper-Scissors between the two players.
        :return: The result of the hand (1 for player 1 win, -1 for player 2 win, 0 for draw).
        """
        move_1 = self.player_1.make_choice()
        move_2 = self.player_2.make_choice()
        if not headless:
            print(f"{self.player_1.NAME} chooses {move_1}, {self.player_2.NAME} chooses {move_2}.")
        result = self.player_1.evaluate_hand(move_1, move_2)
        
        # Update histories
        self.player_1.update_history(move_1, move_2)
        self.player_2.update_history(move_2, move_1)
        
        return result

    def play_match(self, headless=False):
        """
        Play the match until one player reaches the winning score.
        :return: The name of the winning player.
        """
        if not headless:
            print(f"Starting match between {self.player_1.NAME} and {self.player_2.NAME}. First to {self.first_to} wins!")
            print("=================================================================")
            print()
        round_number = 1
        while self.scores[self.player_1.NAME] < self.first_to and self.scores[self.player_2.NAME] < self.first_to and round_number <= self.max_rounds:
            if not headless:
                print(f"Round {round_number}:")
            round_number += 1
            result = self.play_hand(headless=headless)
            if result == 1:
                self.scores[self.player_1.NAME] += 1
                if not headless:
                    print(f"{self.player_1.NAME} wins this hand! Score: {self.scores}")
                    print()
            elif result == -1:
                self.scores[self.player_2.NAME] += 1
                if not headless:
                    print(f"{self.player_2.NAME} wins this hand! Score: {self.scores}")
                    print()
            else:
                if not headless:
                    print("It's a draw! No points awarded.")
                    print()
        if not headless:
            print("=================================================================")
        if round_number > self.max_rounds:
            print(f"Match ended after {self.max_rounds} rounds without a winner.")
            self.scores[self.player_1.NAME] = 0
            self.scores[self.player_2.NAME] = 0
            return None, self.scores
        winner = self.player_1.NAME if self.scores[self.player_1.NAME] >= self.first_to else self.player_2.NAME
        print(f"{winner} wins the match!")
        return winner, self.scores

    def display_scores(self):
        """
        Display the current scores of both players.
        """
        print(f"Scores: {self.player_1.NAME}: {self.scores[self.player_1.NAME]}, {self.player_2.NAME}: {self.scores[self.player_2.NAME]}")

def main():
    print("RPSAIMatch is ready to play a match between two AI players...")
    player_1 = ReverseSwitcherBot()
    player_2 = ConfidentWinner()
    match = RPSAIMatch(player_1, player_2, first_to=20)
    winner = match.play_match(headless=False)
    match.display_scores()

if __name__ == "__main__":
    main()
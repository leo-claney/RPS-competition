from RPSAI import RPSAI
import config as cfg
import random

class AlwaysPaper(RPSAI):
    NAME = "AlwaysPaper"

    def make_choice(self):
        """
        Always choose PAPER.
        :return: The move PAPER.
        """
        return cfg.PAPER

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)

class AlwaysRock(RPSAI):
    NAME = "AlwaysRock"

    def make_choice(self):
        """
        Always choose ROCK.
        :return: The move ROCK.
        """
        return cfg.ROCK

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)

class AlwaysScissors(RPSAI):
    NAME = "AlwaysScissors"

    def make_choice(self):
        """
        Always choose SCISSORS.
        :return: The move SCISSORS.
        """
        return cfg.SCISSORS

    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)

class RandomBot(RPSAI):
    NAME = "RandomBot"
    def make_choice(self):
        """
        Make a random choice from the available moves.
        :return: A random move from the list of possible moves.
        """
        return random.choice(cfg.CHOICES)
    
    def update_history(self, own_move, opp_move):
        """
        Update the history of moves.
        :param own_move: The move made by the AI.
        :param opp_move: The move made by the opponent.
        """
        super().update_history(own_move, opp_move)

def main():
    bot = RandomBot()
    print(f"{bot.NAME} is ready to play!")
    for _ in range(5):  # Simulate 5 rounds
        chosen_move = bot.make_choice()
        print(f"{bot.NAME} chose: {chosen_move}")
        opponent_move = random.choice(cfg.CHOICES)
        print(f"Opponent chose: {opponent_move}")
        update_history = bot.update_history(chosen_move, opponent_move)
        print(f"History updated: {bot.own_history} (own), {bot.opp_history} (opponent)")
        print(f'Bot last move: {bot.own_history[-1]}, Opponent last move: {bot.opp_history[-1]}')

if __name__ == "__main__":
    main()
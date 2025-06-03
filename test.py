import config as cfg
import random

def test_config():
    print("Testing config module...")
    print(cfg.ROCK)
    print(cfg.PAPER)
    print(cfg.SCISSORS)
    print(cfg.WIN)
    print(cfg.LOSS)
    print(cfg.DRAW)
    print(cfg.CHOICES)

def evaluate_hand(own_move, opp_move):
    """
    Evaluate the outcome of a hand.
    :param own_move: The move made by the AI.
    :param opp_move: The move made by the opponent.
    :return: 1 if AI wins, -1 if AI loses, 0 if it's a draw.
    """
    if own_move == opp_move:
        return 0
    elif (own_move == cfg.ROCK and opp_move == cfg.SCISSORS) or \
         (own_move == cfg.PAPER and opp_move == cfg.ROCK) or \
         (own_move == cfg.SCISSORS and opp_move == cfg.PAPER):
        return 1
    else:
        return -1

def test_game(ai_1, ai_2):
    print("Testing game logic...")
    # Placeholder for game logic tests
    # This would typically involve simulating a game between ai_1 and ai_2
    # and checking the results against expected outcomes.
    ai_1_choice = random.choice(cfg.CHOICES)
    ai_2_choice = random.choice(cfg.CHOICES)
    result = evaluate_hand(ai_1_choice, ai_2_choice)
    print(f"AI 1 chose: {ai_1_choice}, AI 2 chose: {ai_2_choice}")
    if result == cfg.WIN:
        print("AI 1 wins!")
    elif result == cfg.LOSS:
        print("AI 2 wins!")
    else:
        print("It's a draw!")

def test_match(ai_1, ai_2, winning_score=17):
    print(f"Testing match between {ai_1} and {ai_2}, first to {winning_score} wins...")
    scores = {ai_1: 0, ai_2: 0}
    while scores[ai_1] < winning_score and scores[ai_2] < winning_score:
        ai_1_choice = random.choice(cfg.CHOICES)
        ai_2_choice = random.choice(cfg.CHOICES)
        result = evaluate_hand(ai_1_choice, ai_2_choice)
        print(f"{ai_1} chose: {ai_1_choice}, {ai_2} chose: {ai_2_choice}")
        if result == cfg.WIN:
            scores[ai_1] += 1
            print(f"{ai_1} gets a point! Current score: {scores[ai_1]} - {scores[ai_2]}")
        elif result == cfg.LOSS:
            scores[ai_2] += 1
            print(f"{ai_2} gets a point! Current score: {scores[ai_1]} - {scores[ai_2]}")
        print()
    print(f"Final scores: {scores}")

if __name__ == "__main__":
    test_config()
    print("Config module test completed.")
    print()
    test_game("RandomBot1", "RandomBot2")  # Replace with actual AI instances
    print("Game logic test completed.")
    print()
    ending_score = 17
    test_match("RandomBot1", "RandomBot2", ending_score)  # Replace with actual AI instances
    print("Match test completed.")


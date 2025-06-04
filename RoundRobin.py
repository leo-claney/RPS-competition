from RPSAIMatch import RPSAIMatch
import config as cfg
from SimpleBots import AlwaysPaper, AlwaysRock, AlwaysScissors, RandomBot
from PredictiveBots import *
from PeoplesBots import MomBotUseUnused #, MomBotAggregateStrategies

def run_tournament(contestants, first_to=100, tournament_headless=False, match_headless=True):
    """
    Run a round-robin tournament between the contestants.
    :param contestants: List of RPSAI contestants.
    :param first_to: The number of wins required to win the match.
    :param tournament_headless: If True, run the tournament without printing match details.
    :param match_headless: If True, run each match without printing hand details.
    :return: A dictionary containing the results of the tournament.
    """
    records = {bot.NAME: {'points': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'score_diff': 0} for bot in contestants}
    for i in range(len(contestants)):
        for j in range(i + 1, len(contestants)):
            player_1 = contestants[i]
            player_2 = contestants[j]
            match = RPSAIMatch(player_1, player_2, first_to)
            winner, scores = match.play_match(headless=match_headless)
            if not tournament_headless:
                print(f"Match between {player_1.NAME} and {player_2.NAME} won by {winner}.")
                print(f'Scores: {scores}')
                print("=================================================================")
                print()
            if winner is None:
                records[player_1.NAME]['draws'] += 1
                records[player_2.NAME]['draws'] += 1
                records[player_1.NAME]['points'] += 1
                records[player_2.NAME]['points'] += 1
            elif winner == player_1.NAME:
                records[player_1.NAME]['wins'] += 1
                records[player_1.NAME]['points'] += 3
                records[player_2.NAME]['losses'] += 1
            else:
                records[player_2.NAME]['wins'] += 1
                records[player_2.NAME]['points'] += 3
                records[player_1.NAME]['losses'] += 1

            records[player_1.NAME]['score_diff'] += scores[player_1.NAME] - scores[player_2.NAME]
            records[player_2.NAME]['score_diff'] += scores[player_2.NAME] - scores[player_1.NAME]
    
    return records

def sort_teams_by_points(records):
    return sorted(
        records.items(),
        key=lambda item: (item[1]['points'], item[1]['score_diff']),
        reverse=True
    )

def sort_teams_by_pos(records):
    return sorted(
        records.items(),
        key=lambda item: (-item[1]['avg_pos'], item[1]['points'], item[1]['score_diff']),
        reverse=True
    )

def multiple_tournaments(contestants, num_tournaments=10, first_to=100, tournament_headless=False, match_headless=True):
    """
    Run multiple tournaments and aggregate the results.
    :param contestants: List of RPSAI contestants.
    :param num_tournaments: Number of tournaments to run.
    :param first_to: The number of wins required to win the match.
    :param tournament_headless: If True, run the tournament without printing match details.
    :param match_headless: If True, run each match without printing hand details.
    :return: A dictionary containing the aggregated results of the tournaments.
    """
    aggregated_records = {bot.NAME: {'points': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'score_diff': 0} for bot in contestants}
    averaged_records = {bot.NAME: {'avg_pos': 0, 'points': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'score_diff': 0} for bot in contestants}
    
    for i in range(num_tournaments):
        print(f"Running tournament {i + 1}/{num_tournaments}...")
        records = run_tournament(contestants, first_to=first_to, tournament_headless=tournament_headless, match_headless=match_headless)
        sorted_records = sort_teams_by_points(records)
        for team_record in sorted_records:
            bot_name, record = team_record
            averaged_records[bot_name]['avg_pos'] += sorted_records.index((bot_name, record)) + 1
            aggregated_records[bot_name]['points'] += record['points']
            aggregated_records[bot_name]['wins'] += record['wins']
            aggregated_records[bot_name]['losses'] += record['losses']
            aggregated_records[bot_name]['draws'] += record['draws']
            aggregated_records[bot_name]['score_diff'] += record['score_diff']
    
    for bot_name, record in averaged_records.items():
        averaged_records[bot_name]['avg_pos'] /= num_tournaments
        averaged_records[bot_name]['points'] = aggregated_records[bot_name]['points'] / num_tournaments
        averaged_records[bot_name]['wins'] = aggregated_records[bot_name]['wins'] / num_tournaments
        averaged_records[bot_name]['losses'] = aggregated_records[bot_name]['losses'] / num_tournaments
        averaged_records[bot_name]['draws'] = aggregated_records[bot_name]['draws'] / num_tournaments
        averaged_records[bot_name]['score_diff'] = aggregated_records[bot_name]['score_diff'] / num_tournaments    

    
    return averaged_records, aggregated_records

def display_results_single(records):
    """
    Display the results of the tournament.
    :param records: The records of the tournament.
    """
    print("Final Results:")
    print("=================================================================")
    print("Records:")
    print("Points\tWins\tLosses\tDraws\tScore Difference --> Bot Name")
    print("------------------------------------------------------------------")
    for team_record in records:
        bot_name, record = team_record
        print(f"{record['points']}\t{record['wins']}\t{record['losses']}\t{record['draws']}\t{record['score_diff']}\t\t --> {bot_name}")

def display_results_multiple(averaged_records, aggregated_records):
    """
    Display the results of multiple tournaments.
    :param averaged_records: The averaged records of the tournaments.
    :param aggregated_records: The aggregated records of the tournaments.
    """
    print("Final Results (Averaged):")
    print("=================================================================")
    print("Averaged Records:")
    print("Avg Pos\tPoints\tWins\tLosses\tDraws\tScore Difference --> Bot Name")
    print("------------------------------------------------------------------")
    for team_record in averaged_records:
        bot_name, record = team_record
        print(f"{record['avg_pos']:.2f}\t{record['points']:.2f}\t{record['wins']:.2f}\t{record['losses']:.2f}\t{record['draws']:.2f}\t{record['score_diff']:.2f}\t --> {bot_name}")
    
    print("\nAggregated Records:")
    print("Points\tWins\tLosses\tDraws\tScore Difference --> Bot Name")
    print("------------------------------------------------------------------")
    for team_record in aggregated_records:
        bot_name, record = team_record
        print(f"{record['points']}\t{record['wins']}\t{record['losses']}\t{record['draws']}\t{record['score_diff']}\t\t --> {bot_name}")
    

def main():
    contestants = [RandomBot(),
                  AlwaysPaper(),
                  AlwaysRock(),
                  AlwaysScissors(),
                  RollingAveragesBot(),
                  InverseRollingAveragesBot(),
                  ConsistencyBot(),
                  ConfidentWinner(),
                  UnconfidentWinner(),
                  StealerBot(),
                  SwitcherBot(),
                  ReverseSwitcherBot(),
                  UseUnused(),
                  MomBotUseUnused()]
    # MomBot1 = MomBotAggregateStrategies(contestants)
    # contestants.append(MomBot1)

    # contestants = [AlwaysPaper(), AlwaysRock(), AlwaysScissors()]

    # Run a single tournament
    # records = run_tournament(contestants, first_to=100, tournament_headless=True, match_headless=True)
    # sorted_records = sort_teams_by_points(records)
    # display_results(sorted_records)
    
    # Run multiple tournaments and aggregate results
    averaged_records, aggregated_records = multiple_tournaments(contestants, num_tournaments=200, first_to=100, tournament_headless=True, match_headless=True)
    sorted_averaged_records = sort_teams_by_pos(averaged_records)
    sorted_aggregated_records = sort_teams_by_points(aggregated_records)
    display_results_multiple(sorted_averaged_records, sorted_aggregated_records)
    
    
if __name__ == "__main__":
    main()

    
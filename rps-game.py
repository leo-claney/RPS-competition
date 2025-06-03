import pygame
import sys

ROCK = 0
PAPER = 1
SCISSORS = 2

def get_winner(player_choice, opponent_choice):
    """Determine the winner of a rock-paper-scissors game."""
    if player_choice == opponent_choice:
        return 0
    elif (player_choice == ROCK and opponent_choice == SCISSORS) or \
         (player_choice == PAPER and opponent_choice == ROCK) or \
         (player_choice == SCISSORS and opponent_choice == PAPER):
        return 1
    else:
        return -1

def draw_all_buttons(screen, rock, paper, scissors, choice=None):
    """Draw all buttons on the screen."""
    screen.fill((66, 200, 245))  # Clear screen
    screen.blit(rock, (50, 50))
    screen.blit(paper, (250, 50))
    screen.blit(scissors, (450, 50))
    if choice:
        if choice == 'rock':
            screen.blit(rock, (250, 250))
        elif choice == 'paper':
            screen.blit(paper, (250, 250))
        elif choice == 'scissors':
            screen.blit(scissors, (250, 250))
    pygame.display.flip()

def main():
    # Initialize Pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Rock Paper Scissors Game")
    screen.fill((66, 200, 245))

    # Load images
    rock = pygame.image.load("rock.png").convert_alpha()
    paper = pygame.image.load("paper.png").convert_alpha()
    scissors = pygame.image.load("scissors.png").convert_alpha()
    rock = pygame.transform.scale(rock, (100, 100))
    paper = pygame.transform.scale(paper, (100, 100))
    scissors = pygame.transform.scale(scissors, (100, 100))

    # Display initial images
    screen.blit(rock, (50, 50))
    screen.blit(paper, (250, 50))
    screen.blit(scissors, (450, 50))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.blit(rock, (50, 50))
            screen.blit(paper, (250, 50))
            screen.blit(scissors, (450, 50))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    draw_all_buttons(screen, rock, paper, scissors, 'rock')
                elif event.key == pygame.K_p:
                    draw_all_buttons(screen, rock, paper, scissors, 'paper')
                elif event.key == pygame.K_s:
                    draw_all_buttons(screen, rock, paper, scissors, 'scissors')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if 50 <= pos[0] <= 150 and 50 <= pos[1] <= 150:
                        draw_all_buttons(screen, rock, paper, scissors, 'rock')
                    elif 250 <= pos[0] <= 350 and 50 <= pos[1] <= 150:
                        draw_all_buttons(screen, rock, paper, scissors, 'paper')
                    elif 450 <= pos[0] <= 550 and 50 <= pos[1] <= 150:
                        draw_all_buttons(screen, rock, paper, scissors, 'scissors')
    pygame.quit()

if __name__ == "__main__":
    main()
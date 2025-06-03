import config as cfg
import random
import pygame

class RPSGame:
    """
    A class to represent the Rock Paper Scissors game.
    param gamemode: The mode of the game (0 for player vs player, 1 for player vs ai, 2 for ai vs ai).
    param ai: A list of AI players. Empty for player vs player mode, contains AI instances for player vs AI or AI vs AI modes.
    param first_to: The number of wins required to win the game.
    """
    def __init__(self, gamemode:int=0, ai:list=None, first_to:int=5):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Rock Paper Scissors Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.choices = [cfg.ROCK, cfg.PAPER, cfg.SCISSORS]
        self.images = self.load_images()
        self.background_color = (66, 200, 245)
        self.gamemode = gamemode
        self.ai = ai
        self.first_to = first_to

    def load_images(self):
        """Load and scale images for the game."""
        images = {
            'rock': pygame.transform.scale(pygame.image.load("rock.png").convert_alpha(), (100, 100)),
            'paper': pygame.transform.scale(pygame.image.load("paper.png").convert_alpha(), (100, 100)),
            'scissors': pygame.transform.scale(pygame.image.load("scissors.png").convert_alpha(), (100, 100))
        }
        return images

    def get_winner(self, player_choice, ai_choice):
        """Determine the winner of the round."""
        if player_choice == ai_choice:
            return config.DRAW
        elif (player_choice == 'rock' and ai_choice == 'scissors') or \
             (player_choice == 'paper' and ai_choice == 'rock') or \
             (player_choice == 'scissors' and ai_choice == 'paper'):
            return config.WIN
        else:
            return config.LOSS

    def welcome_screen(self):
        """Display the welcome screen."""
        self.screen.fill(self.background_color)
        font = pygame.font.Font(None, 36)
        text = font.render("Welcome to Rock Paper Scissors!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(300, 300))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
    
    def pvp(self):
        """Player vs Player mode logic."""
        # Placeholder for player vs player logic
        pass

    def pvAI(self):
        """Player vs AI mode logic."""
        # Placeholder for player vs AI logic
        pass

    def AIvAI(self):
        """AI vs AI mode logic."""
        # Placeholder for AI vs AI logic
        pass

    def play_round(self, player_choice, ai_choice):
        """
        Play a round of the game.
        :param player_choice: The choice made by the player.
        :param ai_choice: The choice made by the AI.
        :return: The result of the round (WIN, LOSS, DRAW).
        """
        return self.get_winner(player_choice, ai_choice)

    def play_game(self):
        """
        Main game loop.
        Handles the game logic based on the selected gamemode.
        """
        self.welcome_screen()
        if self.gamemode == 0:
            self.pvp()
        elif self.gamemode == 1:
            self.pvAI()
        elif self.gamemode == 2:
            self.AIvAI()
        else:
            raise ValueError("Invalid gamemode selected.")



def main():
    """Main function to run the game."""
    game = RPSGame(gamemode=0)  # Change gamemode as needed
    game.play_game()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        # Game logic and rendering would go here

        game.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
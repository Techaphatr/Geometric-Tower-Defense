from DataHandler import database
from EntityHandler import EntityHandler
from Sound import Sound
from Monsters import Monsters
from Troops import Troops
import pygame
import random
import numpy

class run:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.__data_class = database()
        self.__game_states = "Menu"
        self.__difficulty = None
        self.screen = pygame.display.set_mode(self.__data_class.config['Screen_Size'])
        pygame.display.set_caption("Geometric Tower Defense [GTD]")
        pygame.display.set_icon(pygame.image.load("Picture/game_logo.png"))

        self.__play_button = pygame.image.load("Picture/play_button.png")
        self.__play_button_rect = self.__play_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__play_button.get_size()[0]/2,400))
        self.__quit_button = pygame.image.load("Picture/quit_button.png")
        self.__quit_button_rect = self.__quit_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2,500))

        self.__easy = pygame.image.load("Picture/easy_diff.png")
        self.__easy_rect = self.__easy.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__play_button.get_size()[0]/2 - 250,250))
        self.__hard = pygame.image.load("Picture/hard_diff.png")
        self.__hard_rect = self.__hard.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2,250))
        self.__extreme = pygame.image.load("Picture/extreme_diff.png")
        self.__extreme_rect = self.__extreme.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2 + 250,250))

    def __create_grid(self, width=12, height=7):
        empty_grid = "--"
        grid = [[empty_grid for _ in range(width)] for _ in range(height)]

        entrance_y = random.randint(2, height - 3)
        grid[entrance_y][0] = 2
        path_x, path_y = 1, entrance_y
        cd = 1
        while path_x < width - 1:
            if grid[path_y][path_x] == empty_grid:
                grid[path_y][path_x] = "rr"
            path_x += 1

            if path_x < width - 1:
                if cd > 0:
                    cd -= 1
                    continue
                move = random.choice(["up", "down", "right"])
                if move == "up" and path_y > 1:
                    grid[path_y][path_x] = "ul"
                    grid[path_y - 1][path_x] = "ur"
                    path_y -= 1
                    if not bool(random.randint(0,2)):
                        grid[path_y][path_x] = "ud"
                        grid[path_y - 1][path_x] = "ur"
                        path_y -= 1
                elif move == "down" and path_y < height - 2:
                    grid[path_y][path_x] = "dl"
                    grid[path_y + 1][path_x] = "dr"
                    path_y += 1
                    if not bool(random.randint(0,2)):
                        grid[path_y][path_x] = "ud"
                        grid[path_y + 1][path_x] = "dr"
                        path_y += 1
                cd = 1
        grid[path_y][path_x] = 3

        return grid

    def __menu(self):
        title = pygame.font.SysFont('Arial', 50).render('Geometric Tower Defense', False, (0, 0, 0))
        self.screen.blit(title, (self.__data_class.config['Screen_Size'][0]/2 - title.get_size()[0]/2,150))
        self.screen.blit(self.__play_button, self.__play_button_rect)
        self.screen.blit(self.__quit_button, self.__quit_button_rect)

    def __select_mode(self):
        title = pygame.font.SysFont('Arial', 40).render('Select Difficulty', False, (0, 0, 0))
        self.screen.blit(title, (self.__data_class.config['Screen_Size'][0]/2 - title.get_size()[0]/2,150))
        self.screen.blit(self.__easy, self.__easy_rect)
        self.screen.blit(self.__hard, self.__hard_rect)
        self.screen.blit(self.__extreme, self.__extreme_rect)

    def __load_game(self):
        pass

    def __game_over(self):
        pass

    def __reset(self):
        self.__game_states = "Menu"
        self.__difficulty = None
        pass

    def __load(self):
        if self.__game_states == "Menu":
            self.__menu()
        elif self.__game_states == "Gamemode":
            self.__select_mode()
        elif self.__game_states == "Game":
            pass
        elif self.__game_states == "Over":
            pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.__play_button_rect.collidepoint(event.pos) and self.__game_states == "Menu":
                        Sound().click.play()
                        self.__game_states = "Gamemode"
                    elif self.__quit_button_rect.collidepoint(event.pos) and self.__game_states == "Menu":
                        Sound().click.play()
                        running = False
                    elif self.__easy_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
                        Sound().dfficulty_select.play()
                        self.__difficulty = "Easy"
                        self.__game_states = "Game"
                    elif self.__hard_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
                        Sound().dfficulty_select.play()
                        self.__difficulty = "Hard"
                        self.__game_states = "Game"
                    elif self.__extreme_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
                        Sound().dfficulty_select.play()
                        self.__difficulty = "Extreme"
                        self.__game_states = "Game"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        print(f"Reload map: \n{numpy.array(self.__create_grid())}")

            self.screen.fill((255,255,255))
            self.__load()


            pygame.display.update()
        pygame.quit()
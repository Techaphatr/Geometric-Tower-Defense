from DataHandler import database
from EntityHandler import EntityHandler
from Sound import Sound
from Monsters import Monsters
from Troops import Troops
import tkinter as tk
import matplotlib.pyplot as plt
import pygame
import random
import time

class run:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.__data_class = database()
        self.__game_states = "Menu"
        self.__map = []
        self.__map_checkbox = []
        self.__map_path = []
        self.__entrance = None
        self.__exit = None
        self.__difficulty = None
        self.__current_select = None
        self.__match_health = 0
        self.__wave = 0
        self.__coin = 0
        self.__running = True
        self.__is_start = False
        self.__on_wave = False
        self.__load_wave_cd = False
        self.__wave_cd = 0
        self.__sound = Sound()
        self.__sound.menu_theme.play(-1)
        self.__sound.menu_theme.set_volume(0.5)
        self.__background_image = pygame.image.load(self.__data_class.config["Defualt_Img"])
        self.screen = pygame.display.set_mode(self.__data_class.config['Screen_Size'])
        pygame.display.set_caption("Geometric Tower Defense [GTD]")
        pygame.display.set_icon(pygame.image.load("Picture/game_logo.png"))

        self.__play_button = pygame.image.load("Picture/play_button.png")
        self.__play_button_rect = self.__play_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__play_button.get_size()[0]/2,350))
        self.__graph_button = pygame.image.load("Picture/graph_button.png")
        self.__graph_button_rect = self.__graph_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__graph_button.get_size()[0]/2,425))
        self.__quit_button = pygame.image.load("Picture/quit_button.png")
        self.__quit_button_rect = self.__quit_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2,500))

        self.__menu_button = pygame.image.load("Picture/menu_button.png")
        self.__menu_button_rect = self.__menu_button.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__menu_button.get_size()[0]/2,425))

        self.__easy = pygame.image.load("Picture/easy_diff.png")
        self.__easy_rect = self.__easy.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__play_button.get_size()[0]/2 - 250,250))
        self.__hard = pygame.image.load("Picture/hard_diff.png")
        self.__hard_rect = self.__hard.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2,250))
        self.__extreme = pygame.image.load("Picture/extreme_diff.png")
        self.__extreme_rect = self.__extreme.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__quit_button.get_size()[0]/2 + 250,250))

        self.__s1 = pygame.image.load("Picture/slot1.png")
        self.__s1_rect = self.__s1.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__s1.get_size()[0]/2 - 75,self.__data_class.config['Screen_Size'][1] - self.__s1.get_size()[1] - 20))
        self.__s2 = pygame.image.load("Picture/slot2.png")
        self.__s2_rect = self.__s2.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__s2.get_size()[0]/2,self.__data_class.config['Screen_Size'][1] - self.__s1.get_size()[1] - 20))
        self.__s3 = pygame.image.load("Picture/slot3.png")
        self.__s3_rect = self.__s3.get_rect(topleft=(self.__data_class.config['Screen_Size'][0]/2 - self.__s3.get_size()[0]/2 + 75,self.__data_class.config['Screen_Size'][1] - self.__s1.get_size()[1] - 20))

        self.__exit_round = pygame.image.load("Picture/exit_icon.png")
        self.__exit_round_rect = self.__exit_round.get_rect(topleft=(self.__data_class.config['Screen_Size'][0] - self.__exit_round.get_size()[0] - 10, 10))

        self.__bin = pygame.image.load("Picture/bin.png")
        self.__bin_rect = self.__bin.get_rect(topleft=(self.__data_class.config['Screen_Size'][0] - self.__bin.get_size()[0] - 10, self.__data_class.config['Screen_Size'][1] - self.__bin.get_size()[1] - 10))

        self.__time_start = None

    def __create_grid(self, width=12, height=9):
        empty_grid = "-"
        grid = [[empty_grid + str(random.randint(0,2)%2) for _ in range(width)] for _ in range(height)]

        entrance_y = random.randint(2, height - 3)
        grid[entrance_y][0] = 2
        path_x, path_y = 1, entrance_y
        cd = 1
        while path_x < width - 1:
            if grid[path_y][path_x][0] == empty_grid:
                grid[path_y][path_x] = "rr"
            path_x += 1

            if path_x < width - 1:
                if cd > 0:
                    cd -= 1
                    continue
                move = random.choice(["up", "down", "right","up", "down"])
                if move == "up" and path_y > 1:
                    grid[path_y][path_x] = "ul"
                    grid[path_y - 1][path_x] = "ur"
                    path_y -= 1
                    if not bool(random.randint(0,2)) and path_y != 0 and path_y != height-1:
                        grid[path_y][path_x] = "ud"
                        grid[path_y - 1][path_x] = "ur"
                        path_y -= 1
                elif move == "down" and path_y < height - 2:
                    grid[path_y][path_x] = "dl"
                    grid[path_y + 1][path_x] = "dr"
                    path_y += 1
                    if not bool(random.randint(0,2)) and path_y != 0 and path_y != height-1:
                        grid[path_y][path_x] = "ud"
                        grid[path_y + 1][path_x] = "dr"
                        path_y += 1
                cd = 1
        grid[path_y][path_x] = 3
        return grid

    def __menu(self):
        title = pygame.image.load("Picture/game_title.png")
        self.screen.blit(title, (self.__data_class.config['Screen_Size'][0]/2 - title.get_size()[0]/2,50))
        self.screen.blit(self.__play_button, self.__play_button_rect)
        self.screen.blit(self.__quit_button, self.__quit_button_rect)
        self.screen.blit(self.__graph_button, self.__graph_button_rect)

    def __select_mode(self):
        title = pygame.font.SysFont('PromptBold', 60).render('Select Difficulty', False, (255,255,255))
        self.screen.blit(title, (self.__data_class.config['Screen_Size'][0]/2 - title.get_size()[0]/2,150))
        self.screen.blit(self.__easy, self.__easy_rect)
        self.screen.blit(self.__hard, self.__hard_rect)
        self.screen.blit(self.__extreme, self.__extreme_rect)

    def __draw_bg(self):
        """
        draw main part of the game.
        Grid size: x: 50, y: 50
        """
        bg = pygame.image.load("Picture/game_info.png")
        bg_tag = bg.get_rect(topleft=(0,0))
        self.screen.blit(bg, bg_tag)

        self.screen.blit(self.__s1, self.__s1_rect)
        self.screen.blit(self.__s2, self.__s2_rect)
        self.screen.blit(self.__s3, self.__s3_rect)

        Health = pygame.font.SysFont('PromptBold', 40).render(str(self.__match_health), False, (255,226,226))
        self.screen.blit(Health, (150,50))
        Wave = pygame.font.SysFont('PromptBold', 40).render("WAVE  "+str(self.__wave), False, (255,255,255))
        self.screen.blit(Wave, (430,50))
        coin = pygame.font.SysFont('PromptBold', 40).render("COIN: "+str(self.__coin), False, (255,255,0))
        self.screen.blit(coin, (coin.get_size()[0] + 20,self.__data_class.config["Screen_Size"][1] - coin.get_size()[1] - 30))

        width = len(self.__map[0]) * 50
        height = len(self.__map) * 50
        picture_path = "Picture/path_bg/"
        current_pos_x = (self.__data_class.config['Screen_Size'][0] - width)/2
        current_pos_y = (self.__data_class.config['Screen_Size'][1] - height)/2
        for row in self.__map:
            for grid in row:
                grid = str(grid)
                name = grid.split("-")
                name = name[len(name)-1]
                tmp_img = pygame.image.load(picture_path+ "Path" + name + ".png")
                tmp_img_rect = tmp_img.get_rect(topleft=(current_pos_x,current_pos_y))
                if not self.__is_start and str(name) in ("0", "1"):
                    self.__map_checkbox.append(tmp_img_rect)
                if not self.__is_start and not (str(name) in ("0", "1", "2")):
                    self.__map_path.append(tmp_img_rect)
                if not self.__is_start and str(name) == "2":
                    self.__entrance = tmp_img_rect
                if not self.__is_start and str(name) == "3":
                    self.__exit = tmp_img_rect
                current_pos_x += 50
                self.screen.blit(tmp_img, tmp_img_rect)
            current_pos_x = (self.__data_class.config['Screen_Size'][0] - width)/2
            current_pos_y += 50

    def __draw_troops(self):
        for troops in EntityHandler.TROOP_LIST:
            tmp = troops.variance
            tmp_rect = tmp.get_rect(center=troops.position)
            self.screen.blit(tmp, tmp_rect)

    def __placing_troop(self, mouse_pos):
        nearest_grid = None
        dis = 25
        for grid in self.__map_checkbox:
            if database.distance(grid.center, mouse_pos) < 25:
                if database.distance(grid.center, mouse_pos) < dis:
                    nearest_grid = grid
                    dis = database.distance(grid.center, mouse_pos)
        if nearest_grid != None:
            if not self.__current_select.isbuy:
                self.__current_select.isbuy = True
                self.__sound.buy.play()
                self.__coin -= 10
                self.__data_class.save("type", self.__current_select.type)
            status, troop2 = EntityHandler.check_merge(nearest_grid.center[0], nearest_grid.center[1])
            if database.distance(self.__entrance.center, nearest_grid.center) < 60:
                self.__data_class.save("position", "near entrance")
            elif database.distance(self.__exit.center, nearest_grid.center) < 60:
                self.__data_class.save("position", "near exit")
            else:
                for grid in self.__map_path:
                    if database.distance(grid.center, nearest_grid.center) < 60:
                        self.__data_class.save("position", "near path")
                        break
            if status:
                if troop2.current_stage == self.__current_select.current_stage and \
                    troop2.type == self.__current_select.type:
                    troop2.upgrade()
                    self.__sound.sparkle.play()
                    self.__sound.peep.play()
                    self.__current_select = None
                return
            else:
                self.__current_select.x = nearest_grid.center[0]
                self.__current_select.y = nearest_grid.center[1]
                EntityHandler.TROOP_LIST.append(self.__current_select)
                self.__current_select.value = True
                self.__current_select = None
                self.__sound.peep.play()

    def __nearest_troop(self, mouse_pos):
        nearest_grid = None
        dis = 25
        for grid in EntityHandler.TROOP_LIST:
            if database.distance(grid.position, mouse_pos) < 25:
                if database.distance(grid.position, mouse_pos) < dis:
                    nearest_grid = grid
                    dis = database.distance(grid.position, mouse_pos)
        if nearest_grid != None:
            EntityHandler.TROOP_LIST.remove(nearest_grid)
            self.__sound.peep.play()
            self.__current_select = nearest_grid
            self.__current_select.value = False

    def __sell_troop(self):
        self.__coin += 10 * self.__current_select.current_stage
        self.__sound.trash.play()
        self.__current_select = None

    def __clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def __monster_walk(self, mons : Monsters):
        path = None
        dis = 1000
        for i in mons.path:
            if database.distance(mons.position, i.center) < dis:
                path = i
                dis = database.distance(mons.position, i.center)
        if path.center[0] - mons.x > 0:
            mons.x += mons.current_speed
            self.__clamp(mons.x, 0, path.centerx)
        if path.center[1] - mons.y > 0:
            mons.y += mons.current_speed
            self.__clamp(mons.y, 0, path.centery)
        if path.center[1] - mons.y < 0:
            mons.y -= mons.current_speed
            self.__clamp(mons.y, 0, path.centery)
        if database.distance(mons.position, path.center) <= 10:
            mons.path.remove(path)
        if database.distance(mons.position, self.__exit.center) <= 10:
            mons.died()
            self.__sound.hurt.play()
            self.__match_health -= mons.health

    def __draw_monster(self):
        for troops in EntityHandler.MONSTER_LIST:
            self.__monster_walk(troops)
            tmp = troops.variance
            tmp_rect = tmp.get_rect(center=troops.position)
            self.screen.blit(tmp, tmp_rect)

    def __attack(self):
        for i in EntityHandler.TROOP_LIST:
            current_time = time.time()
            if current_time - i.last_attack >= i.cooldown:
                check = EntityHandler.fire(i, i.type)
                if check:
                    self.__sound.hit.play()
                    i.last_attack = current_time
                    self.__coin += 1

    def __next_wave(self):
        self.__wave += 1
        self.__time_start = time.time()
        self.__on_wave = True
        self.__coin += 9 + random.randint(1,3) * self.__wave
        for _ in range(3 + 1*self.__wave):
            Monsters(self.__entrance.center, random.randint(0, self.__clamp(random.randint(0, self.__wave) - 4, 1, 10)), self.__map_path.copy())
            time.sleep(0.01)

    def __load_game(self):
        self.__draw_bg()
        self.__is_start = True
        self.screen.blit(self.__exit_round, self.__exit_round_rect)
        self.__draw_troops()
        self.__draw_monster()
        self.__attack()
        if self.__match_health <= 0:
            if self.__game_states == "Game":
                self.__sound.over.play()
            self.__game_over()
            self.__game_states = "Over"
        if self.__game_states == "Over":
            return
        if EntityHandler.check_win() and self.__on_wave:
            self.__on_wave = False
        if EntityHandler.check_win() and not self.__on_wave:
            if not self.__load_wave_cd:
                self.__load_wave_cd = True
                self.__wave_cd = time.time()
                if self.__time_start != None:
                    self.__data_class.save("time", round(time.time() - self.__time_start))
            if time.time() - self.__wave_cd >= 5:
                self.__load_wave_cd = False
                self.__next_wave()
                self.__sound.next_wave.play()

    def __game_over(self):
        rect_surface = pygame.Surface(self.__data_class.config["Screen_Size"], pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 200))
        self.screen.blit(rect_surface, (0, 0))
        title = pygame.font.SysFont('PromptBold', 140).render('Game Over', False, (255,255,255))
        self.screen.blit(title, (self.__data_class.config['Screen_Size'][0]/2 - title.get_size()[0]/2,150))
        self.screen.blit(self.__menu_button, self.__menu_button_rect)

    def __reset(self):
        if self.__wave > 0:
            self.__data_class.save("highscore", self.__wave)
        self.__entrance = None
        self.__exit = None
        self.__game_states = "Menu"
        self.__map = []
        self.__map_checkbox = []
        self.__map_path = []
        self.__difficulty = None
        self.__current_select = None
        self.__match_health = 0
        self.__wave = 0
        self.__coin = 0
        self.__time_start = None
        self.__is_start = False
        self.__on_wave = False
        self.__load_wave_cd = False
        self.__wave_cd = 0
        self.__background_image = pygame.image.load(self.__data_class.config["Defualt_Img"])
        self.__sound.game_theme.stop()
        self.__sound.menu_theme.play(-1)
        self.__sound.menu_theme.set_volume(0.5)
        EntityHandler.reset()

    def __load(self):
        bg_rect = self.__background_image.get_rect(topleft=(0,0))
        self.screen.blit(self.__background_image, bg_rect)
        if self.__game_states == "Menu":
            self.__menu()
        elif self.__game_states == "Gamemode":
            self.__select_mode()
        elif self.__game_states in ("Game", "Over"):
            self.__load_game()
            self.__ingame_hover(pygame.mouse)

    def __select_difficulty(self):
        self.__data_class.save("difficulty", self.__difficulty)
        self.__sound.menu_theme.stop()
        self.__game_states = "Game"
        self.__sound.start_wave.play()
        self.__sound.start_wave.set_volume(0.5)
        rect_surface = pygame.Surface(self.__data_class.config["Screen_Size"], pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 200))
        self.screen.blit(rect_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(100)

        dirty_rects = []
        for i in range(1, 34):
            tmp = pygame.image.load(f"Picture/Battle_cutscene/Untitled_Artwork-{str(i)}.png")
            tmp_rect = tmp.get_rect(topleft=(0, 0))
            dirty_rects.append(tmp_rect)
            self.screen.blit(tmp, tmp_rect)
            pygame.display.update(dirty_rects)
            bg_rect = self.__background_image.get_rect(topleft=(0,0))
            self.screen.blit(self.__background_image, bg_rect)
            self.__select_mode()
            rect_surface = pygame.Surface(self.__data_class.config["Screen_Size"], pygame.SRCALPHA)
            rect_surface.fill((0, 0, 0, 200))
            self.screen.blit(rect_surface, (0, 0))
            dirty_rects.clear()
            pygame.time.delay(40)

        pygame.time.delay(100)
        self.__sound.game_theme.play(-1)
        self.__sound.game_theme.set_volume(0.3)
        self.__background_image = pygame.image.load(self.__data_class.config["Ingame_Img"])
        self.__match_health = 100
        self.__coin = 15
        self.__wave = 0

    def __mouse_interact(self, event):
        if self.__play_button_rect.collidepoint(event.pos) and self.__game_states == "Menu":
            self.__sound.click.play()
            self.__game_states = "Gamemode"
        elif self.__quit_button_rect.collidepoint(event.pos) and self.__game_states == "Menu":
            self.__sound.click.play()
            self.__running = False
        elif self.__easy_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
            self.__sound.dfficulty_select.play()
            self.__difficulty = "Easy"
            self.__map = self.__create_grid(width=15)
            self.__select_difficulty()
        elif self.__hard_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
            self.__sound.dfficulty_select.play()
            self.__difficulty = "Hard"
            self.__map = self.__create_grid(width=12)
            self.__select_difficulty()
        elif self.__extreme_rect.collidepoint(event.pos) and self.__game_states == "Gamemode":
            self.__sound.dfficulty_select.play()
            self.__difficulty = "Extreme"
            self.__map = self.__create_grid(width=10)
            self.__select_difficulty()
        elif self.__exit_round_rect.collidepoint(event.pos) and self.__game_states == "Game":
            self.__reset()
        elif self.__s1_rect.collidepoint(event.pos) and self.__game_states == "Game":
            if self.__coin >= 10:
                self.__sound.select_slot.play()
                self.__current_select = Troops(stage=0, typ="Circle", pos=event.pos)
            else:
                self.__sound.cancel.play()
        elif self.__s2_rect.collidepoint(event.pos) and self.__game_states == "Game":
            if self.__coin >= 10:
                self.__sound.select_slot.play()
                self.__current_select = Troops(stage=0, typ="Triangle", pos=event.pos)
            else:
                self.__sound.cancel.play()
        elif self.__s3_rect.collidepoint(event.pos) and self.__game_states == "Game":
            if self.__coin >= 10:
                self.__sound.select_slot.play()
                self.__current_select = Troops(stage=0, typ="Square", pos=event.pos)
            else:
                self.__sound.cancel.play()
        elif self.__menu_button_rect.collidepoint(event.pos) and self.__game_states == "Over":
            self.__reset()
        if self.__game_states == "Game":
            if self.__current_select != None:
                if self.__bin_rect.collidepoint(event.pos):
                    self.__sell_troop()
                else:
                    self.__placing_troop(pygame.mouse.get_pos())
            else:
                self.__nearest_troop(pygame.mouse.get_pos())

    def __check_hover(self, mouse : pygame.mouse):
        if self.__easy_rect.collidepoint(mouse.get_pos()) and self.__game_states == "Gamemode":
            self.__background_image = pygame.image.load(self.__data_class.config["Hover_Img"][0])
        elif self.__hard_rect.collidepoint(mouse.get_pos()) and self.__game_states == "Gamemode":
            self.__background_image = pygame.image.load(self.__data_class.config["Hover_Img"][1])
        elif self.__extreme_rect.collidepoint(mouse.get_pos()) and self.__game_states == "Gamemode":
            self.__background_image = pygame.image.load(self.__data_class.config["Hover_Img"][2])
        elif self.__game_states == "Gamemode":
            self.__background_image = pygame.image.load(self.__data_class.config["Defualt_Img"])

    def __ingame_hover(self, mouse : pygame.mouse):
        if self.__current_select != None:
            tmp = self.__current_select.variance
            tmp_rect = tmp.get_rect(center=mouse.get_pos())
            self.screen.blit(tmp, tmp_rect)
            self.screen.blit(self.__bin, self.__bin_rect)

    def run(self):
        self.__running = True
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__reset()
                    self.__running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.__mouse_interact(event)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__map = self.__create_grid(width=15)

            self.__check_hover(pygame.mouse)
            self.screen.fill((255,255,255))
            self.__load()

            pygame.display.update()
        pygame.quit()
import pygame

class Sound:
    __instance = None

    def __new__(cls):
        if Sound.__instance == None:
            Sound.__instance = super().__new__(cls)
        return Sound.__instance

    def __init__(self):
        pygame.mixer.init()
        mixer = pygame.mixer
        self.click = mixer.Sound("Asset/Sound/click.wav")
        self.dfficulty_select = mixer.Sound("Asset/Sound/select_diff.wav")
        self.menu_theme = mixer.Sound("Asset/Sound/menu_bgm.mp3")
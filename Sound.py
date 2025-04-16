import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        mixer = pygame.mixer
        self.click = mixer.Sound("Asset/Sound/click.wav")
        self.dfficulty_select = mixer.Sound("Asset/Sound/select_diff.wav")
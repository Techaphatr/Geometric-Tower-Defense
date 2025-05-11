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
        self.peep = mixer.Sound("Asset/Sound/pop.wav")
        self.next_wave = mixer.Sound("Asset/Sound/next_wave.wav")
        self.start_wave = mixer.Sound("Asset/Sound/start_wave.wav")
        self.cancel = mixer.Sound("Asset/Sound/Cancel.wav")
        self.select_slot = mixer.Sound("Asset/Sound/select_slot.wav")
        self.menu_theme = mixer.Sound("Asset/Sound/menu_bgm.mp3")
        self.game_theme = mixer.Sound("Asset/Sound/RiseAbovetheFlame.mp3")
        self.trash = mixer.Sound("Asset/Sound/trash.wav")
        self.buy = mixer.Sound("Asset/Sound/purch.wav")
        self.sparkle = mixer.Sound("Asset/Sound/sparkle.wav")
        self.hurt = mixer.Sound("Asset/Sound/hurt.wav")
        self.hit = mixer.Sound("Asset/Sound/hit.wav")
        self.over = mixer.Sound("Asset/Sound/over.wav")
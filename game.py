import pygame
from menu import Menu
from game_screen import GameScreen
from customization_screen import CustomizationScreen
from options_screen import OptionsScreen
from levels_screen import LevelsScreen
from winning_screen import WinningScreen
from losing_screen import LosingScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 529))
        pygame.display.set_caption('Eng Lyfe')
        self.clock = pygame.time.Clock()
        self.music_playing = True
        self.music_volume = 0.5
        # set the music file and start playing it
        self.set_and_start_music("TitleScreenMusic - 66 The Noise's Jam-Packed Radical Anthem.mp3")
        
        # set the screen as running and set the current screen to None
        self.is_running = True
        self.current_screen = None
        # create the screens ->  pass self as the third argument
        self.menu = Menu(self.screen, self)
        self.game_screen = GameScreen(self.screen, self)
        self.customization_screen = CustomizationScreen(self.screen, self)
        self.levels_screen = LevelsScreen(self.screen, self)
        self.options_screen = OptionsScreen(self.screen, self) 

        self.character=1
        
        #non-menu screens -> leads back to main menu
        #self.winning_screen = WinningScreen(self.screen, self)
        #self.losing_screen = LosingScreen(self.screen, self)
    
        # set the current screen to the menu to begin the game
        self.set_current_screen(self.menu)
        # start the main game loop
        self.run()



    def run(self):
        while self.is_running:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    self.current_screen.handle_key_press(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.current_screen.handle_mouse_click(pygame.mouse.get_pos())
                elif event.type == pygame.USEREVENT:
                    self.return_to_menu()
            # update and draw the current screen
            self.current_screen.update()
            self.current_screen.draw()
            # update the display
        
            pygame.display.flip()
            # limit the frame rate to 60 FPS
            self.clock.tick(60)
            #set the music volume
            self.set_music_volume(self.music_volume)
            


    def set_current_screen(self, screen):
        #if self.current_screen and hasattr(self.current_screen, 'stop_music'):
            #self.current_screen.stop_music()
        self.current_screen = screen
        # self.current_screen.music_playing = True




    def set_and_start_music(self, filename):
        # stop any currently playing music
        pygame.mixer.music.stop()
        # load the new music
        self.music = pygame.mixer.music.load(filename)
        # set the volume
        pygame.mixer.music.set_volume(self.music_volume)
        # start playing the music
        pygame.mixer.music.play(-1)
        self.music_playing = True


    # start playing the music
    def start_music(self):
        pygame.mixer.music.play(-1)
        self.music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_playing = False


    # function to set the music volume
    def set_music_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
        self.music_volume = volume


    # function to return back to the main menu and start its music again
    def return_to_menu(self):
        self.set_current_screen(self.menu)
        self.set_and_start_music("TitleScreenMusic - 66 The Noise's Jam-Packed Radical Anthem.mp3")
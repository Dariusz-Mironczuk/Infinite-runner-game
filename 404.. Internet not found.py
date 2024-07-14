import pygame
import sys
from random import randint

game_version = 'version 1.0.0'
game_icon = pygame.image.load('assets/icon_img.png')
pygame.display.set_icon(game_icon)

class Game:
    def __init__(self):
        pygame.init()

        # Display options
        pygame.display.set_caption('404.. internet not found...')
        self.display = pygame.display.set_mode((800, 400))
        self.clock = pygame.time.Clock()
        self.x = 1
        self.title_screen_value = 0
        self.game_active = True
        self.time_played = 1
        self.score = 0
        self.last_score_update = pygame.time.get_ticks()

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 2000)

        self.ground_enemy_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ground_enemy_timer,400)

        self.air_enemy_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.air_enemy_timer, 500)

        # Game font
        self.main_font = pygame.font.Font(
            "assets/orange_juice.ttf",
            50)
        self.main_font_score = pygame.font.Font(
            "assets/orange_juice.ttf",
            40)
        self.main_font_instructions = pygame.font.Font(
            "assets/orange_juice.ttf",
            25)
        self.main_font_version = pygame.font.Font(
            "assets/orange_juice.ttf",
            20)
        self.main_font_game_over = pygame.font.Font(
            "assets/orange_juice.ttf",
            100)
        self.main_font_control_instructions = pygame.font.Font(
            "assets/orange_juice.ttf",
            30)


        # Game text on screen
        self.title_screen = self.main_font.render('404.. internet not found...', False, (255, 215, 0))
        self.title_instructions = self.main_font_instructions.render('(Press the "SPACE_BAR" to start and play)', False,
                                                                     (255, 255, 255))
        self.version = self.main_font_version.render(f'{game_version}', False, (128, 128, 128))
        self.game_over_txt = self.main_font_game_over.render('Game over!', False, (255, 0, 0))
        self.control_instructions_text_W = self.main_font_control_instructions.render('"W" - Jump', False,
                                                                                      (128, 128, 128))
        self.control_instructions_text_D = self.main_font_control_instructions.render(' "D" - Right', False,
                                                                                      (128, 128, 128))
        self.control_instructions_text_A = self.main_font_control_instructions.render('"A" - Left', False,
                                                                                      (128, 128, 128))
        self.play_again = self.main_font_instructions.render('Press the "SPACE_BAR" to play again', False,
                                                             (255, 255, 255))

        # Assets to use
        self.background = pygame.image.load(
            "assets/background.png").convert()
        self.ground = pygame.image.load(
            "assets/walk_way.png").convert_alpha()

        # Ground enemy assets
        self.ground_enemy_img1 = pygame.image.load(
            "assets/ground_enemy.png").convert_alpha()
        self.ground_enemy_img2 = pygame.image.load("assets/ground_enemy1.png")
        self.ground_enemy = [self.ground_enemy_img1, self.ground_enemy_img2]
        self.ground_enemy_index = 0
        self.ground_enemy_img = self.ground_enemy[self.ground_enemy_index]
        self.enemy_rect_list = []

        # Air enemy assets
        self.air_enemy_img1 = pygame.image.load(
            "assets/air_enemy.png").convert_alpha()
        self.air_enemy_img2 = pygame.image.load("assets/air_enemy1.png")
        self.air_enemy = [self.air_enemy_img1, self.air_enemy_img2]
        self.air_enemy_index = 0
        self.air_enemy_img = self.air_enemy[self.air_enemy_index]


        # Player assets
        self.player_gravity = 0
        self.player_pressing_d = False
        self.player_pressing_a = False
        self.player_walk1 = pygame.image.load(
            "assets/player_run1.png").convert_alpha()
        self.player_walk2 = pygame.image.load(
            "assets/player_run2.png").convert_alpha()
        self.player_walk3 = pygame.image.load(
            "assets/player_run3.png").convert_alpha()
        self.player_walk4 = pygame.image.load(
            "assets/player_run4.png").convert_alpha()
        self.player_walk5 = pygame.image.load(
            "assets/player_run5.png").convert_alpha()
        self.player_walk6 = pygame.image.load(
            "assets/player_run6.png").convert_alpha()
        self.player_walk7 = pygame.image.load(
            "assets/player_run7.png").convert_alpha()
        self.player_walk8 = pygame.image.load(
            "assets/player_run8.png").convert_alpha()
        self.player_walk = [self.player_walk1, self.player_walk2, self.player_walk3, self.player_walk4,
                            self.player_walk5, self.player_walk6, self.player_walk7, self.player_walk8]
        self.player_jump3 = pygame.image.load(
            "assets/player_jump3.png").convert_alpha()
        self.player_jump4 = pygame.image.load(
            "assets/player_jump4.png").convert_alpha()
        self.player_jump5 = pygame.image.load(
            "assets/player_jump5.png").convert_alpha()
        self.player_jump6 = pygame.image.load(
            "assets/player_jump6.png").convert_alpha()
        self.player_jump7 = pygame.image.load(
            "assets/player_jump7.png").convert_alpha()
        self.player_jump8 = pygame.image.load(
            "assets/player_jump8.png").convert_alpha()
        self.player_jump = [self.player_jump3, self.player_jump4,
                            self.player_jump5, self.player_jump6, self.player_jump7, self.player_jump8]
        self.player_death1 = pygame.image.load("assets/player_death1.png").convert_alpha()
        self.player_death2 = pygame.image.load("assets/player_death2.png").convert_alpha()
        self.player_death3 = pygame.image.load("assets/player_death3.png").convert_alpha()
        self.player_death4 = pygame.image.load("assets/player_death4.png").convert_alpha()
        self.player_death5 = pygame.image.load("assets/player_death5.png").convert_alpha()
        self.player_death = [self.player_death1, self.player_death2, self.player_death3, self.player_death4, self.player_death5]
        self.player_stand = pygame.image.load(
            "assets/player_stand1.png").convert_alpha()
        self.player_index = 0
        self.player_index_jump = 0
        self.player_death_index = 0
        self.player_img = self.player_walk[self.player_index]

        self.player_rect = self.player_img.get_rect(bottomleft=(35, 354))

    def player_animation(self):
        keys = pygame.key.get_pressed()

        if self.player_rect.bottom < 354:
            self.player_index_jump += 0.12
            if self.player_index_jump >= len(self.player_jump):
                self.player_img = self.player_jump8
                self.player_index_jump = -1
            self.player_img = self.player_jump[int(self.player_index_jump)]

        # Animation of the player character
        if keys[pygame.K_d] and self.player_rect.bottom >= 354:
            self.player_index_jump = 0
            self.player_index += 0.10
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.player_img = self.player_walk[int(self.player_index)]

        if keys[pygame.K_a] and self.player_rect.bottom >= 354:
            self.player_index_jump = 0
            self.player_index += 0.10
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.player_img = self.player_walk[int(self.player_index)]

        if not self.game_active:
            if self.player_death_index <= len(self.player_death) - 1:
                self.player_death_index += 0.10
                self.player_img = self.player_death[int(self.player_death_index)]
            else:
                self.player_img = self.player_death[-1]

        if self.game_active:
            if not keys[pygame.K_a] and not keys[pygame.K_d] and self.player_rect.bottom >= 354:
                self.player_index_jump = 0
                self.player_img = self.player_stand

    def update_score_text(self):
        self.score_text = self.main_font_score.render(f'Score: {self.score}', False, (255, 215, 0))
        self.score_rect = self.score_text.get_rect(topleft=(10, 5))
        self.display.blit(self.score_text, self.score_rect)

    def score(self):
        self.current_time = pygame.time.get_ticks()
        self.score_ammount = self.main_font_score.render(f'Score: {self.current_time}', False, (255, 215, 0))
        self.score_rect = self.score_ammount.get_rect(topleft=(10, 5))
        self.display.blit(self.score_ammount, self.score_rect)

    def enemy_spawn(self):
        if randint(0, 2):
            new_enemy_rect = self.ground_enemy_img.get_rect(bottomleft=(randint(800, 1250), 354))
            self.enemy_rect_list.append(new_enemy_rect)
        else:
            new_enemy_rect = self.air_enemy_img.get_rect(bottomleft=(randint(800, 1250), 154))
            self.enemy_rect_list.append(new_enemy_rect)

    def enemy_movemnt(self):
        for enemy_rect in self.enemy_rect_list:
            enemy_rect.x -= 5
            if enemy_rect.bottom == 354:
                self.display.blit(self.ground_enemy_img, enemy_rect)
            else:
                self.display.blit(self.air_enemy_img, enemy_rect)

        self.enemy_rect_list = [enemy for enemy in self.enemy_rect_list if enemy.x > -170]

    # Game Loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.title_screen_value == 0:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.title_screen_value = 1

                # Player restarting the game after losing
                if not self.game_active and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_active = True
                        self.player_death_index = 0
                        self.score = 0  # Reset the score
                        self.enemy_rect_list.clear()  # Clear enemy list on restart
                        self.player_rect.bottomleft = (35, 354)

                # Player jumping pressing 'w'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.player_rect.bottom >= 354 and self.game_active:
                        self.player_gravity = -20

                # Player movement to the right pressing 'd'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.player_pressing_d = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player_pressing_d = False

                # Player movement to the left pressing 'a'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player_pressing_a = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player_pressing_a = False

                # Timer for enemy logic
                if event.type == self.obstacle_timer and self.title_screen_value == 1:

                    self.enemy_spawn()

                if event.type == self.ground_enemy_timer:
                    self.ground_enemy_index = (self.ground_enemy_index + 1) % 2
                    self.ground_enemy_img = self.ground_enemy[self.ground_enemy_index]

                if event.type == self.air_enemy_timer:
                    self.air_enemy_index = (self.air_enemy_index + 1) % 2
                    self.air_enemy_img = self.air_enemy[self.air_enemy_index]

            if self.game_active:
                if self.title_screen_value == 0:
                    # Drawing assets to the screen
                    self.display.blit(self.background, (0, -70))
                    self.display.blit(self.ground, (0, 60))
                    self.player_animation()  # Player animation
                    self.display.blit(self.player_img, self.player_rect)

                    # Drawing text to the screen
                    self.display.blit(self.title_screen, (170, 192))
                    self.display.blit(self.title_instructions, (200, 240))
                    self.display.blit(self.version, (700, 380))

                else:
                    self.player_death_index = 0
                    # Drawing assets to the screen
                    self.display.blit(self.background, (0, -70))
                    self.display.blit(self.ground, (0, 60))

                    # Drawing player on game to display
                    self.player_gravity += 1
                    self.player_rect.y += self.player_gravity
                    if self.player_rect.bottom >= 354:
                        self.player_rect.bottom = 354
                    self.player_animation()  # Player animation
                    self.display.blit(self.player_img, self.player_rect)

                    # Player movement left and right
                    if self.player_pressing_d:
                        self.player_rect.x += 8
                    if self.player_pressing_a:
                        self.player_rect.x -= 5

                    # Drawing enemies in the game to display
                    self.enemy_movemnt()

                    # Drawing text to the screen
                    self.update_score_text()
                    if self.time_played == 1:
                        self.display.blit(self.control_instructions_text_W, (640, 5))
                        self.display.blit(self.control_instructions_text_D, (640, 35))
                        self.display.blit(self.control_instructions_text_A, (640, 65))

                    # Checking collisions with all enemies
                    for enemy_rect in self.enemy_rect_list:
                        if self.player_rect.colliderect(enemy_rect):
                            self.game_active = False
                        else:
                            self.score += 1




            # If the player loses, this will show up
            else:
                # Drawing assets to the screen
                self.display.blit(self.background, (0, -70))
                self.display.blit(self.ground, (0, 60))
                self.player_animation()

                # Drawing player on the game to display
                self.player_gravity += 1
                self.player_rect.y += self.player_gravity
                if self.player_rect.bottom >= 354:
                    self.player_rect.bottom = 354
                self.display.blit(self.player_img, self.player_rect)

                # Drawing text to the screen
                self.display.blit(self.game_over_txt, (170, 140))
                self.display.blit(self.play_again, (217, 365))

                # Game logic stuff
                self.time_played = 0

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()


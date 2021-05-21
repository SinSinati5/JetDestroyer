import random
import pygame
import sys
from pathlib import Path

pygame.init()
score = 0
ending_num = 0
user_text = ""
user_text1 = ""

class Object:
    def __init__(self):
        self.ran = random.randint(0,2)
        if self.ran == 0:
            self.obj = pygame.transform.scale(pygame.image.load("object1.png"), (50, 50))
            self.objrect = self.obj.get_rect()
        if self.ran == 1:
            self.obj = pygame.transform.scale(pygame.image.load("object2.png"), (50, 50))
            self.objrect = self.obj.get_rect()
        if self.ran == 2:
            self.obj = pygame.transform.scale(pygame.image.load("object3.png"), (50, 50))
            self.objrect = self.obj.get_rect()





if True:
        f1 = open("settings.txt", "r")
        f = f1.read()
        start_point = f.find("sts")
        end_point = f.find("ens")
        if len(f[start_point + 3: end_point]) > 0:
            start_speed = int(f[start_point + 3: end_point])
        else:
            start_speed = 2
        f1.close()

        f1 = open("settings.txt", "r")
        f = f1.read()
        start_point = f.find("sms")
        end_point = f.find("ems")
        if len(f[start_point + 3: end_point]) > 0:
            move_set = int(f[start_point + 3: end_point])
        else:
            move_set = 0
        f1.close()
        """
        1 = hold to move 
        0 = press to move
        """










o_speed = [0, 2]

size = width, height = 800, 480
white = 255, 255, 255
screen = pygame.display.set_mode(size)
speed = [0, 0]

background = pygame.transform.scale(pygame.image.load("background.png"), (800, 480))
backgroundrect = background.get_rect()

jet = pygame.transform.scale(pygame.image.load("Jet_image.png"), (50, 50))
jetrect = jet.get_rect()

jet1 = pygame.transform.scale(pygame.image.load("Jet_image.png"), (800, 480))
jetrect1 = jet1.get_rect()

x = "w"
jetrect = jetrect.move(375, 430)
screen.blit(background, backgroundrect)
pygame.display.flip()
ast1 = Object()


pygame.display.set_icon(jet)
pygame.display.set_caption("JetDestroyer")

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0



enc = 0

home_num = 0

home_back = pygame.transform.scale(pygame.image.load("home_back.jpg"), (800, 480))
home_backrect = home_back.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.event.get()
    move1 = [230, 100]
    move2 = [348, 250]
    move3 = [295, 320]
    if home_num == 0:
        ending_num = 0
        mouse = pygame.mouse.get_pos()
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font1.render("JetDestroyer", True, "dark red", "white")

        font3 = pygame.font.Font('freesansbold.ttf', 50)
        text3 = font3.render("Settings", True, "dark red", "white")

        font2 = pygame.font.Font('freesansbold.ttf', 50)
        text2 = font2.render("Play", True, "dark red", "white")


        text2rect = text2.get_rect()
        text2rect = text2rect.move(move2)
        text3rect = text3.get_rect()
        text3rect = text3rect.move(move3)

        text1rect = text1.get_rect()
        text1rect = text1rect.move(move1)
        screen.blit(home_back, home_backrect)
        screen.blit(jet1, jetrect1)
        screen.blit(text1, text1rect)
        screen.blit(text2, text2rect)
        screen.blit(text3, text3rect)
        pygame.event.get()
        if 348 < mouse[0] <454 and 250 < mouse[1] < 300 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(70)
            ending_num = 0
            score = 0
            home_num = 1
        if 395 < mouse[0] < 509 and 320 < mouse[1] < 370 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(70)
            home_num = 2

    if home_num == 1:
        pygame.event.get()
        f1 = open("settings.txt", "r")
        f = f1.read()
        start_point = f.find("sts")
        end_point = f.find("ens")
        if len(f[start_point + 3: end_point]) > 0:
            start_speed = int(f[start_point + 3: end_point])
        else:
            start_speed = 2
        f1.close()

        f1 = open("settings.txt", "r")
        f = f1.read()
        start_point = f.find("sms")
        end_point = f.find("ems")
        if len(f[start_point + 3: end_point]) > 0:
            move_set = int(f[start_point + 3: end_point])
        f1.close()
        """
        1 = hold to move 
        0 = press to move
        """
        if ending_num == 0:
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("Score = " + str(score), True, "black")
            textrect = text.get_rect()
            mov = [10,10]
            textrect = textrect.move(mov)

            time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            if score == 5:
                ast2 = Object()
            if score == 10:
                ast3 = Object()
            if score == 51:
                ast4 = Object()



            if score == 5 and a1 == 0:
                o_speed[1] = 3
                a1 = 1
            if score == 10 and a2 == 0:
                o_speed[1] = 4
                a2 = 1
            if score == 18 and a3 == 0:
                o_speed[1] = 5
                a3 = 1
            if score == 27 and a4 == 0:
                o_speed[1] = 6
                a4 = 1
                speed[0]+=1
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                if move_set == 0:
                    if a4 == 0:
                        speed[0] = -int(start_speed)
                        a4 = 1
                    else:
                        if speed[0] > 0:
                            speed[0] = -speed[0]
                        else:
                            speed[0] = speed[0]

                if move_set == 1:
                    speed[0] = -start_speed
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                if move_set == 0:
                    if a4 == 0:
                        speed[0] = int(start_speed)
                        a4 = 1
                    else:
                        if speed[0] > 0:
                            speed[0] = speed[0]
                        else:
                            speed[0] = -speed[0]
                if move_set == 1:
                    speed[0] = start_speed
            if jetrect.left < 0 or jetrect.right > 800:
                speed[0] = -speed[0]
            if ast1.objrect.bottom > 600:
                score+=1
                point = ast1.objrect.left
                ast1.objrect = ast1.objrect.move(random.randint(point * -1, 750 - point), -550)
            if score > 5:
                if ast2.objrect.bottom > 600:
                    score+=1
                    point = ast2.objrect.left
                    ast2.objrect = ast2.objrect.move(random.randint(point * -1, 750 - point), -550)
            if score > 10:
                if ast3.objrect.bottom > 600:
                    score+=1
                    point = ast3.objrect.left
                    ast3.objrect = ast3.objrect.move(random.randint(point * -1, 750 - point), -550)
            if score > 51:
                if ast4.objrect.bottom > 600:
                    score+=1
                    point = ast4.objrect.left
                    ast4.objrect = ast4.objrect.move(random.randint(point * -1, 750 - point), -550)



            screen.blit(background, backgroundrect)
            pygame.time.wait(3)
            jetrect = jetrect.move(speed)
            ast1.objrect = ast1.objrect.move(o_speed)
            if score > 5:
                ast2.objrect = ast2.objrect.move(o_speed)
            if score > 10:
                ast3.objrect = ast3.objrect.move(o_speed)
            if score > 51:
                ast4.objrect = ast4.objrect.move(o_speed)
            screen.blit(jet, jetrect)
            screen.blit(text, textrect)
            screen.blit(ast1.obj, ast1.objrect)
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        mouse = pygame.mouse.get_pos()
        if score > 5:
            screen.blit(ast2.obj, ast2.objrect)
            if pygame.Rect.colliderect(ast2.objrect, jetrect) == True:
                ending_num = 1
                end_text = font1.render("Game Over : " + str(score), True, "red")
                end_textrect = end_text.get_rect()
                mov = [10, 10]
                end_textrect = textrect.move(mov)

                font2 = pygame.font.Font('freesansbold.ttf', 50)
                text2 = font2.render("Home", True, "dark red", "white")
                mov[1] = 80
                text2rect = text2.get_rect()
                text2rect = text2rect.move(mov)
                font3 = pygame.font.Font('freesansbold.ttf', 50)
                text3 = font3.render("Play", True, "dark red", "white")
                mov[1] = 150
                text3rect = text3.get_rect()
                text3rect = text3rect.move(mov)


                o_speed[1] = 2
                screen.blit(background, backgroundrect)
                screen.blit(end_text, end_textrect)
                screen.blit(text2, text2rect)
                while True:
                    if 10 < mouse[0] < 110 and 80 < mouse[1] < 130 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 0
                        ending_num = 0
                        break

                    if 10 < mouse[0] < 110 and 150 < mouse[1] < 200 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 1
                        ending_num = 0
                        break
                    pygame.display.flip()

        if score > 10:
            screen.blit(ast3.obj, ast3.objrect)
            if pygame.Rect.colliderect(ast3.objrect, jetrect) == True:
                ending_num = 1
                end_text = font1.render("Game Over : " + str(score), True, "red")
                end_textrect = end_text.get_rect()
                mov = [10, 10]
                end_textrect = textrect.move(mov)

                font2 = pygame.font.Font('freesansbold.ttf', 50)
                text2 = font2.render("Home", True, "dark red", "white")
                mov[1] = 80
                text2rect = text2.get_rect()
                text2rect = text2rect.move(mov)

                font3 = pygame.font.Font('freesansbold.ttf', 50)
                text3 = font3.render("Play", True, "dark red", "white")
                mov[1] = 150
                text3rect = text3.get_rect()
                text3rect = text3rect.move(mov)


                o_speed[1] = 2
                screen.blit(background, backgroundrect)
                screen.blit(end_text, end_textrect)
                screen.blit(text2, text2rect)
                while True:
                    print(1)
                    if 10 < mouse[0] < 110 and 80 < mouse[1] < 130 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 0
                        ending_num = 0
                        break

                    if 10 < mouse[0] < 110 and 150 < mouse[1] < 200 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 1
                        ending_num = 0
                        break
                    pygame.display.flip()

        if score > 51:
            screen.blit(ast4.obj, ast4.objrect)
            if pygame.Rect.colliderect(ast4.objrect, jetrect) == True:
                ending_num = 1
                end_text = font1.render("Game Over : " + str(score), True, "red", "white")
                end_textrect = end_text.get_rect()
                mov = [10, 10]
                end_textrect = textrect.move(mov)

                font2 = pygame.font.Font('freesansbold.ttf', 50)
                text2 = font2.render("Home", True, "dark red", "white")
                mov[1] = 80
                text2rect = text2.get_rect()
                text2rect = text2rect.move(mov)
                font3 = pygame.font.Font('freesansbold.ttf', 50)
                text3 = font3.render("Play", True, "dark red", "white")
                mov[1] = 150
                text3rect = text3.get_rect()
                text3rect = text3rect.move(mov)


                o_speed[1] = 2
                screen.blit(background, backgroundrect)
                screen.blit(end_text, end_textrect)
                screen.blit(text2, text2rect)
                while True:
                    pygame.event.wait()
                    if 10 < mouse[0] < 110 and 80 < mouse[1] < 130 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 0
                        ending_num = 0
                        break

                    if 10 < mouse[0] < 110 and 150 < mouse[1] < 200 and pygame.mouse.get_pressed()[0]:
                        pygame.time.wait(70)
                        home_num = 1
                        ending_num = 0
                        break
                    pygame.display.flip()

        if pygame.Rect.colliderect(ast1.objrect, jetrect) == True:
            pygame.event.get()
            ending_num = 1
            end_text = font1.render("Game Over : " + str(score), True, "red")
            end_textrect = end_text.get_rect()

            font2 = pygame.font.Font('freesansbold.ttf', 50)
            text2 = font2.render("Home", True, "dark red", "white")
            mov[1] = 80
            text2rect = text2.get_rect()
            text2rect = text2rect.move(mov)

            font3 = pygame.font.Font('freesansbold.ttf', 50)
            text3 = font3.render("Play", True, "dark red", "white")
            mov[1] = 150
            text3rect = text3.get_rect()
            text3rect = text3rect.move(mov)
            o_speed[1] = 0
            screen.blit(background, backgroundrect)
            screen.blit(end_text, end_textrect)
            screen.blit(text2, text2rect)
            screen.blit(text3, text3rect)
            while True:
                if 10 < mouse[0] < 149 and 80 < mouse[1] < 130 and pygame.mouse.get_pressed()[0]:
                    pygame.time.wait(70)
                    home_num = 0
                    ending_num = 0
                    break

                if 10 < mouse[0] < 116 and 150 < mouse[1] < 200 and pygame.mouse.get_pressed()[0]:
                    pygame.time.wait(70)
                    home_num = 1
                    ending_num = 0
                    break
                pygame.display.flip()


    """
    "settings"
    """
    if home_num == 2:
        mouse = pygame.mouse.get_pos()
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font1.render("JetDestroyer", True, "dark red", "white")

        font2 = pygame.font.Font('freesansbold.ttf', 50)
        text2 = font2.render("Starting Speed", True, "dark red", "white")

        font3 = pygame.font.Font('freesansbold.ttf', 50)
        text3 = font3.render("Movement Mode", True, "dark red", "white")

        move2[0] = 200
        text2rect = text2.get_rect()
        text2rect = text2rect.move(move2)

        lmo = [180, 320]
        text3rect = text3.get_rect()
        text3rect = text3rect.move(lmo)

        text1rect = text1.get_rect()
        text1rect = text1rect.move(move1)
        screen.blit(home_back, home_backrect)
        screen.blit(jet1, jetrect1)
        screen.blit(text1, text1rect)
        screen.blit(text2, text2rect)
        screen.blit(text3, text3rect)

        pygame.event.get()
        if 200 < mouse[0] < 589 and 250 < mouse[1] < 300 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(300)
            home_num = 3
        if 180 < mouse[0] < 569 and 320 < mouse[1] < 370 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(300)
            home_num = 4
    if home_num == 3:
        mouse = pygame.mouse.get_pos()
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font1.render(user_text, True, "dark red", "white")

        font2 = pygame.font.Font('freesansbold.ttf', 50)
        text2 = font2.render("Home", True, "dark red", "white")

        move2[0] = 337
        text2rect = text2.get_rect()
        text2rect = text2rect.move(move2)

        move1[0] = 350
        text1rect = text1.get_rect()
        text1rect = text1rect.move(move1)
        screen.blit(home_back, home_backrect)
        screen.blit(jet1, jetrect1)
        screen.blit(text1, text1rect)
        screen.blit(text2, text2rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
        if 337 < mouse[0] < 476 and 250 < mouse[1] < 300 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(300)
            f = Path('settings.txt').read_text()
            f1 = open('settings.txt', "w+")
            start_point = f.find("sts")
            end_point = f.find("ens")
            final_text = f[:start_point + 3] + user_text + f[end_point:]
            f1.write(final_text)
            f1.close()
            home_num = 0
    if home_num == 4:
        mouse = pygame.mouse.get_pos()
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font1.render(user_text1, True, "dark red", "white")

        font2 = pygame.font.Font('freesansbold.ttf', 50)
        text2 = font2.render("Home", True, "dark red", "white")

        move2[0] = 337
        text2rect = text2.get_rect()
        text2rect = text2rect.move(move2)

        font3 = pygame.font.Font('freesansbold.ttf', 50)
        text3 = font3.render("0 = Press To Move", True, "dark red", "white")

        lmo = [190, 320]
        text3rect = text3.get_rect()
        text3rect = text3rect.move(lmo)

        font4 = pygame.font.Font('freesansbold.ttf', 50)
        text4 = font4.render("1 = Hold To Move", True, "dark red", "white")

        lmo = [200, 370]
        text4rect = text4.get_rect()
        text4rect = text4rect.move(lmo)

        text1rect = text1.get_rect()
        text1rect = text1rect.move(move1)
        screen.blit(home_back, home_backrect)
        screen.blit(jet1, jetrect1)
        screen.blit(text1, text1rect)
        screen.blit(text3, text3rect)
        screen.blit(text4, text4rect)
        screen.blit(text2, text2rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text1 = user_text1[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text1 += event.unicode
        if 337 < mouse[0] < 476 and 250 < mouse[1] < 300 and pygame.mouse.get_pressed()[0]:
            pygame.time.wait(300)
            f = Path('settings.txt').read_text()
            f1 = open('settings.txt', "w+")
            start_point = f.find("sms")
            end_point = f.find("ems")
            final_text1 = f[:start_point + 3] + user_text1 + f[end_point:]
            f1.write(final_text1)
            f1.close()
            home_num = 0

    pygame.display.flip()
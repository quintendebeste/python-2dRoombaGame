import pygame as pg
import math
class Player:
    def __init__(self, name, x, y, radius, color, WINDOW, player_images_off, player_images_on, player_images):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.WINDOW = WINDOW 
        self.images_off = player_images_off
        self.images_on = player_images_on      
        self.images = player_images
        self.facing = self.images[0]  

    def move(self, dx, dy):
        if dx == 0 and dy == 0:
            self.facing = self.facing
        elif dx > 0:
            self.facing = self.images[3]
        elif dx < 0:
            self.facing = self.images[2]
        elif dy > 0:
            self.facing = self.images[1]
        elif dy < 0:
            self.facing = self.images[0]

        self.x += dx
        self.y += dy

    def draw(self):
        self.WINDOW.blit(self.facing, (self.x - (self.radius), self.y - (self.radius)))

    def handle_collision(player, block):

        closest_x = max(block.left, min(player.x, block.right))
        closest_y = max(block.top, min(player.y, block.bottom))
        distance = math.sqrt((player.x - closest_x)**2 + (player.y - closest_y)**2)
        
        if distance < player.radius:
            overlap_x = player.radius - abs(player.x - closest_x)
            overlap_y = player.radius - abs(player.y - closest_y)
            
            if overlap_x < overlap_y:
                if player.x < closest_x:
                    player.x -= overlap_x
                else:
                    player.x += overlap_x
            else:
                if player.y < closest_y:
                    player.y -= overlap_y
                else:
                    player.y += overlap_y

class Block:
    def __init__(self, x, y, width, height,WINDOW):
        self.rect = pg.Rect(x, y, width, height)
        self.WINDOW = WINDOW
        self.top = y
        self.left = x
        self.bottom = y + height
        self.right = x + width

    def draw(self,color):
        pg.draw.rect(self.WINDOW, color, self.rect)

class Button:
    def __init__(self, image, pressed_image, x, y, width, height,WINDOW):
        self.hover = False
        self.image = image
        self.pressed_image = pressed_image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.WINDOW = WINDOW

    def draw(self):
        if self.hover:
            self.WINDOW.blit(self.pressed_image, (self.x, self.y))
        else:
            self.WINDOW.blit(self.image, (self.x, self.y))

    def handle_collision(self):
        mouse = pg.mouse.get_pos()
        if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.y+self.height:
            self.hover = True
            return True
        else:
            self.hover = False
            return False
        
class Battery:
    def __init__(self, x, y,WINDOW, battery_images):
        self.x = x
        self.y = y
        self.WINDOW = WINDOW
        self.images = battery_images
        self.active_image = self.images[0]

    def battery_life(self, battery_life):
        if battery_life == 1:
            self.facing = self.images[0]
        elif battery_life == 2:
            self.facing = self.images[1]
        elif battery_life == 3:
            self.facing = self.images[2]
        elif battery_life == 4:
            self.facing = self.images[3]
        elif battery_life == 5:
            self.facing = self.images[4]

    def draw(self):
        self.WINDOW.blit(self.facing, (self.x, self.y))

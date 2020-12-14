import pygame #импорт библиотеки
from dataclasses import dataclass 
pygame.init()
win_width=800 #ширина окна
win_height=600 #высота окна
fps=60
display=(win_width,win_height) #размеры окна
background=(255, 0, 0)
hero_x=0 #координата х персонажа
hero_y=450 #координата y персонажа
hero_speed=0.2 #скорость персонажа
hero_image_number=0
isJump=False
jump=0
dt=0
#переменные для создания уровня
level_platform_wight=32
level_platform_height=32
platform_color="#B22222"
clock=pygame.time.Clock() #управляющая кадрами в секунду
game_over=False #конец игры    
screen=pygame.display.set_mode((display)) #устанавливаем размер экрана
pygame.display.set_caption("Supernatural Quest") #даем название игры
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon) #установка иконы игры
hero_image=pygame.image.load("dean1.2.png") #загрузка картинки персонажа
hero_images_right=[pygame.image.load("dean1.4.png"), pygame.image.load("dean1.8.png"),pygame.image.load("dean1.9.png")]
hero_images_left=[pygame.image.load("dean1.5.png"),pygame.image.load("dean1.6.png"),pygame.image.load("dean1.7.png")]
background_image=pygame.image.load("background.png") #загружаем фон
level = [
        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "                         ", 
        "                         ",     
        "          ----           ",
        "                         ",
        "  -----------            ",
        "                         ",
        "                         ",
        "             -----       ",
        "     -----               ",]
def blockcreating(level):
    x=y=0 # координаты
    for i in level: # вся строка
        for j in i: # каждый символ
            if j=="-":
                    #создаем блок, заливаем его цветом и рисуем его
                block = pygame.Surface((level_platform_wight,level_platform_height))
                block.fill(pygame.Color(platform_color))
                screen.blit(block,(x,y))
            x+=level_platform_wight #блоки платформы ставятся на ширине блоков
        y+=level_platform_height    #то же самое и с высотой
        x=0                   #на каждой новой строчке начинаем с нуля
@dataclass
class Jump:
    isJump:bool
    jump:float
    def update(self,isSpace,hero_y,dt):
        if not(self.isJump):
            if isSpace:
                self.isJump=True     
                self.jump=0.5    
        else:
            hero_y-=self.jump*dt
            self.jump-=0.001*dt         
            if hero_y>win_height-150:    
                self.isJump=False
                self.jump=0   
        return hero_y
jumping=Jump(False,0)                  

while not game_over:
    for event in pygame.event.get(): #смотрим каждое событие из списка всех событий
        if event.type==pygame.QUIT: #проверяем, является ли тип события типом выхода из игры (событие:конец игры)
            game_over=True
            break
    screen.blit(background_image,(0,0))
    blockcreating(level)
    keys=pygame.key.get_pressed() #список нажатых клавиш клавиатуры
    if keys[pygame.K_RIGHT] and hero_x<win_width-80: #перемещение персонажа вправо
        hero_x+=hero_speed*dt
        hero_image_number+=1
        screen.blit(hero_images_right[hero_image_number//21],(hero_x,hero_y))
    elif keys[pygame.K_LEFT] and hero_x>0: #перемещение персонажа влево
        hero_x-=hero_speed*dt 
        hero_image_number+=1
        screen.blit(hero_images_left[hero_image_number//21],(hero_x,hero_y))
    else:
        hero_image_number=0  
        screen.blit(hero_image,(hero_x,hero_y))
    hero_y=jumping.update(keys[pygame.K_SPACE], hero_y, dt)
    if hero_image_number>fps-1:
        hero_image_number=0    
            #расположение персонажа в соответсвии с координатами
    pygame.display.update() #обновляем окно 
    dt=clock.tick(fps) #рисуются 60 кадров в секунду    
pygame.quit()

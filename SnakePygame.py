import sys, pygame, random

screen_width = 600
screen_height = 600

grid_size = 20
grid_width = screen_width / grid_size
grid_height = screen_height / grid_size

light_green = (0,170,140)
dark_green = (0,140,120)
food_color = (255,255,0)
snake_color = (0,0,0)

up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)

class FOOD: 
    def __init__(self):
        self.position = (0,0)
        self.color = food_color
        self.random_position()
    def random_position(self):
        self.position = (random.randint(0, grid_width-1)*grid_size, random.randint(0, grid_height-1)*grid_size)
    def draw(self, surface):
        rect = pygame.Rect((self.position[0],self.position[1]),(grid_size,grid_size))
        pygame.draw.rect(surface,self.color,rect)






def drawGrid(surface):
    for y in range (0,int(grid_height)):
        for x in range (0,int(grid_width)):
            if (x+y) % 2 == 0:
                light = pygame.Rect((x * grid_size , y * grid_size), (grid_size,grid_size))
                pygame.draw.rect(surface,light_green,light)
            else:
                dark = pygame.Rect((x * grid_size, y * grid_size), (grid_size,grid_size))
                pygame.draw.rect(surface,dark_green,dark)




def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_height,screen_width))
    font = pygame.font.SysFont("arial", 20, True, True)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    food = FOOD()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawGrid(surface)
        food.draw(surface)
        screen.blit(surface,(0,0))
        pygame.display.update()

main()


     

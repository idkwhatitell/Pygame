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

class SNAKE:
    def __init__(self):
        self.positions = [((screen_width/2), (screen_height/2))]
        self.lenght = 1
        self.direction = random.choice([up,down,left,right])
        self.color = snake_color
        self.score = 0
    def draw(self,surface):
        for p in self.positions:
            rect = pygame.Rect((p[0],p[1]),(grid_size,grid_size))
            pygame.draw.rect(surface,self.color,rect)
    def move(self):
        current = self.positions[0]
        x,y = self.direction
        new = ((current[0] + (x * grid_size)), (current[1] + (y * grid_size)))

        if new[0] in range (0,screen_width) and new[1] in range (0,screen_height) and not new in self.positions[2:]:
            self.positions.insert(0,new)
            if len(self.positions) > self.lenght:
                self.positions.pop()
        else:
            self.reset()
    def reset(self):
        self.lenght = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up,down,left,right])
        self.score = 0
    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.turn(up)
                elif event.key == pygame.K_s:
                    self.turn(down)
                elif event.key == pygame.K_d:
                    self.turn(right)
                elif event.key == pygame.K_a:
                    self.turn(left)

    def turn(self,direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction







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
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20, True, True)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    food = FOOD()
    snake = SNAKE()

    while True: 
        clock.tick(10)
        snake.handle_keys()
        snake.move()
        drawGrid(surface)
        if snake.positions [0] == food.position:
            snake.lenght += 1
            snake.score += 1
            food.random_position() 
        food.draw(surface)
        snake.draw(surface)
        screen.blit(surface,(0,0))
        score_text = font.render("Score {0}".format(snake.score), True,(0,0,0))
        screen.blit(score_text,(10,10))
        pygame.display.update()

main()


     

from circleshape import *
from constants import *

class Textbox(CircleShape):
    def __init__(self, x, y, text):
        super().__init__(x, y, TEXT_SIZE)
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = text

    def draw(self, screen):
        text_surface = self.my_font.render(self.text , False , 'white')
        screen.blit(text_surface, (self.position.x , self.position.y))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.kill()



    

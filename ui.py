import pygame

class UI:
    @staticmethod
    def draw_status(screen, x, y, hp, buff, name):
        font = pygame.font.SysFont('Arial', 18, bold=True)
        name_txt = font.render(name, True, (0,0,0))
        screen.blit(name_txt, (x - name_txt.get_width()//2, y - 60))
        
        pygame.draw.rect(screen, (100, 100, 100), (x-50, y+40, 100, 10))
        pygame.draw.rect(screen, (50, 200, 50), (x-50, y+40, max(0, hp), 10))
        
        if buff > 0:
            buff_txt = font.render(f"ATK +{buff}", True, (200, 0, 0))
            screen.blit(buff_txt, (x - buff_txt.get_width()//2, y + 55))
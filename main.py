import pygame
from engine import GameEngine
from card import draw_card

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Card Battle - Reiniciar")
clock = pygame.time.Clock()

font_name = pygame.font.SysFont('Arial', 20, bold=True)
font_ui = pygame.font.SysFont('Consolas', 15, bold=True)
font_big = pygame.font.SysFont('Arial', 70, bold=True)

engine = GameEngine()
btn_end = pygame.Rect(720, 350, 140, 50)
btn_restart = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50)

def draw_pokemon_vitals(x, y, hp, name, status, color, is_enemy=False):
    display_hp = max(0, hp)
    pygame.draw.ellipse(screen, (10, 10, 15), (x-50, y+30, 100, 20)) 
    pygame.draw.circle(screen, color, (x, y), 45)
    
    name_surf = font_name.render(name, True, (255,255,255))
    screen.blit(name_surf, (x - name_surf.get_width()//2, y - 85))
    
    hp_txt = font_ui.render(f"HP: {display_hp}/100", True, (200, 255, 200) if display_hp > 30 else (255, 100, 100))
    screen.blit(hp_txt, (x - hp_txt.get_width()//2, y - 60))
    
    if status["turnos"] > 0:
        tipo = "DEBUFF" if is_enemy else "BUFF ATK"
        cor = (100, 150, 255) if is_enemy else (100, 255, 100)
        val = status["atk_debuff"] if is_enemy else status["atk_buff"]
        status_txt = font_ui.render(f"[{tipo} +{val}] {status['turnos']}T", True, cor)
        screen.blit(status_txt, (x - status_txt.get_width()//2, y + 55))

while True:
    mouse = pygame.mouse.get_pos()
    screen.fill((20, 20, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if engine.game_over:
                if btn_restart.collidepoint(mouse):
                    engine.reset() # Reinicia tudo
            elif engine.is_player_turn:
                if btn_end.collidepoint(mouse):
                    engine.is_player_turn = False
                    pygame.time.set_timer(pygame.USEREVENT, 600)
                else:
                    for c in engine.hand[:]:
                        if c.get("rect") and c["rect"].collidepoint(mouse): 
                            engine.play_card(c)
        
        if event.type == pygame.USEREVENT:
            pygame.time.set_timer(pygame.USEREVENT, 0)
            if not engine.game_over: engine.enemy_turn()

    # Desenho do Campo
    draw_pokemon_vitals(700, 160, engine.enemy_hp, engine.p2['nome'], engine.status_enemy, (200, 60, 60), True)
    draw_pokemon_vitals(200, 260, engine.player_hp, engine.p1['nome'], engine.status_player, (60, 180, 60))

    # Cartas
    if engine.is_player_turn and not engine.game_over:
        for i, c in enumerate(engine.hand):
            x_pos = 100 + i * 185
            draw_card(screen, x_pos, 410, c, pygame.Rect(x_pos, 410, 135, 150).collidepoint(mouse), engine.energy)

    # Interface Lateral
    if not engine.game_over:
        pygame.draw.rect(screen, (50, 50, 80), btn_end, border_radius=10)
        screen.blit(font_name.render("PASSAR", True, (255,255,255)), (745, 362))
        pygame.draw.circle(screen, (255, 215, 0), (50, 370), 25)
        screen.blit(font_name.render(str(engine.energy), True, (0,0,0)), (43, 358))
        screen.blit(font_ui.render("PP", True, (255,215,0)), (43, 400))

    # Overlay de Fim de Jogo
    if engine.game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        screen.blit(overlay, (0,0))
        
        res = "VITÓRIA!" if engine.enemy_hp <= 0 else "DERROTA!"
        res_surf = font_big.render(res, True, (255,255,255))
        screen.blit(res_surf, (WIDTH//2 - res_surf.get_width()//2, HEIGHT//2 - 80))
        
        # Botão Jogar Novamente
        color_btn = (100, 255, 100) if btn_restart.collidepoint(mouse) else (50, 150, 50)
        pygame.draw.rect(screen, color_btn, btn_restart, border_radius=10)
        txt_restart = font_name.render("JOGAR NOVAMENTE", True, (255,255,255))
        screen.blit(txt_restart, (btn_restart.centerx - txt_restart.get_width()//2, btn_restart.centery - 10))

    pygame.display.flip()
    clock.tick(60)
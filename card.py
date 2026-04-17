import pygame

def draw_card(screen, x, y, card, is_hovered, energy):
    rect = pygame.Rect(x, y, 135, 150)
    card["rect"] = rect
    bg_color = (50, 50, 70) if is_hovered else (35, 35, 45)
    if energy < card["cost"]: bg_color = (25, 25, 25)
    
    pygame.draw.rect(screen, bg_color, rect, border_radius=12)
    pygame.draw.rect(screen, (200, 200, 200), rect, 2, border_radius=12)
    
    f_name = pygame.font.SysFont('Arial', 11, bold=True)
    f_val = pygame.font.SysFont('Arial', 14, bold=True)
    
    # Nome
    name_txt = f_name.render(card["name"].upper(), True, (255, 255, 255))
    screen.blit(name_txt, (x + (135 - name_txt.get_width())//2, y + 15))
    
    # Custo
    pygame.draw.circle(screen, (255, 215, 0), (x + 115, y + 130), 12)
    screen.blit(f_val.render(str(card["cost"]), True, (0,0,0)), (x + 110, y + 122))
    
    # Rótulo de Tipo
    cores = {"attack": (255, 100, 100), "buff": (100, 255, 100), "debuff": (100, 150, 255)}
    labels = {"attack": f"DANO: {card['value']}", "buff": f"ATK +{card['value']}", "debuff": f"ALVO -{card['value']}"}
    
    txt = f_val.render(labels[card["type"]], True, cores[card["type"]])
    screen.blit(txt, (x + 15, y + 70))
    screen.blit(f_name.render("3 TURNOS" if card["type"] != "attack" else "", True, (150,150,150)), (x+15, y+90))
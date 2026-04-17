import asyncio
import random
from pokemon_data import pokemon_aleatorio, buscar_detalhes_movimento

class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.player_hp, self.enemy_hp = 100, 100
        self.status_player = {"atk_buff": 0, "turnos": 0}
        self.status_enemy = {"atk_debuff": 0, "turnos": 0}
        self.energy = 3
        self.is_player_turn = True
        self.game_over = False
        
        # Carregamento inicial
        loop = asyncio.get_event_loop()
        self.p1 = loop.run_until_complete(pokemon_aleatorio())
        self.p2 = loop.run_until_complete(pokemon_aleatorio())
        
        self.hand = []
        self.novo_turno()

    def novo_turno(self):
        if self.game_over: return
        self.energy = 3
        self.is_player_turn = True
        
        if self.status_player["turnos"] > 0:
            self.status_player["turnos"] -= 1
            if self.status_player["turnos"] == 0: self.status_player["atk_buff"] = 0
            
        if self.status_enemy["turnos"] > 0:
            self.status_enemy["turnos"] -= 1
            if self.status_enemy["turnos"] == 0: self.status_enemy["atk_debuff"] = 0

        loop = asyncio.get_event_loop()
        urls = random.sample(self.p1['moves_urls'], min(4, len(self.p1['moves_urls'])))
        self.hand = []
        for url in urls:
            m = loop.run_until_complete(buscar_detalhes_movimento(url))
            if m:
                tipo_status = random.choice(["buff", "debuff"])
                self.hand.append({
                    "name": m['name'],
                    "cost": random.randint(1, 2),
                    "value": (m['power'] // 5) if m['power'] > 0 else 10,
                    "type": "attack" if m['power'] > 0 else tipo_status
                })

    def check_game_over(self):
        if self.player_hp <= 0:
            self.player_hp = 0
            self.game_over = True
        if self.enemy_hp <= 0:
            self.enemy_hp = 0
            self.game_over = True

    def play_card(self, card):
        if self.energy < card['cost'] or self.game_over: return
        self.energy -= card['cost']
        
        if card['type'] == "attack":
            dano_final = card['value'] + self.status_player["atk_buff"] + self.status_enemy["atk_debuff"]
            self.enemy_hp -= dano_final
        elif card['type'] == "buff":
            self.status_player["atk_buff"] = card['value']
            self.status_player["turnos"] = 3
        elif card['type'] == "debuff":
            self.status_enemy["atk_debuff"] = card['value']
            self.status_enemy["turnos"] = 3
            
        self.hand.remove(card)
        self.check_game_over()

    def enemy_turn(self):
        if self.game_over: return
        dano = 10
        self.player_hp -= dano
        self.check_game_over()
        if not self.game_over:
            self.novo_turno()
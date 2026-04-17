Pokemon Card Battle Engine

Motor de batalha de cartas por turnos desenvolvido em Python, com dados dinâmicos obtidos em tempo real via PokeAPI.

Overview

Este projeto implementa um sistema de combate baseado em turnos, onde cada rodada apresenta novas possibilidades estratégicas a partir de ataques reais dos Pokémons. A integração com a PokeAPI garante variabilidade e replay contínuo.

Tech Stack
Python 3.10+
Pygame
Requests
Asyncio
Features
PokeAPI Integration
Consumo em tempo real de dados de Pokémons e movimentos.
Status System
Aplicação de buffs e debuffs com duração de até 3 turnos.
Dynamic Deck
Geração de 4 ataques aleatórios por turno com base no movepool.
Battle Management
Controle de HP, uso de PP e definição de vitória/derrota.
Getting Started
Requirements
Python instalado
pip disponível no ambiente
Installation
git clone https://github.com/Onnichan/pokeapi-react.git
cd pokeapi-react
pip install pygame requests
Run
python main.py
Project Structure
.
├── main.py           # Loop principal e renderização
├── engine.py         # Regras de combate e turnos
├── pokemon_data.py   # Integração com a API
└── card.py           # Interface das cartas

# Master Plan: 2D Dungeon Crawler RPG

## I. Project Setup

### A. Environment
1.  **Create Virtual Environment:**
    -   Use `python -m venv venv` to create a virtual environment.
    -   Activate the environment using `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows).
2.  **Install Dependencies:**
    -   Install required libraries using `pip install pygame numpy pytmx pickle sounddevice`.
3.  **Project Structure:**
    ```
    dungeon_crawler/
    ├── venv/           # Virtual environment
    ├── assets/         # Game assets (images, sounds, etc.)
    │   ├── sprites/
    │   ├── sounds/
    │   ├── maps/
    │   └── ...
    ├── src/            # Source code
    │   ├── core/       # Core game logic (game loop, etc.)
    │   │   ├── game.py
    │   │   ├── settings.py
    │   │   └── ...
    │   ├── entities/   # Player, enemies, etc.
    │   │   ├── player.py
    │   │   ├── enemy.py
    │   │   └── ...
    │   ├── map/        # Map generation and management
    │   │   ├── generator.py
    │   │   ├── tile.py
    │   │   └── ...
    │   ├── combat/     # Combat system logic
    │   │   ├── combat_system.py
    │   │   ├── attack.py
    │   │   └── ...
    │   ├── ui/         # User interface elements
    │   │   ├── hud.py
    │   │   ├── menu.py
    │   │   └── ...
    │   ├── items/      # Inventory, equipment, crafting
    │   │   ├── item.py
    │   │   ├── inventory.py
    │   │   └── ...
    │   ├── utils/      # Utility functions
    │   │   ├── math_utils.py
    │   │   └── ...
    │   ├── main.py     # Entry point of the game
    │   └── ...
    ├── data/           # Game data (save files, etc.)
    ├── masterplan.md   # This file
    └── README.md
    ```

### B. Initial Setup
1.  **Create basic project structure** as outlined above.
2.  **Create a basic Pygame window** in `src/main.py` to ensure the environment is working.
3.  **Implement basic game loop** in `src/core/game.py`.
4.  **Create a settings file** in `src/core/settings.py` to store game constants.

## II. Core Game Mechanics

### A. Procedural Generation
1.  **Implement a basic room generation algorithm** in `src/map/generator.py`.
2.  **Create a tile class** in `src/map/tile.py` to represent map tiles.
3.  **Implement pathway generation** to connect rooms.
4.  **Add treasure and boss room generation logic.**
5.  **Implement dynamic difficulty scaling** based on player progression.

### B. Combat System
1.  **Create a combat system class** in `src/combat/combat_system.py`.
2.  **Implement basic melee attack logic** in `src/combat/attack.py`.
3.  **Implement ranged projectile logic.**
4.  **Implement magic spell logic.**
5.  **Add status effect system.**
6.  **Implement critical hit mechanics.**
7.  **Add dodge and block abilities.**

## III. Player Character

### A. Character Classes
1.  **Create a base character class** in `src/entities/player.py`.
2.  **Implement Warrior class** inheriting from the base class.
3.  **Implement Archer class** inheriting from the base class.
4.  **Implement Mage class** inheriting from the base class.

### B. Attributes
1.  **Add health, mana, stamina, and experience points** to the character class.

### C. Progression
1.  **Implement a basic skill tree** in `src/entities/player.py`.
2.  **Implement level-up system.**
3.  **Add attribute point allocation logic.**

## IV. Inventory and Equipment

### A. Loot System
1.  **Implement item drop logic** in `src/items/item.py`.
2.  **Implement rarity tiers.**

### B. Equipment
1.  **Add weapon, armor, and accessory slots** to the character class.
2.  **Implement visual upgrades based on equipment.**

### C. Crafting
1.  **Implement basic crafting mechanics** in `src/items/inventory.py`.
2.  **Implement item enhancement.**
3.  **Implement salvaging system.**

## V. Enemy System

### A. Enemy Types
1.  **Create a base enemy class** in `src/entities/enemy.py`.
2.  **Implement diverse enemy behaviors.**
3.  **Add pixel-art enemy sprites.**
4.  **Implement adaptive AI pathfinding.**
5.  **Implement boss encounters.**

### B. Enemy Mechanics
1.  **Implement dynamic scaling.**
2.  **Add unique attack patterns.**
3.  **Implement environmental interactions.**

## VI. Technical Requirements

### A. Code Quality
1.  **Follow modular, object-oriented design principles.**
2.  **Use efficient algorithms.**
3.  **Optimize for performance.**
4.  **Ensure cross-platform compatibility.**

### B. Game Management
1.  **Implement save/load functionality** using `pickle`.
2.  **Add error handling.**
3.  **Implement input validation.**

## VII. Bonus Features

### A. Visuals and Audio
1.  **Add animated pixel-art graphics.**
2.  **Implement background music.**
3.  **Add sound effects.**

### B. Additional Features
1.  **Implement achievement system.**
2.  **Add mini-map.**
3.  **Implement difficulty settings.**

## VIII. Development Tools

### A. Tools
1.  **Use Visual Studio Code for coding.**
2.  **Use Pygame for game engine.**
3.  **Use Aseprite for pixel art.**
4.  **Use PyCharm for debugging (optional).**

## IX. Performance Considerations

### A. Optimization
1.  **Aim for smooth 60 FPS gameplay.**
2.  **Minimize loading times.**
3.  **Implement efficient memory management.**

## X. Development Phases

### Phase 1: Core Mechanics
-   Project setup, basic game loop, procedural generation, basic combat.
### Phase 2: Player and Enemies
-   Player classes, attributes, progression, basic enemy AI.
### Phase 3: Inventory and Equipment
-   Loot system, equipment, basic crafting.
### Phase 4: Polish and Features
-   Bonus features, performance optimization, bug fixing.

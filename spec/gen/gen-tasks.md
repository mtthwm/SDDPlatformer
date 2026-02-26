# External Tasks

- Install pygame via pip install pygame and create a requirements.txt containing pygame
- Create the project file structure: main.py, player.py, and tiles.py
- Create a tiles.json file that maps hex color strings to tile property objects, each with a solid boolean and an image_path string
- Create sprite images for each tile type and place them at the paths defined in tiles.json
- Create a level.png using an image editor where each pixel represents one tile, using the hex colors defined in tiles.json to lay out a floor, some platforms, and open space


# Coding Tasks

- TILE SYSTEM | Define tile data structure | In tiles.py, write a load_tile_defs(path) function that reads tiles.json and returns a dict mapping hex strings to tile property dicts containing solid and image_path
- TILE SYSTEM | Preload tile sprites | In tiles.py, write a load_tile_sprites(tile_defs, tile_size) function that iterates the tile definitions, loads each image with pygame.image.load, scales it to tile_size, and returns a dict mapping hex strings to surfaces
- TILE SYSTEM | Write level loader | In tiles.py, write load_level(path, tile_defs) that loads a PNG with pygame, reads each pixel, converts it to a hex string, looks it up in tile_defs, and returns a 2D list of tile definition dicts
- TILE SYSTEM | Write tile renderer | In tiles.py, write draw_tiles(surface, tile_grid, tile_sprites, tile_size) that iterates the grid and blits the appropriate sprite surface for each non-empty tile at its computed screen position
- PLAYER | Create Player class | In player.py, create a Player class with a pygame.Rect, a vel list, and a grounded flag set in __init__
- PLAYER | Implement movement | Add handle_input(self) to set horizontal velocity from keypresses, apply_gravity(self, gravity) to accelerate downward each frame, and jump(self) to set a negative vertical velocity when grounded
- PLAYER | Implement collision | Add move_and_collide(self, tile_grid, tile_size) that moves the rect by velocity in each axis separately, resolves overlaps with solid tiles (checking the solid property) per axis, and updates self.grounded on downward vertical collisions
- PLAYER | Implement draw method | Add draw(self, surface) that renders the player rect to the screen
- GAME LOOP | Initialize pygame | In main.py, set up the pygame window, clock, gravity constant, and tile_size, then load tile definitions, preload sprites, and load the tile grid before the game loop
- GAME LOOP | Wire up player | Instantiate Player at a valid starting position above the floor, handle jump input in the pygame event loop, and call movement and collision methods each frame in the correct order
- GAME LOOP | Wire up rendering | Each frame, fill the background, call draw_tiles, call player.draw, then pygame.display.flip() and clock.tick(60)
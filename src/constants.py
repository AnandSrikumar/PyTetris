constants = {}
constants['SCREEN_WIDTH'] = 1920
constants['SCREEN_HEIGHT'] = 1080
constants['FULL_SCREEN'] = True
constants['BACKGROUND_COLOR'] = (245, 240, 240)
constants['GAME_CONTAINER_COLOR'] = (0, 0, 0)
constants['GRAY'] = (191, 191, 191)
constants['BLOCK_SIZE'] = 35
constants['GRID_BLOCKS'] = (20, 10)
constants['GRID_ORIGIN'] = (50, 70)
constants['TITLE_SIZES'] = {"main_menu": 48, 'pause_menu': 24,
                            'highscore': 30, 'game_over': 36,
                            'game': 12}
constants['TITLE_COLOR'] = (132, 237, 245)
constants['TITLE_FONT'] = "assets/fonts/title_font.otf"
constants['RANDOM_COLORS'] = [(92, 206, 255),
                              (31, 47, 224),
                              (224, 109, 247),
                              (212, 38, 87)]
constants['main_menu'] = "assets/screens/main_menu.json"
constants['game'] = "assets/screens/game_screen.json"
constants['game_over'] = "assets/screens/game_over.json"
constants['menu_title_font'] = {"size": 32, "color": (
    255, 255, 255), 'path': "assets/fonts/menu_items.ttf"}
constants['text_font'] = {"size": 32, "color": (
    255, 255, 255), 'path': "assets/fonts/text_font.ttf"}
constants['shapes'] = "assets/screens/shapes_rotations.json"
constants['movement_delay'] = {1: 400,
                               2: 250,
                               3: 150,
                               4: 100}
constants['level_change_score'] = {1: 12000,
                                   2: 35000,
                                   3: 55000}

constants['scores_awarded'] = {1: {"lines": {1: "60",
                                             2: "120",
                                             3: "360",
                                             4: "1000"},
                                   'placed': 20,
                                   'placed_fast': 30},
                               2: {"lines": {1: "80",
                                             2: "160",
                                             3: "480",
                                             4: "1200"},
                                   'placed': 25,
                                   'placed_fast': 35},
                               3: {"lines": {1: "100",
                                             2: "200",
                                             3: "600",
                                             4: "1500"},
                                   'placed': 30,
                                   'placed_fast': 40},
                               4: {"lines": {1: "120",
                                             2: "240",
                                             3: "720",
                                             4: "1800"},
                                   'placed': 40,
                                   'placed_fast': 50}}

# constants['main_menu'] = "assets/screens/main_menu.json"
# constants['main_menu'] = "assets/screens/main_menu.json"

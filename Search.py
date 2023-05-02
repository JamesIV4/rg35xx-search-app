import pygame
import pygame_gui
import os
import fnmatch

class Keyboard:
    def __init__(self, gui_manager, search_input):
        self.gui_manager = gui_manager
        self.search_input = search_input
        
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((25, 200), (590, 230)),
            manager=self.gui_manager,
        )
        
        # Don't show the panel initially
        self.panel.hide()
        self.panel.panel_container.hide()
        self.showing = False
        
        # Make sure it's on top
        self.panel.change_layer(10)
        self.panel.panel_container.change_layer(10)
        
                    
        button_width = 45
        button_height = 30
        key_spacing = 10
        key_start_x = 20
        key_start_y = 20

        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 
            'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '!',
            'Close', 'Space', 'Bksp'
        ]

        for i, key in enumerate(keys):
            row = i // 10
            col = i % 10
            rect = pygame.Rect(
                (key_start_x + col * (button_width + key_spacing),
                 key_start_y + row * (button_height + key_spacing)),
                (button_width, button_height)
            )
            if key == 'Bksp':
                rect = pygame.Rect((460, key_start_y + row * (button_height + key_spacing)), (100, button_height))
            elif key == 'Close':
                rect = pygame.Rect((key_start_x + col * (button_width + key_spacing), key_start_y + row * (button_height + key_spacing)), (100, button_height))
            elif key == 'Space':
                rect = pygame.Rect((130, key_start_y + row * (button_height + key_spacing)), (320, button_height))
      
            button = pygame_gui.elements.UIButton(
                relative_rect=rect,
                text=key,
                manager=self.gui_manager,
                container=self.panel,
                object_id=i,
            )

            button.callback = self._on_key_press
            
    def togglePanel(self):
        # Containers
        self.showing = not self.showing
        if self.showing:
            self.panel.show()
            self.panel.panel_container.show()
            
            self.button_list_main = []
        else:
            self.panel.hide()
            self.panel.panel_container.hide()

    def _on_key_press(self, button):
        print(f"Button {button.text} was pressed.")
        self.search_input.set_text(self.search_input.get_text() + button.text)

class SearchApp:
    def __init__(self):

        # initialize pygame
        pygame.init()

        # create the window
        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        # self.screen = pygame.Surface((WINDOW_SIZE)).convert()

        # Set the title bar to "Search Roms"
        pygame.display.set_caption("Search Roms")

        # Create a GUI manager
        self.gui_manager = pygame_gui.UIManager(WINDOW_SIZE)

        # Set the background color to grey
        background_color = (42, 42, 42)
        self.screen.fill(background_color)

        # Define the font
        myfont = pygame.font.SysFont("Oswald", 25)

        # Search label
        self.search_label_shadow = myfont.render("Search", 1, (20, 20, 20))
        self.search_label = myfont.render("Search", 1, (255, 255, 255))
        self.screen.blit(self.search_label_shadow, (28, 16))
        self.screen.blit(self.search_label, (26, 14))

        # Create search input field
        self.search_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((25, 50), (425, 50)), manager=self.gui_manager, object_id="#search-input")
        self.search_input.blink_cursor_time = 480

        # Create search button
        self.search_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((465, 50), (150, 50)),
            text='Search',
            manager=self.gui_manager
        )

        # Search results mock data
        self.search_results = [
            "Mario Bros., Arcade",
            "Super Mario Bros., NES",
            "Super Mario Bros.: The Lost Levels, NES",
            "Super Mario Bros. 2, NES",
            "Super Mario Bros. 3, NES",
            "Super Mario Land, Game Boy",
            "Super Mario World, SNES",
            "Super Mario Land 2: 6 Golden Coins, Game Boy",
            "Super Mario All-Stars, SNES",
            "Super Mario World 2: Yoshi's Island, SNES",
            "Super Mario 64, Nintendo 64",
            "Mario Kart 64, Nintendo 64",
            "Super Mario Bros. Deluxe, Game Boy Color",
            "Paper Mario, Nintendo 64",
            "Mario Kart: Super Circuit, Game Boy Advance",
            "Super Mario Sunshine, GameCube",
            "Mario Kart: Double Dash!!, GameCube",
            "Mario & Luigi: Superstar Saga, Game Boy Advance",
            "Paper Mario: The Thousand-Year Door, GameCube",
            "Mario Kart DS, Nintendo DS",
            "New Super Mario Bros., Nintendo DS",
            "Super Mario Galaxy, Wii",
            "Mario Kart Wii, Wii",
            "New Super Mario Bros. Wii, Wii",
            "Super Mario Galaxy 2, Wii",
            "Super Mario 3D Land, Nintendo 3DS",
            "Mario Kart 7, Nintendo 3DS",
            "New Super Mario Bros. 2, Nintendo 3DS",
            "New Super Mario Bros. U, Wii U",
            "Super Mario 3D World, Wii U",
            "Mario Kart 8, Wii U",
            "Super Mario Odyssey, Nintendo Switch",
            "Mario Kart 8 Deluxe, Nintendo Switch",
            "Super Mario Maker 2, Nintendo Switch",
            "Paper Mario: The Origami King, Nintendo Switch",
            "Super Mario 3D All-Stars, Nintendo Switch"
        ]

        self.sorted_search_results = sorted(self.search_results)

        # Results label
        self.results_label_shadow = myfont.render("Results", 1, (20, 20, 20))
        self.results_label = myfont.render("Results", 1, (255, 255, 255))
        self.screen.blit(self.results_label_shadow, (28, 115))
        self.screen.blit(self.results_label, (26, 113))

        # Create results list
        self.results_list = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect((25, 150), (590, 280)),
            manager=self.gui_manager,
            item_list=[]
        )
        
        # Create on-screen keyboard
        self.keyboard = Keyboard(self.gui_manager, self.search_input)
        
        # Highlight handling
        self.highlight_area = "main" # "main" or "keyboard"
        # Main
        self.button_list_main = [self.search_input, self.search_button, *self.results_list.item_list_container.elements]
        self.button_index_main = 0
        self.active_button_main = self.button_list_main[self.button_index_main]
        # Keyboard
        self.button_list_keyboard = [*self.keyboard.panel.panel_container.elements]
        self.button_index_keyboard = 0
        self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
        
    def search_directory(self, path, search_string='', excluded_exts=None):
        """
        Search a directory (and its subdirectories) for files matching the given search string, excluding any file types
        specified in exclude_types.
        """
        files = []
        for root, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if any(filename.endswith(ext) for ext in excluded_exts):
                    continue
                if fnmatch.fnmatch(filename, '*' + search_string + '*'):
                    files.append(os.path.join(root, filename))
        return files
        
    def resetButtonListMain(self):
        self.button_list_main = [self.search_input, self.search_button, *self.results_list.item_list_container.elements]
        
    def handleSearch(self):
        if self.search_input.text != "":
            # Clear previous search results
            self.results_list.set_item_list([])

            # Perform search
            query = self.search_input.text
            directory = "D:\Games\EMULATION\RG35XX\Roms"
            exclude_extensions = [".png", ".jpg", ".jpeg"]
            matching_files = self.search_directory(directory, query, exclude_extensions)
            print("MATCHES", matching_files)
            
            results = sorted(matching_files)
            self.results_list.add_items(results)
            self.resetButtonListMain()            
        
    def toggleKeyboard(self):
        self.keyboard.togglePanel()
        if self.highlight_area == "main":
            self.highlight_area = "keyboard"
        else: 
            self.highlight_area = "main"
            
    def handleSpaceButtonEvents(self, button_pressed):
        if self.highlight_area == "main":
            if button_pressed == self.search_button:
                self.handleSearch()
            elif button_pressed == self.search_input:
                self.toggleKeyboard()

    def run(self):
        # main game loop
        running = True
        while running:            
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        print(f"Button was pressed:", event.ui_element.text)
                        if event.ui_element.text == "Close":
                            self.toggleKeyboard()
                            
                        elif event.ui_element == self.search_button:
                            self.handleSearch()
                        
                        elif event.ui_element.text == "Space":
                            self.search_input.set_text(self.search_input.text + " ")
                        elif event.ui_element.text == "Bksp":
                            self.search_input.set_text(self.search_input.text[:-1])
                        else:
                            self.search_input.set_text(self.search_input.text + event.ui_element.text)
                            
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT:
                    self.toggleKeyboard()
                
                if event.type == pygame.KEYDOWN:  
                    # Move between buttons with arrow keys
                    if event.key == pygame.K_LEFT:
                        if self.highlight_area == "main":
                            if self.button_index_main > 0:
                                self.button_index_main -= 1
                                self.active_button_main = self.button_list_main[self.button_index_main]
                                # print("Updated selection:", self.active_button_main.text, ", Index:", self.button_index_main)
                        else:
                            if self.button_index_keyboard > 0:
                                self.button_index_keyboard -= 1
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                                # print("Updated selection:", self.active_button_keyboard.text, ", Index:", self.button_index_keyboard)
                    elif event.key == pygame.K_RIGHT:
                        if self.highlight_area == "main":
                            if self.button_index_main < (self.button_list_main.__len__() - 1):
                                self.button_index_main += 1
                                self.active_button_main = self.button_list_main[self.button_index_main]
                        else:
                            if self.button_index_keyboard < (self.button_list_keyboard.__len__() - 1):
                                self.button_index_keyboard += 1
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                    if event.key == pygame.K_UP:
                        if self.highlight_area == "main":
                            if self.button_index_main > 0:
                                self.button_index_main -= 1
                                self.active_button_main = self.button_list_main[self.button_index_main]
                        else:
                            if self.button_index_keyboard >= 10 and self.button_index_keyboard <= 40:
                                self.button_index_keyboard -= 10
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard == 40:
                                self.button_index_keyboard = 29
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard == 41:
                                self.button_index_keyboard = 32
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard == 42:
                                self.button_index_keyboard = 38
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                    elif event.key == pygame.K_DOWN:
                        if self.highlight_area == "main":
                            if self.button_index_main < (self.button_list_main.__len__() - 1):
                                self.button_index_main += 1
                                self.active_button_main = self.button_list_main[self.button_index_main]
                        else:
                            if self.button_index_keyboard >= 0 and self.button_index_keyboard <= 29:
                                self.button_index_keyboard += 10
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard > 29 and self.button_index_keyboard <= 31:
                                self.button_index_keyboard = 40
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard > 31 and self.button_index_keyboard <= 37:
                                self.button_index_keyboard = 41
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                            elif self.button_index_keyboard > 37 and self.button_index_keyboard <= 40:
                                self.button_index_keyboard = 42
                                self.active_button_keyboard = self.button_list_keyboard[self.button_index_keyboard]
                                
                    # Activate the active button with spacebar
                    elif event.key == pygame.K_SPACE:
                        print(f"Button was pressed ACTIVATE.", self.active_button_main.text)
                        self.handleSpaceButtonEvents(self.active_button_main)
                    
                # Update the GUI manager with the current event
                self.gui_manager.process_events(event)
                
            # Update the GUI manager
            self.gui_manager.update(pygame.time.Clock().tick(60))
            
            self.gui_manager.set_visual_debug_mode(False)
            
            # Draw the GUI manager on the screen
            self.gui_manager.draw_ui(self.screen)
            
            # Draw a highlight around the active button
            if self.highlight_area == "main":
                pygame.draw.rect(self.screen, (24, 109, 245), self.active_button_main.rect, 2, 4)
            else:
                pygame.draw.rect(self.screen, (24, 109, 245), self.active_button_keyboard.rect, 2, 4)
            
            # update the screen
            pygame.display.flip()

        # clean up pygame
        pygame.quit()
        
if __name__ == '__main__':
    app = SearchApp()
    app.run()
class Settings: 
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's staticsettings."""
        # Screen settings 
        self.screen_width = 1200 
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Ship settings
        self.ship_limit = 3  
        #Bullet settings 
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        # Alien settings 
        
        self.fleet_drop_speed = 10
        
        
        #Houw qucikly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Intialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 2.5
        # fleet_direction of 1 repersents right, -1 repersents left
        self.fleet_direction = 1

        # Scoring Settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed  and point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
class Settings:
    def __init__(self):
        self.resolution_width = 1200
        self.resolution_height = 650
        self.resolution = (self.resolution_width, self.resolution_height)
        self.bg_color = (255, 255, 0)

        self.ship_limit = 3

        self.fleet_drop_speed = 10

        self.bullet_info = {
            "speed": 1.0,
            "width": 3,
            "height": 15,
            "color": (60, 60, 60),
            "bullets_allowed": 3
        }

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)

# To download images easy use the `curl` command.
# ./images > curl <image-url> --output <image-name>.bmp
# example
# > curl https://raw.githubusercontent.com/ehmatthes/pcc_2e/master/chapter_12/adding_ship_image/images/ship.bmp --output ship.bmp

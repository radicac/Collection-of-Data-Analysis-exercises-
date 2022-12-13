class Settings:
    def __init__(self):
        self.resolution_width = 1200
        self.resolution_height = 650
        self.resolution = (self.resolution_width, self.resolution_height)
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1
        self.ship_limit = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 30
        self.fleet_direction = 1
        self.bullet_info = {
            "speed": 1.0,
            "width": 3,
            "height": 15,
            "color": (60, 60, 60),
            "bullets_allowed": 3
        }

# To download images easy use the `curl` command.
# ./images > curl <image-url> --output <image-name>.bmp
# example
# > curl https://raw.githubusercontent.com/ehmatthes/pcc_2e/master/chapter_12/adding_ship_image/images/ship.bmp --output ship.bmp

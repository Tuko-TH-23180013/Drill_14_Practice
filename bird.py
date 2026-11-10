from pico2d import get_canvas_width, load_image

import game_framework


SHEET_HEIGHT = 506
# (x, top, width, height) rectangles around each non-transparent pose.
# The source image uses top-origin coordinates; Pico2D clip APIs use bottom-origin.
BIRD_FRAMES = (
    (34, 1, 146, 143), (216, 2, 146, 141), (398, 12, 146, 130),
    (555, 17, 171, 122), (728, 48, 182, 88),
    (34, 217, 146, 118), (216, 216, 146, 124), (398, 216, 146, 120),
    (580, 217, 146, 109), (762, 219, 146, 110),
    (34, 392, 146, 108), (216, 394, 146, 106),
    (376, 395, 168, 88), (546, 370, 180, 114),
)
BIRD_HALF_WIDTH = max(frame[2] for frame in BIRD_FRAMES) / 2.0
ANIMATION_FRAMES_PER_SECOND = 12.0
BIRD_SCALE = 1.0
WORLD_PIXELS_PER_METER = 10.0 / 0.3
FLIGHT_SPEED_KMPH = 20.0
FLIGHT_SPEED_MPS = FLIGHT_SPEED_KMPH * 1000.0 / 3600.0
FLIGHT_SPEED_PPS = FLIGHT_SPEED_MPS * WORLD_PIXELS_PER_METER


class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x = get_canvas_width() / 2
        self.y = 400
        self.direction = 1
        self.animation_frame = 0.0

    def update(self):
        frame_time = max(0.0, game_framework.frame_time)
        self.animation_frame = (
            self.animation_frame +
            ANIMATION_FRAMES_PER_SECOND * frame_time
        ) % len(BIRD_FRAMES)
        self.x += self.direction * FLIGHT_SPEED_PPS * frame_time
        left_limit = BIRD_HALF_WIDTH
        right_limit = get_canvas_width() - BIRD_HALF_WIDTH
        while self.x < left_limit or self.x > right_limit:
            if self.x > right_limit:
                self.x = right_limit - (self.x - right_limit)
                self.direction = -1
            elif self.x < left_limit:
                self.x = left_limit + (left_limit - self.x)
                self.direction = 1

    def draw(self):
        frame_index = int(self.animation_frame)
        sx, top, sw, sh = BIRD_FRAMES[frame_index]
        sy = SHEET_HEIGHT - top - sh
        flip = 'h' if self.direction < 0 else ''
        self.image.clip_composite_draw(
            sx, sy, sw, sh, 0, flip,
            self.x, self.y, sw * BIRD_SCALE, sh * BIRD_SCALE
        )

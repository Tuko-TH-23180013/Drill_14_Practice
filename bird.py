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
ANIMATION_FRAMES_PER_SECOND = 12.0
BIRD_SCALE = 1.0


class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x = get_canvas_width() / 2
        self.y = 400
        self.animation_frame = 0.0

    def update(self):
        self.animation_frame = (
            self.animation_frame +
            ANIMATION_FRAMES_PER_SECOND * game_framework.frame_time
        ) % len(BIRD_FRAMES)

    def draw(self):
        frame_index = int(self.animation_frame)
        sx, top, sw, sh = BIRD_FRAMES[frame_index]
        sy = SHEET_HEIGHT - top - sh
        self.image.clip_draw(
            sx, sy, sw, sh,
            self.x, self.y, sw * BIRD_SCALE, sh * BIRD_SCALE
        )

from pico2d import get_canvas_width, load_image


SHEET_HEIGHT = 506
FIRST_FRAME = (34, 1, 146, 143)  # (x, top, width, height), top-origin
BIRD_DRAW_WIDTH = 180
BIRD_DRAW_HEIGHT = 150


class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x = get_canvas_width() / 2
        self.y = 400

    def update(self):
        pass

    def draw(self):
        sx, top, sw, sh = FIRST_FRAME
        sy = SHEET_HEIGHT - top - sh
        self.image.clip_draw(
            sx, sy, sw, sh,
            self.x, self.y, BIRD_DRAW_WIDTH, BIRD_DRAW_HEIGHT
        )

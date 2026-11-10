from pico2d import *
import game_world
import game_framework
from bird import Bird
from grass import Grass

bird = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global bird
    bird = Bird()
    game_world.add_oject(bird)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    pass


def resume():
    pass


def finish():
    global bird
    game_world.clear()
    bird = None


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

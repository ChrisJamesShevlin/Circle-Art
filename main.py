import py5
import math

def setup():
    py5.size(1920, 1080)
    py5.background(0)
    
def draw():
    py5.stroke(0, 255, 0)
    py5.fill(0)
    py5.circle(py5.mouse_x, py5.mouse_y, 50)
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame("circle_art.png")

py5.run_sketch()

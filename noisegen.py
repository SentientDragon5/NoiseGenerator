# pip install pillow
# pip install numpy
# pip install noise

# if you want to do shaders
# pip install pyglet

# https://stackoverflow.com/questions/60350598/perlin-noise-in-pythons-noise-library

import noise
import numpy as np
from PIL import Image


def perlin(x, y, scale, octaves, persistence, lacunarity, seed):
    world = np.zeros((x,y))
    x_idx = np.linspace(0, 1, x)
    y_idx = np.linspace(0, 1, y)
    world_x, world_y = np.meshgrid(x_idx, y_idx)
    world = np.vectorize(noise.pnoise2)(world_x/scale,
                        world_y/scale,
                        octaves=octaves,
                        persistence=persistence,
                        lacunarity=lacunarity,
                        repeatx=x,
                        repeaty=y,
                        base=seed)

    return np.floor((world + 1) * 127).astype(np.uint8)

# settings
scale = .1
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0,100)
# dimensions
x,y = 1024, 1024

# generation
r = perlin(x, y, scale, octaves, persistence, lacunarity, seed)
g = perlin(x, y, scale, octaves, persistence, lacunarity, seed+1)
b = perlin(x, y, scale, octaves, persistence, lacunarity, seed+2)
img = np.dstack((r,g,b))
image = Image.fromarray(img, mode='RGB')
image.save('perlin' + (str)(x) + 'x' + (str)(y)  + '.png')

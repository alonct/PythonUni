from MatMaps.MatMaps_code.Engine.EngineMain import MatMapsEngine
from MatMaps.MatMaps_code.Graphics.GraphicsMain import MatMapsGraphics
import pygame


class MatMap:

    def __init__(self):
        self._engine = MatMapsEngine()
        self._graphics = MatMapsGraphics(self._engine)

    def run(self):
        pass
    
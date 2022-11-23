from matplotlib import pyplot as plt
from matplotlib import collections as mcoll
from matplotlib.animation import FuncAnimation
import numpy as np

class Scene:
    def __init__(self, points=[], lines=[]) -> None:
        self.points = points
        self.lines = lines

class PointsCollection:
    def __init__(self, points, **kwargs) -> None:
        self.points = points
        self.kwargs = kwargs
    
    def add_points(self, points):
        for point in points:
            self.points.append(point)

class LinesCollection:
    def __init__(self, lines, **kwargs) -> None:
        self.lines = lines
        self.kwargs = kwargs
    
    def add_lined(self, lines):
        for line in lines:
            self.lines.append(line)

    def get_lines(self):
        return mcoll.LineCollection(self.lines, **self.kwargs)  

class Plot:
    def __init__(self, scenes=[Scene()], points=[], lines=[]) -> None:
        self.fig = plt.figure()
        self.scenes = scenes
        if points or lines:
            self.scenes[0].points = points
            self.scenes[0].lines = lines

    @staticmethod
    def convert_points(points_colllection):
        dev_x = []
        dev_y = []
        for x in points_colllection.points:
            dev_x.append(x[0])
            dev_y.append(x[1])
        return (dev_x, dev_y)

    def add_scene(self, points=[], lines=[]):
        scene = Scene(points, lines)
        self.scenes.append(scene)

    def draw(self, interval=800, scene_num=-1):
        if scene_num == -1:
            plt.close()
            curr_scene = [0]
            def an(i):
                ax = plt.axes()
                scene = self.scenes[curr_scene[0]]
                for collection in scene.points:
                    dev_x, dev_y = Plot.convert_points(collection)
                    ax.scatter(dev_x, dev_y, **collection.kwargs)
                for collection in scene.lines:
                    ax.add_collection(collection.get_lines())

                if curr_scene[0] < len(self.scenes) - 1:
                    curr_scene[0] += 1
            
            ani = FuncAnimation(plt.gcf(), an, interval=interval)
        else:
            if scene_num-1 >= len(self.scenes):
                return -1
            plt.close()
            ax = plt.axes()
            scene = self.scenes[scene_num-1]
            for collection in scene.points:
                dev_x, dev_y = Plot.convert_points(collection)
                ax.scatter(dev_x, dev_y, **collection.kwargs)
            for collection in scene.lines:
                ax.add_collection(collection.get_lines())

        plt.show()

    def draw_scene(self, scene_num=1):
        if scene_num-1 >= len(self.scenes):
            return -1

        plt.close()
        ax = plt.axes()
        scene = self.scenes[scene_num-1]
        for collection in scene.points:
            dev_x, dev_y = Plot.convert_points(collection)
            ax.scatter(dev_x, dev_y, **collection.kwargs)
        for collection in scene.lines:
            ax.add_collection(collection.get_lines())
        
        plt.show()


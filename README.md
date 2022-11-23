# graphictool_temp
Simple tool to represent your geometric algorithms results

## Python pakages needed

* matplotlib

## Usage

```python
from plot import Plot, PointsCollection, LinesCollection
```

# Plot
Structure which can store and draw PointsCollection and LinesCollection

You can simply create new plot
```python
plot = Plot(points=[PointsCollection(your_points_list, **matplotlib_kwargs)], lines=LinesCollection(your_lines_list, **matplotlib_kwargs))
```

To draw plot use method Plot.draw().
If your plot has more scenes, draw method will display them in animation.
You can set interval as draw methon argument, default interval=800

```python
Plot().draw(interval=1000)
```

If you want to one particular scene, you can set scene_num argument

```python
Plot().draw(scene_num=25)
```

To add new scene use add_scene() method

```python
new_scene = Scene([your_PointsCollections()], [your_LinesCollections()])
Plot().add_scene(new_scene)
```

Points and lines are kept in scenes

# Scene

Scene object contains 2 fields

```python
self.points # list of PointsCollections structures
self.lines # list of LinesCollection structures
```
# PointsCollection

This structure contains 2 fields

```python
self.points # list of points (x, y)
self.kwargs # list of matplotlib modifiers
```

You can also add points using add_points(points) method

# LinesCollection

This structure is similar to PointsCollection

It contains list of lines ((x1, y1), (x2, y2))

You can add more lines using add_lines(lines) method


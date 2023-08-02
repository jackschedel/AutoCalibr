import bpy
import math

radius = 1.
shift = 2 * math.pi / len(bpy.context.selected_objects)  #how much to rotate each consecutive object


for i, obj in enumerate(bpy.context.selected_objects):
    obj.location.x = radius * math.cos(i*shift)
    obj.location.y = radius * math.sin(i*shift)

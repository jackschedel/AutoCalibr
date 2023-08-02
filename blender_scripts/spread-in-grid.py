import bpy
import math

# Set start location
start_location = (0, 0, 0)
spacing = 2 # Change this to increase/decrease spacing between objects

# Calculate number of objects in rows and columns
num_objects = len(bpy.context.selected_objects)
grid_size = math.ceil(math.sqrt(num_objects))

for i, obj in enumerate(bpy.context.selected_objects):
    row = i // grid_size
    col = i % grid_size

    # Calculate location for each object
    obj.location.x = start_location[0] + col * spacing
    obj.location.y = start_location[1] + row * spacing

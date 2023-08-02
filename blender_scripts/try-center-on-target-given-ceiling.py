import bpy

for obj in bpy.context.selected_objects:
  # Calculate the approximate center by using the bounding box
  bbox_center = (sum((obj.matrix_world @ Vector(v) for v in obj.bound_box), Vector())) / 8
  z_diff = 0.3 - bbox_center.z

  # Calculate the highest point (in world coordinates)
  highest_z = max((obj.matrix_world @ Vector(v[:])).z for v in obj.bound_box)

  if highest_z + z_diff > 1:
    # If moving center to 0.3 would result in going higher than 1, adjust the diff
    z_diff -= ((highest_z + z_diff) - 1)

  # Move the object
  obj.location.z += z_diff


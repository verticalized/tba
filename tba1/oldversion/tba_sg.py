##tba scene generator
import os

print(os.getcwd())

with open('scene_types.txt', 'r') as scene_type_list:
    for line in scene_type_list:
        scene_type_list_contents = scene_type_list.readline()
        print(scene_type_list_contents)

print(scene_type_list.name)

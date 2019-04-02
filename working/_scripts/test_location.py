import os

current_dir = os.path.realpath(__file__)
target_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-3])
print(target_dir)

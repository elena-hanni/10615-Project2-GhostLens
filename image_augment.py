import Augmentor
p = Augmentor.Pipeline("ghost_50", "resize")

# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=25)
# p.flip_left_right(probability=1)
# p.crop_random(probability=1, percentage_area=0.7)
# p.rotate(probability=1, max_left_rotation=20, max_right_rotation=20)
p.resize(probability=1.0, width=120, height=120)

p.process()
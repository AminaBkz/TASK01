import os
import random
from IPython.display import Image, display

class Animal(object):
    def __init__(self, root_path: str, batch_size: int,
                 is_train: bool = True,
                 width: int = 256, height: int = 256):
        self.root_path = root_path
        self.batch_size = batch_size
        self.width = width
        self.height = height
        self.is_train = is_train

        self.image_paths = []
        for subdir, _, files in os.walk(root_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.image_paths.append(os.path.join(subdir, file))

    def __len__(self):
        return len(self.image_paths)

    def get_item(self):
        return random.sample(self.image_paths, self.batch_size)

    def _show_image(self, batch):
        random_path = random.choice(batch) #
        display(Image(filename=random_path, width=self.width, height=self.height))

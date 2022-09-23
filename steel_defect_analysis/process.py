"""
    A set of functions to pre- and post-process images.

    @author: Dmytro Kuksenko
    @date: Sept 23, 2022
"""

import os

def get_images(data_dir, class_names):

    image_files = [
        [os.path.join(data_dir, class_name, x) for x in os.listdir(os.path.join(data_dir, class_name))] 
        for class_name in class_names
    ]
    
    return image_files
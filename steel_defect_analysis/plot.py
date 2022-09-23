"""
    A set of tool for the visualization of results.

    @author: Dmytro Kuksenko
    @date: Sept 23, 2022
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage


def plot_images(image_files, class_names, im_plot=9):
    
    plt.subplots(3,3, figsize=(8,8))
    plt.title('Visualization of randomly selected images')

    for i in range(im_plot):
        class_idx = np.random.randint(len(class_names))
        img_idx = np.random.randint(len(image_files[class_idx]))
        im = skimage.io.imread(image_files[class_idx][img_idx], as_gray=True)
        plt.subplot(3,3,i+1)
        plt.xlabel(class_names[class_idx])
        plt.imshow(im, cmap='gray')
    
    plt.tight_layout()
    plt.show()


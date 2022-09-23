"""
    Classification of defects in hot rolled surface steel. 

    @author: Dmytro Kuksenko
    @date: Sept 23, 2022

    References:
    
    [1] Cohn, R., Holm, E. Unsupervised Machine Learning aia Transfer Learning 
    and k-Means Clustering to Classify Materials Image Data. 
    Integr Mater Manuf Innov 10, 231–244 (2021). 
    https://doi.org/10.1007/s40192-021-00205-8
"""

import os
from process import get_images
from plot import plot_images

if __name__ == "__main__":

    # set path to a data dir
    data_dir = "data"

    # extract images
    class_names = sorted([x for x in os.listdir(data_dir)])

    image_files = get_images(data_dir, class_names)
    total_im_num = sum([len(x) for x in image_files])

    for name, files in zip(class_names, image_files):
        print(f"Class {name} contains {len(files)} images")

    print(f"Total number of images is {total_im_num}")

    plot_images(image_files, class_names)

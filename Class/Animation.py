import pygame
import numpy as np

def SliceAnimationSheet(imagePath, slice_x, slice_y, direction = "horizontal"):
    """Take an image and slice it in different image to make animation.

    Parameters
    ----------
    imagePath : string
        Absolute or relative path to the image to slice.
    slice_x : int
        Sub-image size on X axis
    slice_y : int
        Sub-image size on Y axis
    direction : string
        'horizontal' or 'vertical'

    Returns
    -------
    Pygame Image Array
        List of all sub-image, with one dimension.
        Example : [image1, image2, image3]
    """
    image = pygame.image.load(imagePath)
    width, height = image.get_width(), image.get_height()
    sub_image_count_x, sub_image_count_y = width % slice_x, height % slice_y
    if sub_image_count_x == 0 and sub_image_count_y == 0:
        sub_image_list = []
        for x in sub_image_count_x:
            for y in sub_image_count_y:
                sub_image_list.append(pygame.transform.chop(image, (slice_x * x, slice_y * y, slice_x * (x + 1), slice_y * (y + 1))))
        sub_image_list = np.array(sub_image_list)
        if direction == 'vertical':
            sub_image_list = np.transpose(sub_image_list)
        return sub_image_list
    else:
        raise Exception(f"Unable to slice image in equal part with these parameters : slice_x = {slice_x}, slice_y = {slice_y}")
        return None

import pygame

class AnimatorController:
    def __init__(self, animation_dict):
        """Init an animator controller for an object, will handle the sprite's animation of your object.

        Parameters
        ----------
        object : Scripts Objects
            An object script
        animation_dict : type
            A dictionnary with all your animation_dict
            Example : {"idle" : [img1, img2, img3], "running_left" : [img 1, img2, img3]}
        """

        self.animation          = animation_array

        self.actual_animation       = None
        self.actual_animation_index = 0

    def update_sprite(self, animation_to_run):
        """Update the sprite of your predefined object.

        Parameters
        ----------
        animation_to_run : str
            The key in the dictionnary corresponding to the animation you want to run.

        Returns
        -------
        sprite
            The surface rect of the corresponding animation
        """
        sprite = None
        if animation_to_run == self.actual_animation:
            sprite = self.animation[animation_to_run][self.actual_animation_index]
            self.actual_animation_index += 1
        else:
            self.actual_animation       = animation_to_run
            self.actual_animation_index = 0
            sprite = self.animation[self.actual_animation][self.actual_animation_index]
        if self.actual_animation_index == len(self.animation[self.actual_animation]):
            self.actual_animation_index = 0
        return sprite

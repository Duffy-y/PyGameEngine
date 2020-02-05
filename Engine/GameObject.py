import os
import sys
import time
from importlib import import_module
sys.path.append(".")

class GameObject:
    scripted_objects    = []
    scripted_classes    = []

    @staticmethod
    def init():
        for r, _, f in os.walk("."):
            for file in f:
                if ".py" in file and ".pyc" not in file and "s_" in file:
                    module_name = r.replace(".\\", "") + "." + file.replace(".py", "")
                    class_name  = file.replace(".py", "").replace("s_", "")
                    module = import_module(module_name)
                    class_imported = getattr(module, class_name)
                    GameObject.scripted_classes.append(class_imported)
                    # GameObject.init_object(GameObject.scripted_classes[0]())

    @staticmethod
    def init_object(object):
        if "transform" in object.__dict__ and "sprite" in object.__dict__:
            object.sprite_rect = object.sprite.get_rect()
            GameObject.scripted_objects.append(object)
            GameObject.scripted_objects  = sorted(GameObject.scripted_objects, key = lambda x: x.transform.position.z)

    @staticmethod
    def destroy(object):
        try:
            index = GameObject.scripted_objects.index(object)
            GameObject.scripted_objects.pop(index)
            del object
        except:
            print(f"Warning : You tried to delete an unexisting object : {object}.")

    @staticmethod
    def update_objects():
        for obj in GameObject.scripted_objects:
            try:
                obj.update()
            except:
                pass

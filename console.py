#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Place": Place,
               "Amenity": Amenity,
               "Review": Review}

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, cls_name):
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[cls_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        commands = arg.split()
        # Reloading data from json file
        storage.reload()
        all_instances = storage.all()

        if not commands:
            print("** class name missing **")
            return
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(commands) <= 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        if not all_instances or key not in all_instances:
            print("** no instance found **")
        else:
            print(all_instances[key])

    def do_destroy(self, arg):
        commands = arg.split()
        # Reloading data from json file
        storage.reload()
        all_instances = storage.all()

        if not commands:
            print("** class name missing **")
            return
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(commands) <= 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        if not all_instances or key not in all_instances:
            print("** no instance found **")
        else:
            del all_instances[key]
            # Saving the new dictionary to the JSON file
            HBNBCommand.save_all_instances(all_instances)

    def do_all(self, arg):
        commands = arg.split()
        all_list = []
        all_instances = storage.all()

        if len(commands) == 0:
            all_list = [obj.__str__() for obj in all_instances.values()]
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif commands[0] in HBNBCommand.classes:
            all_list = [obj.__str__() for obj in all_instances.values()
                        if obj.__class__.__name__ == commands[0]]

        print(all_list)

    def do_update(self, arg):
        commands = arg.split()
        # Reloading data from json file
        storage.reload()
        all_instances = storage.all()

        if not commands:
            print("** class name missing **")
            return
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(commands) <= 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        if not all_instances or key not in all_instances:
            print("** no instance found **")
        elif len(commands) <= 2:
            print("** attribute name missing **")
        elif len(commands) <= 3:
            print("** value missing **")
        else:
            attributeValue = commands[3].replace('"', '')

            if attributeValue.isdigit():
                setattr(all_instances[key], commands[2], int(attributeValue))
            elif HBNBCommand.is_float(attributeValue):
                setattr(all_instances[key], commands[2], float(attributeValue))
            else:
                setattr(all_instances[key], commands[2], attributeValue)

            # Saving the new dictionary to the JSON file
            HBNBCommand.save_all_instances(all_instances)

    def default(self, arg):
        commands = arg.split()
        command_error_msg = "*** Unknown syntax: {}".format(arg)

        if '.' in commands[0]:
            first_command = commands[0].split('.')
            if first_command[0] in HBNBCommand.classes and\
                    first_command[1] == "all()":
                storage.reload()
                all_instances = storage.all()
                inst_list = [obj.__str__() for obj in all_instances.values()
                             if obj.__class__.__name__ == first_command[0]]
                instances_list_len = len(inst_list)
                counter = 0

                print('[', end='')
                for obj in inst_list:
                    print(obj, end='')
                    if counter < instances_list_len - 1:
                        print(', ', end='')
                    counter += 1
                print(']')
            else:
                print(command_error_msg)
        else:
            print(command_error_msg)

    @staticmethod
    def is_float(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False

    @staticmethod
    def save_all_instances(all_instances):
        # Saving the new dictionary to the JSON file
        with open(storage.get_file_path(), 'w') as json_file:
            obj_dict = {k: v.to_dict()
                        for k, v in all_instances.items()}
            json.dump(obj_dict, json_file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

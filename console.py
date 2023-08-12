#!/usr/bin/python3
"""Defines the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for a program, allowing users to interact
    with the application using text-based commands.

    Attributes:
        prompt (str): The command prompt displayed to the use
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line + ENTER shouldn't excute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

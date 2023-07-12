#!/usr/bin/python3
"""defining console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of HBNB console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exits the program"""
        return True

    def do_EOF(self, arg):
        """takes care of EOF"""
        return True

    def emptyline(self):
        """ empty line"""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

#!/usr/bin/python3
"""defining console module"""
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, line):
        """command to create intance of basemodel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ prints string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            argv = line.split(' ')
            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argv[0], argv[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """destorys a basemodel instance based on class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            argv = line.split(' ')
            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argv[0], argv[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ prints string representation of all instances """
        if line != "":
            argv = line.split(" ")
            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                strform = [str(obj) for key, obj in storage.all().items()
                           if type(obj).__name__ == argv[0]]
                print(strform)
        else:
            strform = [str(obj) for key, obj in storage.all().items()]
            print(strform)

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

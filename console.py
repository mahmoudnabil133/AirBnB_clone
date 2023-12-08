#!/usr/bin/python3
"""
comand line interpretter the entry point
of the project where we can create, update, show, deleate opjects
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        "EOF command to exit program"
        print()
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        "to do nothing if user intered empty line"
        pass

    def do_create(self, line):
        """
        used to create a new obj then save it to file
        command should be like that:
        (create) + <class_Name>
        """
        if line:
            if line == "BaseModel":
                obj = BaseModel()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        used to show str reprsentation of obj by its id
        command should be like that:
        (show) + <class_Name> + <obj_id>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            idn = parsed[1]
            if class_name == "BaseModel":
                if idn:
                    full_key = f'BaseModel.{idn}'
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        used to destroy object by its id
        then remove it from json file
        the command should be like that:
        (destroy) + <class_Name> + <obj_id>
        """
        if line:
            "parse line to get class_name and id"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            idn = parsed[1]
            if class_name == "BaseModel":
                if idn:
                    full_key = f'BaseModel.{idn}'
                    dic = storage.all()
                    try:
                        """
                        (How we save changes in file)
                        if you delete obj from var (dic)
                        you are actually deleeting it from __objects dictionary
                        (a private class Attr for FileStorage class)
                        as it points to the same dictionary obj.
                        then when you save a storage you are
                        looping __objects dict and save objects to the file
                        """
                        del (dic[full_key])
                        storage.save()
                    except KeyError:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        used to print str repr of objects of specific class
        or prnit all objects of all classes in storage
        command should be like that:
        (all) + <class_Name> ---> print objects of specific class
        or
        (all) -----> print all objs in the storage
        """
        dic = storage.all()
        if line:
            if line == 'BaseModel':
                for value in dic.values():
                    dic_value = value.to_dict()
                    if dic_value['__class__'] == 'BaseModel':
                        print(value)
            else:
                print("** class doesn't exist **")

        else:
            for value in dic.values():
                print(value)

    def do_update(self, line):
        """
        used to update objects by its id
        the command should be like that:
        (update) <class_Name>  <obj_id>  <attribute_name> "<attribute value>"
        if user put more attributes and its values we will ignore.
        """
        if line:
            """
            parse to get <class_name> and the others
            (others)--> is  <obj_id> + <attribute_name> + "<attribute value>"
            """
            parsed_1 = cmd.Cmd.parseline(self, line)
            class_name = parsed_1[0]
            others = parsed_1[1]
            if class_name == "BaseModel":
                if others:
                    """
                    to optain <obj_id> we will take first 35 char of others
                    as you know id contains 32 (char) with 3 (-)
                    """
                    id = others[:36]
                    full_key = f"BaseModel.{id}"
                    "handle if object found or not"
                    try:
                        dic = storage.all()
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                    """
                    after we optained <obj_id> from others
                    the remain will be <attr_name> <attr_value> (and me be
                    other attributees but we will ignore them)"
                    """
                    key_val_others = others[36:]
                    "parse remain to optain <key> and \"<value>\""
                    parsing_touples = cmd.Cmd.parseline(self, key_val_others)
                    key = parsing_touples[0]
                    if key:
                        value_others = parsing_touples[1]
                        "to avoid parsing character (\") we will ignore it"
                        val_oth2 = value_others[1:]
                        """
                        step below to aptain just a value as we may have other
                        attributes so we will parse remaining
                        and take just a value
                        """
                        pars2 = cmd.Cmd.parseline(self, val_oth2)
                        value = pars2[0]
                        if value:
                            """now we have obj and <key>, <val>
                            --> setattr and save to json file"""
                            setattr(obj, key, value)
                            obj.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

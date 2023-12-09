#!/usr/bin/python3
"""
comand line interpretter the entry point
of the project where we can create, update, show, deleate opjects
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes_list = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review",
]


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

    def precmd(self, line):
        """
        do some changes on the line to prepare it to be excuted
        input line will be like that:
        User.show(<id>),
        User.update(<id>, "attr_name", "attr_value")
        output is supposed to be like that:
        show User <id>,
        update User <id> attr_name "attr_value"
        """
        id = ''
        list_attrs = []
        attr_name = ''
        attr_value = ''
        "handle if line contains ."
        if '.' in line:
            parse_line = line.split('.')
            "separate command from class_name"
            class_name = parse_line[0]
            big_comand = parse_line[1]
            "command is unsparated from () so we will separate them"
            "handle if the user put parenthese or not"
            if '(' in big_comand:
                list_command_attributes = big_comand.split('(')
                command = list_command_attributes[0]
                attrs_R_parenthese = list_command_attributes[1]
                "handle if user put command without right parenthese )"
                if not attrs_R_parenthese:
                    return cmd.Cmd.precmd(self, line)
                attrs = attrs_R_parenthese.split(')')[0]
                "now we have all attributes without parentheses"
                """and if user didn't put attrs-->\
                    remaining = '' , line = comand + class_name"""
                if attrs:
                    list_attrs.append(attrs)
                    if ',' in attrs:
                        list_attrs = attrs.split(',')
                    "now we have all attributes separated in (list_attr)"
                    id = list_attrs[0]
                    "optain id without \""
                    if "\"" in list_attrs[0]:
                        id = list_attrs[0].split('\"')[-2]
                    "handle update attributes"
                    if len(list_attrs) > 1:
                        "you are in update"
                        attr_name = list_attrs[1]
                        "optain attr_name without \""
                        if "\"" in attr_name:
                            attr_name = attr_name.split("\"")[-2]
                        if len(list_attrs) > 2:
                            attr_value = list_attrs[2]
                            attr_value = attr_value.split(' ')[-1]
                """
                now we have attributes wich user intered in the console
                and the other attributes is empty string.
                """
                attributes = id + ' ' + attr_name + ' ' + attr_value

                line = command + ' ' + class_name + ' ' + attributes
            else:
                return cmd.Cmd.precmd(self, line)

        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """
        used to create new object
        the command should be like that:
        (create) + <class_Name>
        """
        if line:
            "parse line to separate class name"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            if class_name in classes_list:
                new_obj = eval(class_name)()
            else:
                print("** class doesn't exist **")
                return
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        used to show object by its id
        command should be like that:
        (show) + <class_Name> + <obj_id>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            idn = parsed[1]
            if class_name in classes_list:
                if idn:
                    full_key = f"{class_name}.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        used to delete object by its id
        command should be like that:
        (destroy) + <class_Name> + <obj_id>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            idn = parsed[1]
            if class_name in classes_list:
                if idn:
                    full_key = f"{class_name}.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            if class_name in classes_list:
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == class_name:
                        print(value)
            else:
                print("** class doesn't exist **")
                return
        else:
            dic = storage.all()
            for key, value in dic.items():
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
            if class_name in classes_list:
                if others:
                    splited_attrs = others.split(' ')
                    update_attrs = []
                    "to remove empty string from splited_attrs"
                    for val in splited_attrs:
                        if val:
                            update_attrs.append(val)
                    id = update_attrs[0]
                    key = ''
                    value = ''
                    if len(update_attrs) > 1:
                        key = update_attrs[1]
                        if len(update_attrs) > 2:
                            value = update_attrs[2]
                    full_key = f"{class_name}.{id}"
                    "handle if object found or not"
                    try:
                        dic = storage.all()
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if key:
                        if value:
                            """now we have obj and <key>, <val>
                            --> setattr and save to json file"""
                            if "\"" in value:
                                value = value.split('\"')[1]
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

    def do_count(self, line):
        """
        used to show all objects
        command should be like that:
        (all) + <class_Name>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0]
            if class_name in classes_list:
                dic = storage.all()
                count = 0
                for key, value in dic.items():
                    if key.split(".")[0] == class_name:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
                return
        else:
            dic = storage.all()
            for key, value in dic.items():
                print(value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

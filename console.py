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
        used to create new object
        the command should be like that:
        (create) + <class_Name>
        """
        if line:
            "parse line to separate class name"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0].lower()
            if class_name == "basemodel":
                new_obj = BaseModel()
            elif class_name == "user":
                new_obj = User()
            elif class_name == "state":
                new_obj = State()
            elif class_name == "city":
                new_obj = City()
            elif class_name == "amenity":
                new_obj = Amenity()
            elif class_name == "place":
                new_obj = Place()
            elif class_name == "review":
                new_obj = Review()
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
            class_name = parsed[0].lower()
            idn = parsed[1]
            if class_name == "basemodel":
                if idn:
                    full_key = f"BaseModel.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "user":
                if idn:
                    full_key = f"User.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "state":
                if idn:
                    full_key = f"State.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "city":
                if idn:
                    full_key = f"City.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "amenity":
                if idn:
                    full_key = f"Amenity.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "place":
                if idn:
                    full_key = f"Place.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "review":
                if idn:
                    full_key = f"Review.{idn}"
                    dic = storage.all()
                    try:
                        print(dic[full_key])
                    except KeyError:
                        print("** no instance found **")
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
            class_name = parsed[0].lower()
            idn = parsed[1]
            if class_name == "basemodel":
                if idn:
                    full_key = f"BaseModel.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "user":
                if idn:
                    full_key = f"User.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "state":
                if idn:
                    full_key = f"State.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "city":
                if idn:
                    full_key = f"City.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "amenity":
                if idn:
                    full_key = f"Amenity.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "place":
                if idn:
                    full_key = f"Place.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            elif class_name == "review":
                if idn:
                    full_key = f"Review.{idn}"
                    dic = storage.all()
                    try:
                        del dic[full_key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        used to show all objects
        command should be like that:
        (all) + <class_Name>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0].lower()
            if class_name == "basemodel":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "BaseModel":
                        print(value)
            elif class_name == "user":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "User":
                        print(value)
            elif class_name == "state":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "State":
                        print(value)
            elif class_name == "city":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "City":
                        print(value)
            elif class_name == "amenity":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "Amenity":
                        print(value)
            elif class_name == "place":
                dic = storage.all()
                for key, value in dic.items():
                    if key.split(".")[0] == "Place":
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
        used to update object by its id
        command should be like that:
        (update) + <class_Name> + <obj_id> + <attribute_name> + <attribute_value>
        """
        if line:
            "parse line to separate class name and id in a touple"
            parsed = cmd.Cmd.parseline(self, line)
            class_name = parsed[0].lower()
            idn = parsed[1]
            if class_name == "basemodel":
                if idn:
                    full_key = f"BaseModel.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif class_name == "user":
                if idn:
                    full_key = f"User.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif class_name == "state":
                if idn:
                    full_key = f"State.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif class_name == "city":
                if idn:
                    full_key = f"City.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif class_name == "amenity":
                if idn:
                    full_key = f"Amenity.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif class_name == "place":
                if idn:
                    full_key = f"Place.{idn}"
                    dic = storage.all()
                    try:
                        obj = dic[full_key]
                    except KeyError:
                        print("** no instance found **")
                        return
                    if len(parsed) == 4:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                    elif len(parsed) == 5:
                        if parsed[2] == "created_at":
                            obj.created_at = parsed[3]
                        elif parsed[2] == "updated_at":
                            obj.updated_at = parsed[3]
                        else:
                            print("** attribute name missing **")
                            return
                        obj.save()
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** instance id missing **")
                    return
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()

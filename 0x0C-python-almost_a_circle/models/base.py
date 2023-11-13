#!/usr/bin/python3
'''module for base class'''


class Base:
    ''' manage id attribute in all your future classes'''


    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''jsonifiles Dictionary'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save json obj'''
        if list_objs is not None:
            list_objs  = [o.to_dictionaries() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8")as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''loads instance from dictionary'''
        from models.rectangle import Rectangle
        from models.square import Square 
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''loads string from file and unjsonifiles'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.creat(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save obj to csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]for o in list_objs]
        with open ('{}.csv'.format(cls.__name__), 'w', newline='', encoding='utf-8')as f:
                    writer = csv.writer(f)
                    writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        ''''''

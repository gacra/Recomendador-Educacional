class Field(object):
    '''
    Class Field
    '''


class Item(dict):
    fields = None

    def __init__(self, *args, **kwargs):
        self.fields = set()

        for attr_name in dir(self):
            attr = getattr(self, attr_name)

            if isinstance(attr, Field):
                self.fields.add(attr_name)

        if args and isinstance(args[0], dict):
            dict_args = dict(args[0])
            dict_args.update(kwargs)
            kwargs = dict_args

        for field in self.fields:
            dict.__setitem__(self, field, kwargs.get(field, self.get(field)))

    # When used as dict
    def __setitem__(self, key, value):
        if isinstance(object.__getattribute__(self, key), Field):
            dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    # When used as class
    def __setattr__(self, name, value):
        if isinstance(object.__getattribute__(self, name), Field):
            dict.__setitem__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        try:
            return dict.__getitem__(self, name)
        except KeyError:
            return object.__getattribute__(self, name)

    def keys(self):
        return self.fields

    def copy(self):
        return self.__class__(self)

    def __len__(self):
        return len(self.fields)

    def __delitem__(self, key):
        setattr(self, key, None)


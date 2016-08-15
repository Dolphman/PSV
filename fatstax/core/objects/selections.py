from ..utils import cleanup_name
from types import FunctionType

class Selection(object):

    __slots__ = ["__rows__"]


    def __init__(self, selection):
        self.__rows__ = (selection)
        if not self.rows:
            Exception("Selection Error")

    @property
    def rows(self):
        if not isinstance(self.__rows__, tuple):
            self.__rows__ = tuple(self.__rows__)
            return self.__rows__
        else:
            return self.__rows__

    @property
    def columns(self):
        return tuple(self.rows[0].keys())

    def single_find(self, func):
        try:
            g = self._find_all(func)
            result = next(g)
            next(g)
            raise Exception("Function returned more than 1 result")
        except StopIteration:
            return result

    def find(self, func):
        try:
            g = self._find_all(func)
            return next(g)
        except StopIteration:
            return None

    def _find_all(self, func):
        for x in self.rows:
            if func(x):
                yield x

    def find_all(self, func):
        return tuple(self._find_all(func))

    def flipoutput(self):
        for x in self.rows:
            ~x
        return self

    def no_output(self):
        for x in self.rows:
            -x
        return self

    def all_output(self):
        for x in self.rows:
            +x
        return self

    def lenoutput(self):
        return len(tuple(filter(lambda x: x.outputrow, self.rows)))

    def enable(self, v):
        for x in self.rows:
            if bool(v(x)):
                +x
    def disable(self, v):
        for x in self.rows:
            if bool(v(x)):
                -x
                
    def __getattr__(self, attr):
        s = cleanup_name(attr)
        if attr in self.columns:
            return self[attr]
        if s in self.columns:
            raise AttributeError((
                "{}{}"
                .format(
                '\'{}\' has no attribute \'{}\''.format(
                    type(self), attr),
                ". However, '{s}' is an existing condensed ".format(s=s) + 
                "column name. Only the condensed version is supported."
                .format(s=s)
                )))
        else:
            raise AttributeError('\'{}\' has no attribute \'{}\''.format(
        type(self), attr))

    def __getitem__(self, v):
        if isinstance(v, slice):
            return Selection(self.rows[v])
        if isinstance(v, int):
            return (self.rows[v])
        elif isinstance(v, str):
            return (x.getcolumn(v) for x in self.rows)
        elif isinstance(v, tuple):
            return (multiple_index(x,v) for x in self.rows)
        elif isinstance(v, FunctionType):
            return Selection(_index_function_gen(self, v))
        else:
            raise TypeError("Row indices must be int, slices, str, tuple, or functions. Not {}".format(type(v)))
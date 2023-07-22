# -*- coding: utf-8 -*-

"""
todo: doc string here
"""


class BaseMixin:
    @property
    def sort_key(self) -> str:  # pragma: no cover
        """
        a string that can be used to sort, detect equal, hash this object.
        """
        raise NotImplementedError

    def __hash__(self):  # pragma: no cover
        """
        Copy the following snippet to all subclass of this. Attrs will remove
        the __hash__ method when you subclass it.
        See https://www.attrs.org/en/stable/hashing.html

            def __hash__(self):
                return hash(self.sort_key)
        """
        # raise NotImplementedError
        return hash(self.sort_key)

    def __eq__(self, other): # pragma: no cover
        """
        Copy the following snippet to all subclass of this. Attrs will remove
        """
        return self.sort_key == other.sort_key

    def __gt__(self, other): # pragma: no cover
        """
        Copy the following snippet to all subclass of this. Attrs will remove
        """
        return self.sort_key > other.sort_key

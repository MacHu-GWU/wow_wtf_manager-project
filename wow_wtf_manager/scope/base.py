# -*- coding: utf-8 -*-

"""
该模块定义了所有的作用域类的基类. 所有的作用域类都必须继承自该基类. 该基类不应该被直接使用.
"""


class BaseScope:
    """
    Base class for all scope classes. This class should not be used directly.
    """

    def apply(
        self,
        dry_run: bool = True,
        **kwargs,
    ):
        """
        Abstract method, apply configuration to this scope
        """
        msg = (
            f"You may forget to implement the ``apply()` method. For example:\n"
            f"\n"
            f"class {self.__class__.__name__}(BaseScope):\n"
            f"    def apply(self, dry_run: bool = True, **kwargs):\n"
            f"        ...\n"
        )
        raise NotImplementedError(msg)

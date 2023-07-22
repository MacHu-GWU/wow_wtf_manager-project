# -*- coding: utf-8 -*-

"""
该模块定义了所有的配置类的基类. 所有的配置类都必须继承自该基类. 该基类不应该被直接使用.
"""

import typing as T


class BaseConfig:
    """
    Base class for all config classes. This class should not be used directly.
    """

    # --------------------------------------------------------------------------
    # NOTE:
    #
    # below are abstract methods, they are commented out intentionally as a reference
    # --------------------------------------------------------------------------
    def build(
        self,
        **kwargs,
    ) -> str:
        """
        Build final configuration data from template and parameters.
        """
        msg = (
            f"You may forget to implement the ``build()` method. For example:\n"
            f"\n"
            f"class {self.__class__.__name__}(BaseConfig):\n"
            f"    def build(self, **kwargs):\n"
            f"        ...\n"
        )
        raise NotImplementedError(msg)

    def apply(
        self,
        dry_run: bool = True,
        **kwargs,
    ):
        """
        Abstract method, apply configuration to the target scope
        """
        msg = (
            f"You may forget to implement the ``apply()` method. For example:\n"
            f"\n"
            f"class {self.__class__.__name__}(BaseConfig):\n"
            f"    def apply(self, dry_run: bool = True, **kwargs):\n"
            f"        ...\n"
        )
        raise NotImplementedError(msg)

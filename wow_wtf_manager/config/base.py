# -*- coding: utf-8 -*-

import typing as T


class BaseConfig:
    """
    Base class for all config classes.
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
        raise NotImplementedError

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

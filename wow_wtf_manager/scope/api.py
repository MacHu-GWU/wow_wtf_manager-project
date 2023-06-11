# -*- coding: utf-8 -*-

"""
Example::

    from wow_wtf_manager.scope.api import ...
"""

from .base import BaseScope
from .client import (
    # client level
    ClientScope,
    # account level
    AccountKeyBindingScope,
    AccountUserInterfaceScope,
    AccountAddonSavedVariablesScope,
    # character level
    CharacterUserInterfaceScope,
    CharacterChatScope,
    CharacterKeyBindingScope,
    CharacterLayoutScope,
    CharacterAddonsScope,
    CharacterAddonSavedVariablesScope,
)

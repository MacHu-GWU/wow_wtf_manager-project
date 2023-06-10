# -*- coding: utf-8 -*-

import platform

IS_WINDOWS = False
IS_MACOS = False
IS_LINUX = False
OS_NAME = None


class OSEnum:
    WINDOWS = "Windows"
    MACOS = "MacOS"
    LINUX = "Linux"
    AMAZON_LINUX = "Amazon Linux"
    CENTOS = "CentOS"
    REDHAT = "Redhat"
    FEDORA = "Fedora"
    UBUNTU = "Ubuntu"
    DEBIAN = "Debian"


platform_system = platform.system()
if platform_system == "Windows":
    IS_WINDOWS = True
    OS_NAME = OSEnum.WINDOWS
elif platform_system == "Darwin":
    IS_MACOS = True
    OS_NAME = OSEnum.MACOS
elif platform_system == "Linux":
    IS_LINUX = True
    OS_NAME = OSEnum.LINUX
else:
    raise NotImplementedError

# -*- coding: utf-8 -*-

import platform

IS_WINDOWS = False
IS_MACOS = False
OS_NAME = None


class OSEnum:
    WINDOWS = "Windows"
    MACOS = "MacOS"
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
else:
    raise NotImplementedError

Project Folder Structure 项目文件目录结构
==============================================================================
该项目是一个 Git 仓库, 本文介绍了里面的文件都是做什么的.


目录结构
------------------------------------------------------------------------------
该项目是一个 Python 项目, 所以它符合标准的 Python 项目结构规范. Git 仓库名称是 ``wow_wtf_manager-project``, 我们称这个目录为项目根目录, 之后用 ``${dir_project_root}`` 或 ``root`` 来指代.

- ``root/wow_wtf_manager``: 项目的 Python 库, 也是该项目的核心源代码. 实现了业务逻辑和各种抽象, 但不储存任何数据.
- ``root/tests``: 对核心源代码的单元测试. 不涉及该项目具体的应用, 只测试该项目的各种实现是否正确, 有没有 Bug.
- ``root/docs``: 该项目的文档.
- ``root/app``: 以 ``wow_wtf_manager`` Python 库为基础构建的 App. 用于管理一些具体服务器上, 具体账号, 具体人物角色的 WTF 配置. 主要储存数据, 而不是业务逻辑.
- ``root/tests_int``: 对 ``root/app`` 中的具体业务逻辑做集成测试, 确保在持续迭代的过程中不破话已有的逻辑.

由于魔兽世界有很多个资料片, 而且我也不止在一个服务器上玩, 具体的配置区别也很大. 所以在你会看到很多按照资料片, 服务器呈树状结构的目录. 其中 ``wow_wtf_manager`` 和 ``tests`` 里的文件一一对应. 因为核心源代码中的所有模块都需要有对应的单元测试. 而 ``wow_wtf_manager/app`` (没写错, 是 ``wow_wtf_manager/app`` 而不是 ``app``, 下一节会详细说) 和 ``tests_int`` 里的文件一一对应, 因为 ``wow_wtf_manager/app`` 里的的是具体服务器上的逻辑, 需要被集成测试.

``wow_wtf_manager`` Python 库是整个项目的重中之重, 90% 的业务逻辑都在里面. 下面我们重点说一下这个目录结构.


``wow_wtf_manager`` 源代码目录结构
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
该目录是 WTF manager 的源代码. 按照用途, 分为 **底层代码** 和 **应用层代码**. 底层代码指的是不涉及具体的应用逻辑, 而是作为工具给开发应用提供方便. 而应用层代码则是为最终的配置管理应用而服务器的, 具体到真实的配置数据, 真实的账号, 游戏角色.

底层代码也分为 **通用型** 和 **专用型**. 由于魔兽世界有多个资料片, 这些资料片的配置管理方式非常相似, 但仍有细微不同. 通用型代码实现了适用于所有资料片的逻辑, 而专用型代码则是针对某个特定的资料片. 专用型代码会通过 import, 类继承等机制复用通用型代码.

我们按照这个框架来介绍一下涉及的具体模块.

**底层通用型模块**

- ``wow_wtf_manager/models``: 最底层的数据模型, 相当于是一个工具包. 所有的稳定功能都可以从 ``wow_wtf_manager/models/api.py`` 导入.
- ``wow_wtf_manager/config``: 跟配置数据有关的抽象, 相当于是一个工具包. 所有的稳定功能都可以从 ``wow_wtf_manager/config/api.py`` 导入.
- ``wow_wtf_manager/scope``: 跟作用域有关的抽象, 相当于是一个工具包. 所有的稳定功能都可以从 ``wow_wtf_manager/scope/api.py`` 导入.

**底层专用型模块**

- ``wow_wtf_manager/exp/`` 模块对于不同的资料片的将核心逻辑用抽象类, 方法来实现. 它不涉及到具体的服务器, 具体的配置, 具体的宏. 例如它不会实现你在巫妖王之怒官方怀旧服上具体的角色名, 具体的宏命令. 这个模块里面又按照资料片分成了多个子模块. 这是因为不同的资料片 WTF 的目录结构, 文件格式什么的都不一样, 需要为不同的资料片设计单独的模块. 具体的目录结构是 ``wow_wtf_manager/exp/${expansion_name}``.
    - ``wow_wtf_manager/exp/e03_wotlk`` 例如这是巫妖王之怒版本的底层模块, 定义了巫妖王之怒版本的配置文件列表, 格式等信息.
    - ``wow_wtf_manager/exp/e05_mop`` 这是熊猫人之迷版本的底层模块, 定义了熊猫人之谜版本的配置文件列表, 格式等信息.

**应用层代码**

- ``wow_wtf_manager/app/`` 模块则是以 ``exp`` 模块为基础, 为你在具体的服务器上, 做具体的配置, 管理具体的宏. 它下面有很多个并列的文件夹, 每一个文件夹代表着一个项目. 这个项目名称一般遵循 ``${expansion_name}_${realm_name}`` 的格式. 例如我在我自己的 example 巫妖王之怒服务器上的 server name 就是 ``e03_wotlk_example``. 你在里面可以看到我具体在这个服务器上有什么角色, 它们的配置都是怎么样的. 该目录是以 ``modules``, ``config``, ``scope``, ``exp`` 中的底层模块为基础构建的 App. 主要用于枚举在该项目中所有可用的配置, 以及所有的账号和角色, 以及配置和账号角色的对应关系.


应用层源代码目录结构
------------------------------------------------------------------------------
这里我们以示例项目 ``e03_wotlk_example`` 为例. 该项目是基于本项目开发的一个用于管理我在一个巫妖王之怒服务器上的所有账号角色的配置管理工具. 每个类似于这样的项目都有两个关键目录:

1. **数据文件目录**: 位于 ``app/e03_wotlk_example/`` 目录下. 所谓数据文件就是具体的配置文件模板, 插件 lua 文件的拷贝, 宏命令的拷贝等等.
2. **配置管理源代码**: 位于 ``wow_wtf_manager/app/e03_wotlk_example`` 目录下. 所谓源代码就是指将这些数据文件组合起来的逻辑代码实现.

下面我们一一来讲解一下这两个目录的结构:

**数据文件目录**

- ``app/e03_wotlk_example/01_game_client``: 游戏客户端的配置, 分辨率, 图像, 声音, 国家地区等.
- ``app/e03_wotlk_example/11_account_user_interface``: 账号级的用户界面配置.
- ``app/e03_wotlk_example/12_account_keybindings``: 该目录已废弃, 账号级的按键绑定配置. 现在全部的按键绑定配置都是角色级的.
- ``app/e03_wotlk_example/13_account_saved_variables``: 账号级的插件数据.
- ``app/e03_wotlk_example/14_account_macro``: 该目录已废弃, 原本是账号级的宏命令管理, 而现在的宏命令管理已经全部交给了 SDM 插件, 所以不再需要.
- ``app/e03_wotlk_example/21_character_user_interface``: 角色级的用户界面配置.
- ``app/e03_wotlk_example/22_character_chat``: 角色级的聊天配置.
- ``app/e03_wotlk_example/23_character_keybindings``: 角色级的按键绑定配置.
- ``app/e03_wotlk_example/24_character_layout``: 角色级的界面布局配置.
- ``app/e03_wotlk_example/25_character_addons``: 角色级的插件管理, 开启哪些关闭哪些.
- ``app/e03_wotlk_example/26_character_macro``: 该目录已废弃, 原本是角色级的宏命令管理, 而现在的宏命令管理已经全部交给了 SDM 插件, 所以不再需要.
- ``app/e03_wotlk_example/27_character_saved_variables``: 角色级的插件数据管理.
- ``app/e03_wotlk_example/31_myslots``: 每个角色的动作条按钮配置.
- ``app/e03_wotlk_example/32_SuperDuperMacro``: SDM 插件的宏命令配置.
- ``app/e03_wotlk_example/32_SuperDuperMacro/run.py``: 将 SDM 插件的宏命令配置应用到游戏客户端的 WTF 目录中.
- ``app/e03_wotlk_example/run.py``: 运行该脚本可将所有的配置应用到游戏客户端的 WTF 目录中.

**配置管理源代码**

- ``wow_wtf_manager/app/e03_wotlk_example/config/...``: 对数据文件目录中的配置文件进行管理的源代码, 主要是用变量对其一一进行枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/config/client_level.py``: 对 client 级的配置文件进行枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/config/account_level.py``: 对 account 级的配置文件进行枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/config/character_level.py``: 对 character 级的配置文件进行枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/...``: 对配置文件的作用域进行管理的源代码, 主要是枚举账号, 服务器, 角色, 并对它们进行分组.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/enum.py``: 对单个的账号, 服务器, 角色进行枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/group.py``: 将账号, 服务器, 角色进行分组, 以便于批量管理.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/setup.py``: 将 ``config`` 和 ``scope`` 中的代码 import 进来, 对其进行排列组合, 完成 setup.

**SDM 宏命令管理源代码**

- ``wow_wtf_manager/app/e03_wotlk_example/scope/sdm_macro_generator.py``: 扫描 ``app/e03_wotlk_example/32_SuperDuperMacro`` 目录中的宏命令数据文件, 自动生成对它们进行枚举的源代码.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/sdm_macro.py``: 被 ``sdm_macro_generator.py`` 自动生成的源代码, 对所有的宏命令数据文件进行了枚举.
- ``wow_wtf_manager/app/e03_wotlk_example/scope/sdm_setup.py``: 将 scope 中的角色枚举和宏命令枚举进行排列组合, 决定每个角色用什么宏.

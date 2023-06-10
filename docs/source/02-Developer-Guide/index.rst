
Developer Guide (开发者指南)
------------------------------------------------------------------------------


项目目录结构
------------------------------------------------------------------------------
该项目是一个 Git 仓库. 里面有几个重要的文件夹

- ``wow_wtf_manager-project/wow_wtf_manager``: 该项目的核心源代码.
- ``wow_wtf_manager-project/tests``: 对核心源代码的单元测试. 不涉及该项目具体的应用, 只测试该项目的各种实现是否符合逻辑)
- ``wow_wtf_manager-project/tests_int``: 对核心源代码的集成测试. 对使用该项目解决具体问题的应用进行测试, 看看是否真的解决了该问题.
- ``wow_wtf_manager-project/docs``: 该项目的文档
- ``wow_wtf_manager-project/app``



``wow_wtf_manager`` 目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
该目录是 WTF manager 的核心源代码. 里面最为重要的是 ``exp`` 和 ``app`` 的两个子模块.

- ``wow_wtf_manager/exp/`` 模块对于不同的资料片的将核心逻辑用抽象类, 方法来实现. 它不涉及到具体的服务器, 具体的配置, 具体的宏. 例如它不会实现你在巫妖王之怒官方怀旧服上具体的角色名, 具体的宏命令. 这个模块里面又按照资料片分成了多个子模块. 这是因为不同的资料片 WTF 的目录结构, 文件格式什么的都不一样, 需要为不同的资料片设计单独的模块. 具体的目录结构是 ``wow_wtf_manager/exp/${expansion_name}``, 例如巫妖王之怒版本的目录是 ``wow_wtf_manager/exp/e03_wotlk``.
- ``wow_wtf_manager/app/`` 模块则是以 ``exp`` 模块为基础, 为你在具体的服务器上, 做具体的配置, 管理具体的宏. 它的目录结构是 ``wow_wtf_manager/app/${server_name}``, 这个 server name 就是具体的服务器名字. 我的 server name 一般遵循 ``${expansion_name}_${realm_name}`` 的格式. 例如我在我自己的 Azerothcore 巫妖王之怒服务器上的 server name 就是 ``e03_wotlk_acore``. 你在里面可以看到我具体在这个服务器上有什么角色, 它们的配置都是怎么样的.
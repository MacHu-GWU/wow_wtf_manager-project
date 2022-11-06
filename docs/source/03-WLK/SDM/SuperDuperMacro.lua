sdm_version = "1.8.3"
sdm_listFilters = {
	["true"] = true,
	["s"] = true,
	["b"] = true,
	["false"] = true,
	["global"] = true,
	["f"] = true,
}
sdm_iconSize = 36
--[[
sdm_mainContents 这是一个有序列表数据结构, 列出了所有的 Macro 在游戏 UI 中的顺序.
里面的每一个元素是 Macro ID
--]]
sdm_mainContents = {
	0,
	1,
}
--[[
sdm_macros 这是一个字典结构, 枚举了所有已经定义了的宏命令. 每个宏命令的编号就是 ID.
这里不允许有相同的 ID. 并且这个 ID 非常重要, 是你储存在服务端动作条上所放的宏命令的 ID.
如果你动作条上已经放了一个宏命令, 但是之后你手动修改了 ID, 虽然内容还是同一个宏, 但是动作条
上的按钮将消失.
--]]
sdm_macros = {
	[0] = {
		["type"] = "b",
		["name"] = "Act1",
		["ID"] = 0,
		["text"] = "/s act1",
		["icon"] = 1,
	},
	[1] = {
		["type"] = "b",
		["name"] = "Act2",
		["ID"] = 1,
		["text"] = "/s act2",
		["icon"] = 1,
	},
}

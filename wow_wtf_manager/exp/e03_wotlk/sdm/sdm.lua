
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
sdm_mainContents = {
	1, -- [1]
	0, -- [2]
}
sdm_macros = {
	{
		["type"] = "f",
		["name"] = "asdf-0123-asdf_asdf",
		["character"] = {
			["name"] = "Rk",
			["realm"] = "AzerothCore",
		},
		["ID"] = 1,
		["text"] = "/s hello",
		["icon"] = 1,
	}, -- [1]
	[0] = {
		["type"] = "b",
		["name"] = "MB-Special1",
		["ID"] = 0,
		["text"] = "#showtooltip\n1234\n# ICC 1 瑪洛嘉領主\n/target 瑪洛嘉領主\n/target 骸骨尖刺\n\n# ICC 4 萨鲁法尔\n#/target 血獸\n/castsequence 憤怒,星火術\n",
		["icon"] = 1,
	},
}

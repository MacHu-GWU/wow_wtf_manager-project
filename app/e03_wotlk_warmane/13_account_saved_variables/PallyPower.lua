
PallyPowerDB = {
	["profiles"] = {
		["MyDefault"] = {
			["freeassign"] = 1,
			["autobuff"] = {
				["autokey1"] = false,
				["autokey2"] = "9",
			},
			["display"] = {
				["frameLocked"] = true,
			},
			["disable"] = false,
		},
		["class/Paladin"] = {
		},
	},
	["currentProfile"] = {
		{%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
}
PallyPower_Assignments = {
	["Qsa"] = {
		0, -- [1]
		0, -- [2]
		0, -- [3]
		0, -- [4]
		4, -- [5]
		0, -- [6]
		0, -- [7]
		0, -- [8]
		0, -- [9]
		0, -- [10]
		0, -- [11]
	},
	["Glowyy"] = {
		2, -- [1]
		2, -- [2]
		1, -- [3]
		1, -- [4]
		1, -- [5]
		1, -- [6]
		1, -- [7]
		1, -- [8]
		1, -- [9]
		2, -- [10]
		2, -- [11]
	},
	["Qsb"] = {
		0, -- [1]
		0, -- [2]
		0, -- [3]
		0, -- [4]
		2, -- [5]
		0, -- [6]
		0, -- [7]
		0, -- [8]
		0, -- [9]
		0, -- [10]
		0, -- [11]
	},
	["Batlefury"] = {
		3, -- [1]
		3, -- [2]
		3, -- [3]
		3, -- [4]
		4, -- [5]
		3, -- [6]
		3, -- [7]
		3, -- [8]
		3, -- [9]
		4, -- [10]
		3, -- [11]
	},
	["Qsc"] = {
		0, -- [1]
		0, -- [2]
		0, -- [3]
		0, -- [4]
		3, -- [5]
		0, -- [6]
		0, -- [7]
		0, -- [8]
		0, -- [9]
		0, -- [10]
		0, -- [11]
	},
	["Qse"] = {
		0, -- [1]
		0, -- [2]
		0, -- [3]
		0, -- [4]
		1, -- [5]
		0, -- [6]
		0, -- [7]
		0, -- [8]
		0, -- [9]
		0, -- [10]
		0, -- [11]
	},
	["Qsd"] = {
		0, -- [1]
		0, -- [2]
		0, -- [3]
		0, -- [4]
		0, -- [5]
		0, -- [6]
		0, -- [7]
		0, -- [8]
		0, -- [9]
		0, -- [10]
		0, -- [11]
	},
}
PallyPower_NormalAssignments = {
	["Qsc"] = {
	},
	["Qse"] = {
	},
	["Qsd"] = {
	},
	["Qsb"] = {
	},
}
PallyPower_AuraAssignments = {
	["Qsa"] = 1,
	["Qsb"] = 2,
	["Qsc"] = 7,
	["Qse"] = 3,
	["Qsd"] = 5,
}
PallyPower_SavedPresets = {
}

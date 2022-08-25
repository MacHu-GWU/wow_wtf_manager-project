
MapsterDB = {
	["namespaces"] = {
		["GroupIcons"] = {
		},
		["Coords"] = {
		},
		["FogClear"] = {
			["profiles"] = {
				["MyDefault"] = {
					["version"] = 1,
				},
			},
		},
		["BattleMap"] = {
		},
	},
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["point"] = "CENTER",
			["scale"] = 1.088940024375916,
			["x"] = -12.46296433374118,
			["y"] = -37.15286228670789,
		},
	},
}

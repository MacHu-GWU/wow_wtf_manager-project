
oCCDB = {
	["profileKeys"] = {
		{%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["tscd"] = {
				["lock"] = true,
				["enable"] = false,
			},
			["notify"] = {
				["scale"] = 0.5,
				["y"] = 259.1017037928452,
				["x"] = 468.5910979920071,
				["lock"] = true,
			},
		},
	},
}

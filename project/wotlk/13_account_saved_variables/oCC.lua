
oCCDB = {
	["profileKeys"] = {
		{%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["notify"] = {
				["scale"] = 0.5,
				["x"] = 468.5910979920071,
				["y"] = 259.1017037928452,
				["lock"] = true,
			},
		},
	},
}

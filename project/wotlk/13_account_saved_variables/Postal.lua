
Postal3DB = {
	["global"] = {
		["BlackBook"] = {
			["alts"] = {
			},
		},
	},
	["profileKeys"] = {
		{%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["BlackBook"] = {
				["recent"] = {
					{%- for character in all_characters %}
					"{{ character.character }}",
					{%- endfor %}
				},
			},
		},
	},
}

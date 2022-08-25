
SkadaDB = {
	["namespaces"] = {
		["LibDualSpec-1.0"] = {
		},
	},
	["hasUpgraded"] = true,
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["windows"] = {
				{
					["y"] = 152.5002288818359,
					["point"] = "BOTTOMRIGHT",
					["mode"] = "Damage",
					["x"] = 0,
				}, -- [1]
			},
		},
	},
}


RatingBusterDB = {
	["namespaces"] = {
		["LibDualSpec-1.0"] = {
		},
	},
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["showItemID"] = true,
		},
	},
}

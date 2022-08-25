
AtlasLootCharDB = {
	["namespaces"] = {
		["WishList"] = {
		},
	},
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["AtlasLootVersion"] = "70703",
}

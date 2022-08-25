
AtlasLootDB = {
	["namespaces"] = {
		["DefaultFrame"] = {
		},
		["AtlasLootPanel"] = {
		},
		["WishList"] = {
		},
		["Filter"] = {
		},
	},
	["showWarning"] = true,
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["BonusRollEnabled"] = false,
			["ItemIDs"] = true,
			["CraftingLink"] = 2,
		},
	},
}

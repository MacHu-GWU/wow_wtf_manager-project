
AtlasLootOptions = nil
AtlasLootDB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["CraftingLink"] = 2,
			["ItemIDs"] = 1,
			["AllLinks"] = false,
			["AtlasLootVersion"] = "51103",
		},
	},
}
AtlasLootWishList = {
	["Options"] = {
	},
	["Shared"] = {
	},
	["Own"] = {
	},
}

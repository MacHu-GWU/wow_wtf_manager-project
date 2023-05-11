
AtlasOptions = {
	["AtlasSortBy"] = 4,
	["AtlasDontShowInfo"] = false,
	["AtlasCtrl"] = false,
	["AtlasAlpha"] = 1,
	["AtlasCheckModule"] = true,
	["AtlasButtonRadius"] = 78,
	["AtlasAutoSelect"] = true,
	["AtlasLocked"] = false,
	["AtlasClamped"] = true,
	["AtlasColoringDropDown"] = true,
	["AtlasDontShowInfo_12201"] = false,
	["AtlasAcronyms"] = true,
	["AtlasType"] = 1,
	["AtlasButtonShown"] = true,
	["AtlasVersion"] = "1.24.00",
	["AtlasButtonPosition"] = 26,
	["AtlasBossDescScale"] = 0.8999999761581421,
	["AtlasZone"] = 1,
	["AtlasBossDesc"] = true,
	["AtlasScale"] = 0.9999999403953552,
	["AtlasRightClick"] = false,
}
AtlasDB = {
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["minimap"] = {
				["minimapPos"] = 150.422071368287,
			},
		},
	},
}

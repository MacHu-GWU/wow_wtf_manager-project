
CombuctorVersion = nil
CombuctorDB2 = {
	["version"] = "5.4.0",
	["global"] = {
	},
	["profiles"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = {
			["inventory"] = {
				["showBags"] = false,
				["h"] = 515.9998779296875,
				["exclude"] = {
					["All"] = {
						"All", -- [1]
					},
				},
				["position"] = {
					"RIGHT", -- [1]
					nil, -- [2]
					"RIGHT", -- [3]
					-3.999734401702881, -- [4]
					-80.99995422363281, -- [5]
				},
				["bags"] = {
					0, -- [1]
					1, -- [2]
					2, -- [3]
					3, -- [4]
					4, -- [5]
				},
				["sets"] = {
					"All", -- [1]
					"Equipment", -- [2]
					"Usable", -- [3]
					"Quest", -- [4]
					"Trade Goods", -- [5]
					"Miscellaneous", -- [6]
				},
				["w"] = 557.000244140625,
				["leftSideFilter"] = true,
			},
			["bank"] = {
				["h"] = 512,
				["showBags"] = false,
				["exclude"] = {
					["All"] = {
						"All", -- [1]
					},
				},
				["sets"] = {
					"All", -- [1]
					"Equipment", -- [2]
					"Trade Goods", -- [3]
					"Miscellaneous", -- [4]
				},
				["w"] = 512,
				["bags"] = {
					-1, -- [1]
					5, -- [2]
					6, -- [3]
					7, -- [4]
					8, -- [5]
					9, -- [6]
					10, -- [7]
					11, -- [8]
				},
			},
		},
		{%- endfor %}
	},
}

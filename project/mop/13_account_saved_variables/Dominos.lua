
DominosDB = {
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["frames"] = {
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = -261,
					["spacing"] = 4,
					["padH"] = 2,
					["pages"] = {
						["PALADIN"] = {
							["page2"] = 1,
							["page5"] = 4,
							["page4"] = 3,
							["page3"] = 2,
							["page6"] = 5,
						},
					},
					["numButtons"] = 12,
				}, -- [1]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["anchor"] = "1TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 40,
				}, -- [2]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["anchor"] = "2TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 80,
				}, -- [3]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = -280,
					["anchor"] = "3TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 120,
				}, -- [4]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = -280,
					["anchor"] = "4TR",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 160,
				}, -- [5]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = 245,
					["spacing"] = 4,
					["padH"] = 2,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["numButtons"] = 12,
				}, -- [6]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = 345,
					["anchor"] = "6TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 40,
				}, -- [7]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = 345,
					["anchor"] = "7TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 80,
				}, -- [8]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = 345,
					["anchor"] = "8TC",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 120,
				}, -- [9]
				{
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["padW"] = 2,
					["x"] = 345,
					["anchor"] = "9TR",
					["spacing"] = 4,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["PALADIN"] = {
						},
					},
					["y"] = 160,
				}, -- [10]
				["encounter"] = {
					["y"] = 190,
					["point"] = "BOTTOM",
					["showInOverrideUI"] = true,
					["showInPetBattleUI"] = true,
				},
				["bags"] = {
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOMRIGHT",
					["spacing"] = 2,
					["anchor"] = "menuTR",
					["showInOverrideUI"] = false,
					["numButtons"] = 5,
					["y"] = 76,
				},
				["xp"] = {
					["showInPetBattleUI"] = false,
					["point"] = "TOPLEFT",
					["showInOverrideUI"] = false,
					["width"] = 0.1,
					["y"] = -91,
					["x"] = 31,
					["height"] = 14,
					["alwaysShowText"] = true,
					["texture"] = "blizzard",
				},
				["cast"] = {
					["showInPetBattleUI"] = false,
					["showInOverrideUI"] = false,
					["width"] = 28,
					["y"] = -240,
					["showText"] = true,
					["height"] = 8,
					["padding"] = 0,
					["SetBlizzBorder"] = 1,
				},
				["menu"] = {
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOMRIGHT",
					["columns"] = 7,
					["clickThrough"] = false,
					["showInOverrideUI"] = false,
					["spacing"] = 0,
				},
				["extra"] = {
					["y"] = 231,
					["x"] = -364,
					["point"] = "BOTTOM",
					["anchor"] = "vehicleTL",
					["showInOverrideUI"] = false,
					["showInPetBattleUI"] = false,
				},
				["class"] = {
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.9,
					["showInOverrideUI"] = false,
					["y"] = 167,
					["x"] = -386,
					["spacing"] = 2,
					["anchor"] = "5TL",
					["numButtons"] = 0,
				},
				["vehicle"] = {
					["y"] = 200,
					["x"] = -374,
					["point"] = "BOTTOM",
					["anchor"] = "petTL",
					["showInOverrideUI"] = false,
					["showInPetBattleUI"] = false,
				},
				["roll"] = {
					["showInPetBattleUI"] = true,
					["x"] = -408,
					["columns"] = 1,
					["spacing"] = 2,
					["scale"] = 0.75,
					["showInOverrideUI"] = true,
					["point"] = "BOTTOMRIGHT",
				},
				["pet"] = {
					["showInPetBattleUI"] = false,
					["point"] = "BOTTOM",
					["scale"] = 0.75,
					["showInOverrideUI"] = false,
					["y"] = 236,
					["x"] = -343,
					["spacing"] = 6,
					["anchor"] = "classTL",
				},
			},
			["minimap"] = {
				["minimapPos"] = 150.8901934156853,
			},
			["showgrid"] = 1,
		},
	},
}
DominosVersion = "5.4.12"

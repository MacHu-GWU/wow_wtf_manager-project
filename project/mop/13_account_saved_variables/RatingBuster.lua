
RatingBusterDB = {
	["namespaces"] = {
		["LibDualSpec-1.0"] = {
		},
	},
	["profileKeys"] = {
	    {%- for character in all_characters %}
		["{{ character.character }} - {{ character.server }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["sumHaste"] = true,
			["sumSpellPower"] = true,
			["sumIgnoreMail"] = false,
			["profileVersion"] = 1,
			["sumIgnoreCloth"] = false,
			["sumHit"] = true,
			["showHealingFromStr"] = true,
			["sumIgnorePlate"] = false,
			["sumAP"] = true,
			["showSpellCritFromInt"] = true,
			["sumDodge"] = true,
			["ratingPhysical"] = true,
			["showCritFromAgi"] = true,
			["sumParry"] = true,
			["showDodgeFromAgi"] = true,
			["sumMP"] = true,
			["sumSpellCrit"] = true,
			["sumBlock"] = true,
			["showSpellPwrFromInt"] = true,
			["sumSpellHaste"] = true,
			["sumMP5"] = true,
			["sumSpellHit"] = true,
			["showMP5FromSpi"] = true,
			["sumCrit"] = true,
			["showParryFromStr"] = true,
			["showSpellHitFromSpi"] = true,
			["sumExpertise"] = true,
			["sumIgnoreLeather"] = false,
			["showSpellPwrFromStr"] = true,
			["ratingSpell"] = true,
		},
	},
}

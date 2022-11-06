sdm_version = "1.8.3"
sdm_listFilters = {
	["true"] = true,
	["s"] = true,
	["b"] = true,
	["false"] = true,
	["global"] = true,
	["f"] = true,
}
sdm_iconSize = 36
sdm_mainContents = {
{%- for macro in macro_list %}
    {{ loop.index - 1 }},
{%- endfor %}
}
sdm_macros = {
{%- for macro in macro_list %}
    [{{ loop.index - 1 }}] = {
        ["type"] = "b",
		["name"] = "{{ macro.name }}",
		["ID"] = {{ loop.index - 1 }},
		["text"] = "{{ macro.encode_content() }}",
		["icon"] = 1,
    }
{%- endfor %}
}

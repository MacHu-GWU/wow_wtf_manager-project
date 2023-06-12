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
    {{ macro.id }},
{%- endfor %}
}
sdm_macros = {
{%- for macro in macro_list %}
    {{ macro.render() | indent(4) }}
{%- endfor %}
}

#Command: "consul kv export" The kv export command is used to retrieve KV pairs for the given prefix from Consul's KV store, and write a JSON representation to stdout. This can be used with the command "consul kv import" to move entire trees between Consul clusters.

# To export the tree at "redis/" in the key value store:
consul kv export redis/

""" O/P: 
[
	{
		"key": "redis/config/connection",
		"flags": 0,
		"value": ""
	}
]
"""

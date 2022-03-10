# The kv put command writes the data to the given path in the KV store.

# To insert a value of "5" for the key named "redis/config/connections" in the KV store:
consul kv put redis/config/connections 5        # O/P: Success! Data written to: redis/config/connections

#If no data is specified, the key will be created with empty data:
consul kv put redis/config/connections         # O/P: Success! Data written to: redis/config/connections


## Be careful of overwriting data! The above operation would overwrite any existing value at the key to the empty value. ##

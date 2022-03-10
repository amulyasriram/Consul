# "consul kv delete" This query is used to deleting a key
consul kv delete redis/config/connection                # Success! Deleted key: redis/config/connection

# If the key does not exist, the command will not error, and a success message will be returned:
consul kv delete not-a-real-key                         # Success! Deleted key: not-a-real-key

# -cas - Perform a Check-And-Set operation. Specifying this value also requires the -modify-index flag to be set. The default value is false.
# -modify-index=<int> - Unsigned integer representing the ModifyIndex of the key. This is used in combination with the -cas flag.
# -recurse - Recursively delete all keys with the path. The default value is false.


# To only delete a key if it has not been modified since a given index, specify the -cas and -modify-index flags:
consul kv get -detailed redis/config/connection | grep ModifyIndex      # O/P: ModifyIndex      519
consul kv delete -cas -modify-index=123 redis/config/connection         # O/P: Error! Did not delete key redis/config/connection: CAS failed
consul kv delete -cas -modify-index=456 redis/config/connection         # O/P: Success! Deleted key: redis/config/connection

# To recursively delete all keys that start with a given prefix, specify the -recurse flag:
consul kv delete -recurse redis/                    # O/P: Success! Deleted keys with prefix: redis/


# It is not valid to combine the -cas option with -recurse, since you are deleting multiple keys under a prefix in a single operation:
consul kv delete -recurse redis/                   #O/P: Cannot specify both -cas and -recurse!

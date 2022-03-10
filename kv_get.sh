# This query is used to read a value back from consul

consul kv get redis/config/connection       # O/P: 5



# this query is used to get detailed information
consul kv get -detailed redis/config/connection

""" O/P: CreateIndex      332
    Flags            0
    Key              redis/config/connection
    LockIndex        0
    ModifyIndex      332
    Session          -
    Value            5 """

# To treat the path as a prefix and list all entries which start with the given prefix, specify the -recurse flag:
consul kv get -recurse redis/ 

""" O/P: redis/config/conn:
    redis/config/connection:
    redis/test/conn: """
    
# Alternatively, combine with the -detailed flag to list detailed information about all entries under a prefix:
consul kv get -recurse -detailed redis

""" 
O/P: CreateIndex      604
Flags            0
Key              redis/config/conn
LockIndex        0
ModifyIndex      604
Session          -
Value

CreateIndex      562
Flags            0
Key              redis/config/connection
LockIndex        0
ModifyIndex      562
Session          -
Value

CreateIndex      612
Flags            0
Key              redis/test/conn
LockIndex        0
ModifyIndex      612
Session          -
Value    """

# To just list the keys which start with the specified prefix, use the -keys option instead. This is more performant and results in a smaller payload:
consul kv get -keys redis/config/

""" O/P: redis/config/conn
redis/config/connection """

# To list all keys at the root, simply omit the prefix parameter:
consul kv get -keys
""" O/P: my-key
    redis/
    sample/
    test/ """
    
# By default, the -keys operation uses a separator of "/", meaning it will not recurse beyond that separator. You can choose a different separator by setting -separator="<string>".
consul kv get -keys -separator="c" redis
""" redis/c
redis/test/c """


#Alternatively, you can disable the separator altogether by setting it to the empty string:
consul kv get -keys -separator="" redis
""" O/P: redis/config/conn
redis/config/connection
redis/test/conn """

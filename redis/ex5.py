#lpush() returns the length of the list after the push operation succeeds. Each call of .lpush() puts the IP at the beginning of the Redis list that is keyed by the string "ips".

import redis
r = redis.Redis(db=3)
print(r.lpush("ips","51.218.112.236"))      #O/P: 1
print(r.lpush("ips", "90.213.45.98"))       #O/P: 2
print(r.lpush("ips", "115.215.230.176"))    #O/P: 3

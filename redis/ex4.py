import redis
r = redis.Redis(db=2)
from datetime import timedelta
print(r.setex(
     "runner",
     timedelta(minutes=1),
     value="now you see me, now you don't"
 ))
 
 #O/P: True
 
print(r.ttl("runner"))          #O/P: 60
print(r.pttl("runner"))         #O/P: 60000
print(r.get("runner"))          #O/P: b"now you see me, now you don't"
## Set new expire window
print(r.expire("runner", timedelta(seconds=3)))     #O/P: True
# Pause for a few seconds
print(r.get("runner"))
# Key & value are both gone (expired)
print(r.exists("runner"))       #O/P: 0

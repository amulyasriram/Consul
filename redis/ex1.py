import redis
r = redis.Redis(host="localhost", port=6379,db=0)
r.set('foo','bar')
value = r.get('foo')
print(value)

#O/p: b'bar

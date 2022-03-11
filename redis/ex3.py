# url: https://realpython.com/python-redis/
import redis 
import random
random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}
r = redis.Redis(db=1)
print(r.bgsave())
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        print(pipe.hmset(h_id,hat))
    print(pipe.execute())
    
"""O/P: Pipeline<ConnectionPool<Connection<host=localhost,port=6379,db=1>>>
Pipeline<ConnectionPool<Connection<host=localhost,port=6379,db=1>>>
Pipeline<ConnectionPool<Connection<host=localhost,port=6379,db=1>>>
[True, True, True]"""
    
print(r.hgetall("hat:56854717"))    #O/P: {b'color': b'green', b'price': b'99.99', b'style': b'baseball', b'quantity': b'200', b'npurchased': b'0'}

print(r.keys())         #O/P: [b'hat:1236154736', b'hat:1326692461', b'hat:56854717']
print(r.hincrby("hat:56854717", "quantity", -1))        #O/P:199

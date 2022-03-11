import consul 
c = consul.Consul()
print(c.kv.put('foo','bar'))                #O/P: True

index, data = c.kv.get('foo')
print(data['Key'],data['Value'])            #O/P: foo, b'bar'

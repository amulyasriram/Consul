import consul
def test_kv_delete(consul_port):
    c = consul.Consul(port=consul_port)
    c.kv.put('foo1', '1')
    c.kv.put('foo2', '2')
    c.kv.put('foo3', '3')
    index, data = c.kv.get('foo', recurse=True)
    assert [x['Key'] for x in data] == ['foo1', 'foo2', 'foo3']
    assert c.kv.delete('foo2') is True
    index, data = c.kv.get('foo', recurse=True)
    assert [x['Key'] for x in data] == ['foo1', 'foo3']
    assert c.kv.delete('foo', recurse=True) is True
    index, data = c.kv.get('foo', recurse=True)
    assert data is None
    
test_kv_delete("8301")

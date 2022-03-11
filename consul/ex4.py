import consul
import pytest
def test_kv_acquire_release(consul_port):
        c = consul.Consul(port=consul_port)

        pytest.raises(
            consul.ConsulException, c.kv.put, 'foo', 'bar', acquire='foo')

        s1 = c.session.create()
        s2 = c.session.create()

        print( c.kv.put('foo', '1', acquire=s1) is True)
        assert c.kv.put('foo', '2', acquire=s2) is False
        assert c.kv.put('foo', '1', acquire=s1) is True
        assert c.kv.put('foo', '1', release='foo') is False
        assert c.kv.put('foo', '2', release=s2) is False
        assert c.kv.put('foo', '2', release=s1) is True

        c.session.destroy(s1)
        c.session.destroy(s2) 
        
test_kv_acquire_release("8301")   

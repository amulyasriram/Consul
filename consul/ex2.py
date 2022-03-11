import consul
# master_token is a *management* token, for example the *acl_master_token*
# you started the Consul server with
master = consul.Consul(token=master_token)
master.kv.put('foo','bar')
master.kv.put('private/foo','bar')
rules = """
    key "" {
        policy = "read"
    }
    key "private/" {
        policy = "deny"
    }
 """

token = master.acl.create(rules=rules)
client = consul.Consul(token = token)
print(client.kv.get('foo'))
print(client.kv.put('foo','bar2'))
print(client.kv.get('private/foo'))
print(client.kv.put('private/foo', 'bar2'))

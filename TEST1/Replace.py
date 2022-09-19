host={'ip':{'dev':'192.168.0.1',
            'test':'192.168.0.2'},
      'default':'test'}
ip=host['ip'][host['default']]
url='/add'
print(ip+url)
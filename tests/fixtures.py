diff1 = {
              'timeout': ('changed', (50, 20)),
              'host': ('unchanged', 'hexlet.io'),
              'proxy': ('deleted', '123.234.53.22'),
              'verbose': ('added', True),
              'follow': ('deleted', False)
        }
diff2 = {
              'common': ('nested', {
                  'setting3': ('changed', (True, {'key': 'value'})),
                  'setting6': ('nested', {
                      'doge': ('nested', {
                          'wow': ('changed', ('too much', 'so much'))
                      }),
                      'key': ('unchanged', 'value'),
                      'ops': ('added', 'vops')
                  }),
                  'setting1': ('unchanged', 'Value 1'),
                  'setting2': ('deleted', 200),
                  'setting5': ('added', {'key5': 'value5'}),
                  'setting4': ('added', 'blah blah'),
                  'follow': ('added', False)
              }),
              'group1': ('nested', {
                  'baz': ('changed', ('bas', 'bars')),
                  'nest': ('changed', ({'key': 'value'}, 'str')),
                  'foo': ('unchanged', 'bar')
              }),
              'group2': ('deleted', {'abc': 12345, 'deep': {'id': 45}}),
              'group3': ('added', {
                              'fee': 100500,
                              'deep': {'id': {'number': 45}}
                         })
        }

t = open('template.html').read(); d = open('data.json').read()
open('index.html', 'w').write(t.replace('__DATA__', d))
print('index.html written')

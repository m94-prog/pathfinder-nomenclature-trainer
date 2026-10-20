# Builds index.html (GitHub Pages, uses img/) from template.html + data.json
t = open('template.html').read(); d = open('data.json').read()
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
page = t.replace('__DATA__', d).replace('<style>', '<style>[hidden]{display:none!important}', 1)
open('index.html', 'w').write(head + page + '\n</html>\n')
print('index.html written')

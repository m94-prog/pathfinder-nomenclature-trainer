# Builds index.html (GitHub Pages, uses img/) from template.html + data.json
t = open('template.html').read(); d = open('data.json').read()
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
page = t.replace('__DATA__', d).replace('<style>', '<style>[hidden]{display:none!important}', 1)
open('index.html', 'w').write(head + page + '\n</html>\n')
print('index.html written')

# Single-file offline build with photos embedded
import json, base64, io
from PIL import Image
dd = json.load(open('data.json'))
for f in dd['figures']:
    im = Image.open(f['img']).convert('RGB')
    if im.width > 1200: im = im.resize((1200, int(im.height * 1200 / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=72, optimize=True)
    f['img'] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
page2 = t.replace('__DATA__', json.dumps(dd, ensure_ascii=False, separators=(',', ':'))).replace('<style>', '<style>[hidden]{display:none!important}', 1)
open('Pathfinder_Nomenclature_Trainer.html', 'w').write(head + page2 + '\n</html>\n')
print('Pathfinder_Nomenclature_Trainer.html written')

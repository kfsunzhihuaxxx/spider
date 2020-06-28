import execjs

with open('translate.js','r') as f:
    js_code = f.read()

loader = execjs.compile(js_code)
print(loader.call('e','hello'))
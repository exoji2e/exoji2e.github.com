import json
with open('links.json') as links:
    J = json.loads(links.read())

f = open('../../_data/archive/skoldebatten.yml', 'w')
def pp(s):
    f.write('{}\n'.format(s))
def getSite(url):
    if '.se/' in url:
        k = url.split('.se/')[0]
    elif '.com/' in url:
        k = url.split('.com/')[0]
    else:
        return None
    return k.split('.')[-1].split('/')[-1]

for k, v in sorted(J.items(), reverse=True, key=lambda x: x[1]['datetime']):
    pp(f'- title: "{v["title"]}"')
    pp(f'  date: "{v["datetime"]}"')
    pp(f'  url: "{k}"')
    source = getSite(k)
    if source:
        pp(f'  source: "{source}"')
f.close()
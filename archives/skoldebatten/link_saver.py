import json
LINK_FILE = 'links.json'
import argparse
def getLinks():
    try:
        with open(LINK_FILE) as f:
            return json.loads(f.read())
    except:
        return {}

def saveLinks(links):
    text = json.dumps(links, sort_keys=True, indent=2)
    with open(LINK_FILE, 'w') as f:
        f.write(text)

links = getLinks()

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-d', '--datetime', required=True)
    parser.add_argument('-t', '--title', required=True)
    parser.add_argument('-f', '--force', action='store_true')
    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()
    u, d = args.url, args.datetime
    if u in links and not args.force:
        print('Already stored (use -f to override) {}'.format(u))
        exit()
    links[u] = {'datetime' : d, 'title': args.title}
    saveLinks(links)




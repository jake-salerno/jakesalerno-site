#!/usr/bin/env python3
"""Check generated static routes, metadata, structured data and retained assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];BASE='https://www.jakesalerno.ai';pages=json.loads((ROOT/'content/pages.json').read_text());data=json.loads((ROOT/'content/site.json').read_text())
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.ids=set();self.jsons=[];self.script=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs);self.tags.append((t,a));self.ids.update([a['id']] if 'id' in a else []);self.script=t=='script' and a.get('type')=='application/ld+json'
 def handle_endtag(self,t):
  if t=='script':self.script=False
 def handle_data(self,s):
  if self.script:self.jsons.append(json.loads(s))
parsed={}
for path in pages:
 file=ROOT/(path.strip('/')+'/index.html' if path!='/' else 'index.html');p=Parser();p.feed(file.read_text());parsed[path]=p
 assert sum(t=='h1' for t,a in p.tags)==1,path
 assert any(t=='link' and a.get('rel')=='canonical' and a['href']==BASE+path for t,a in p.tags),path
 assert any(t=='meta' and a.get('name')=='robots' and 'max-image-preview:large' in a.get('content','') for t,a in p.tags),path
 assert p.jsons,path
 for t,a in p.tags:
  if t=='img' and a.get('src'):
   assert a.get('alt') and a.get('width') and a.get('height') and a.get('srcset') and a.get('sizes'),(path,a)
 for graph in p.jsons:
  ids=[x['@id'] for x in graph['@graph'] if '@id' in x];assert len(ids)==len(set(ids)),path
for path,p in parsed.items():
 for t,a in p.tags:
  for attr in (['href'] if t in ['a','link'] else ['src'] if t in ['img','script'] else []):
   url=a.get(attr,'');u=urlsplit(url)
   if u.scheme and u.netloc!='www.jakesalerno.ai':continue
   if u.scheme in ['mailto','tel']:continue
   target=u.path or path
   if not target.startswith('/'):continue
   if target in pages:
    if u.fragment:assert unquote(u.fragment) in parsed[target].ids,(path,url)
   else:assert (ROOT/unquote(target.lstrip('/'))).is_file(),(path,url)
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','i':'http://www.google.com/schemas/sitemap-image/1.1'};tree=ET.parse(ROOT/'sitemap.xml');locs={x.text for x in tree.findall('.//s:url/s:loc',ns)};assert locs=={BASE+p for p in pages}
imageLocs={x.text for x in tree.findall('.//i:loc',ns)}
for group,folder in [('eventPhotos','event-photos'),('speakerCards','speaker-cards')]:
 for i in data[group]:assert BASE+'/images/'+folder+'/'+i['image'] in imageLocs,i['image']
assert len(data['eventPhotos'])==38 and len(data['speakerCards'])==35
ranks=sorted([i for i in data['eventPhotos'] if i.get('editorialRank')],key=lambda i:i['editorialRank']);assert len(ranks)==6
assert 't=22280' in (ROOT/'media/index.html').read_text()
assert 'previous-sessions/jake-salerno' not in (ROOT/'index.html').read_text()
print('PASS:',len(pages),'pages; all internal routes/fragments, dimensions, metadata, JSON-LD, sitemap, 38 photos and 35 cards.')

agent=ROOT/'appearances/agentic-finance-2026/index.html'
assert agent.is_file()
for path in ['index.html','media/index.html','event-features/index.html',str(agent.relative_to(ROOT))]:
 assert 'Watch discussion' in (ROOT/path).read_text(),path
assert sum('finance.yahoo.com/news/0g-labs' in i.get('url','') for i in data['mediaResources'])==1
assert [i['event'] for i in sorted([x for x in data['speakingAppearances'] if x.get('editorialRank')],key=lambda x:x['editorialRank'])]==['TOKEN2049 Singapore','EthCC[9] Cannes','ETHDenver — The Scaling Summit']

# Editorial photo rank is independent of chronology and archive metadata.
assert [i['image'] for i in ranks]==['ethdenver-end-of-blind-faith-talk.webp','dev-day-2026-speaking.webp','onepiece-labs-talk.webp','ai-frontier-speaking-closeup.webp','bass-denver-fireside.webp','kbw-2026-speaking.webp']
home=(ROOT/'index.html').read_text()
assert home.count('class="talk-visual')==3
assert 'AI infrastructure × go-to-market' in home
assert 'DM+Serif' not in home
css=(ROOT/'assets/site.css').read_text()
assert '@media(prefers-reduced-motion:reduce)' in css and 'scroll-behavior:auto' in css
assert 'opacity:0' not in css and '.gallery-extra' not in css

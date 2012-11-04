#!/usr/bin/env python

from mrjob.job import MRJob
from businesses import businesses
import feedparser
from regex import compile, escape
from sys import stderr


def wordReS(w):
    return '\\b'+ escape(w)+ '\\b'

feedparser._HTMLSanitizer.acceptable_elements = set()

bnReS = ''
for bId, bNames in businesses.iteritems():
    s = u"|".join([wordReS(n) for n in bNames if len(n) >= 2])
    if s != '':
        bnReS = bnReS + ('|' if bnReS != '' else '') + '('+ s+ ')'

bnRe = compile(bnReS)

def matchedIds(mList):
    out = set()
    for m in mList:
        for (gm, bId) in zip(m.groups(), businesses.keys()):
            if gm != None:
                out.add(bId)
    return out

class MRCompaniesInTheNews(MRJob):
    def fetch_sources(self, key, url):
        d = feedparser.parse(url)
        for e in d.entries:
            if hasattr(e, 'link') and hasattr(e, 'title') and hasattr(e, 'description'):
                txt = e.description.replace('&nbsp;', ' ')
                yield e.link, (e.title, txt)

    def tag_doc(self, url, (title, txt) ):
        mTitle = bnRe.finditer(title)
        mTxt = bnRe.finditer(txt)
        if mTitle or mTxt:
            yield url, list(matchedIds(mTitle).union(matchedIds(mTxt)))
        else:
            yield url, []

    def steps(self):
        return [self.mr(self.fetch_sources), self.mr(self.tag_doc)]

if __name__ == '__main__':
    MRCompaniesInTheNews.run()


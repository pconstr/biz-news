#!/usr/bin/env python2.7

from freebase import mqlread
from pickle import Pickler

res = mqlread([{"type": "/business/business_operation", "name": None, "/common/topic/alias": [], "id": None, "revenue" : [{"amount":None, "currency": None}], "limit": 5000}])
print 'got', len(res), 'businesses'

d = {}
for r in res:
    d[r['id']] = [r['name']] + r['/common/topic/alias']

#p = Pickler(open('businesses_names.pickle', 'w'))
#p.dump(d)

f = open('businesses.py', 'w')
f.write('businesses = '+ str(d))





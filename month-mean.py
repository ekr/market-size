#!/usr/bin/env python
import re
import sys

tot = 0
ct = 0
mon = None

mau = open(sys.argv[1])
for l in mau:
    if l.startswith("date"):
        print l,
        continue
    ll = l.split(",")
    m = re.match("\d\d\d\d-\d\d\-(\d\d)", ll[0])
    if m is None:
        print("Error: "+l)
        sys.exit(1)
    if m.group(1) == "01":
        if mon is not None:
            print "%s,%d"%(mon, tot/ct)
        tot = 0
        ct = 0
        mon = ll[0]
    ct += 1
    tot += int(ll[1])
            


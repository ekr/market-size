#!/usr/bin/env python
import re
import sys

mau = open("browser-US-monthly-200901-201910.csv")
for l in mau:
    if l.startswith('"Date"'):
        print l,
        continue
    m = re.match("(\d\d\d\d-\d\d)(.*)", l)
    if m is None:
        print("Error: "+l)
        sys.exit(1)
    print m.group(1) + "-01" + m.group(2)

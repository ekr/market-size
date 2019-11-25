#!/usr/bin/env python
import re
import sys

mau = open("Desktop_MAU_in_US_and_ROW_2019_11_22.csv")
for l in mau:
    if l.startswith("date"):
        print l,
        continue
    m = re.match("\d\d\d\d-\d\d\-(\d\d)", l)
    if m is None:
        print("Error: "+l)
        sys.exit(1)
    if m.group(1) == "01":
        print l,


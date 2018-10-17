#!/usr/bin/env python

import os, sys, hashlib
from collections import defaultdict

if __name__ == '__main__':
    dirs = [os.getcwd()] if len(sys.argv) == 1 else sys.argv[1:]
    dirs = [os.path.abspath(d) for d in dirs]
    if not all(map(os.path.exists, dirs)):
        print('Error: invalid path(s)')
        sys.exit()

    sizetable = defaultdict(list)
    for d in dirs:
        for r, _, fs in os.walk(d):
             for f in fs:
                f = os.path.join(r, f)
                s = os.path.getsize(f)
                sizetable[s].append(f)

    hashtable = defaultdict(list)
    for fs in sizetable.values():
        if len(fs) < 2: continue
        for f in fs:
            with open(f, 'rb') as fp:
                h = hashlib.md5(fp.read()).hexdigest()
                hashtable[h].append(f)

    for fs in hashtable.values():
        if len(fs) < 2: continue
        print('# Dups:')
        for f in fs: print(f)

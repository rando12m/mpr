#!/usr/bin/env python
import sys
from itertools import groupby
from functools import reduce

if __name__ == "__main__":
  data = {key: reduce(lambda x, y: x + 1, group, 0) for key, group in groupby(sorted(sys.stdin.read().split()))}

  for key, count in sorted(data.items()):
    print "%s\t%d" % (key, count)

#Example:
#time cat books/* | ./sequential.py

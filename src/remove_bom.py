#!/usr/bin/python
# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/YANG-to-Redfish-Converter/LICENSE.md

import codecs
import shutil
import sys

s = sys.stdin.read(3)
if s != codecs.BOM_UTF8:
    sys.stdout.write(s)

shutil.copyfileobj(sys.stdin, sys.stdout)

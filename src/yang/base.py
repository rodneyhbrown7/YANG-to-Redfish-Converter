# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/YANG-to-Redfish-Converter/LICENSE.md

from modgrammar import *
from yang.comment import *
grammar_whitespace_mode = 'optional'


class Base(Grammar):
    grammar = (L('base'), OPTIONAL(SingleLineComment),
               WORD('"a-zA-Z0-9', restchars='a-zA-Z0-9:\.\-"',
                    fullmatch=True, escapes=True), OPTIONAL(SingleLineComment)
               )

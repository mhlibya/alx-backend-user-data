#!/usr/bin/env python3
import re
"""
   filter_detum
"""
def filter_datum(fields, redaction, message, separator):
    """
       filter_detum
    """
    return re.sub(rf'({"|".join(fields)})=[^ {separator}]+', lambda m: f'{m.group(1)}={redaction}', message)

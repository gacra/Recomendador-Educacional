import re

RE_TERMS = re.compile('[\d\-_]*[^\W\d_][\w-]*')
MAX_TERMS = 50000

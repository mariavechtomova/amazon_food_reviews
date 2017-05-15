import re
import numpy as np

def cleanData(strg):
    line = re.sub("[^a-zA-Z]",' ',strg)
    line = re.sub('  ',' ',line)
    result=str.lower(line)
    return result

def getSentenceLength(strg):
    return len(strg.split())

def add_placeholders(strg, limit):
    line = strg.split()
    length = len(line)
    if length<limit:
        line = line + ['nowordplaceholder']*(limit-length)
    result = ' '.join(line)
    return result

def create_sentence_vectors(strg, dic):
    line = strg.split()
    result = np.array([*map(lambda x: dic[x], line)])
    return result

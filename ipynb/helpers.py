import re
import numpy as np

def cleanData(strg,stopwords):
    line = re.sub("[^a-zA-Z]",' ',strg)
    line = re.sub('  ',' ',line)
    #line=line.encode('utf-8')
    line=str.lower(line)
    querywords = line.split()
    resultwords  = [word for word in querywords if word not in stopwords]
    result = ' '.join(resultwords)
    return result

def getSentenceLength(strg):
    return len(strg.split())

def add_placeholders(strg):
    line = strg.split()
    length = len(line)
    if length<200:
        line = line + ['nowordplaceholder']*(200-length)
    result = ' '.join(line)
    return result

def create_sentence_vectors(strg, dic):
    line = strg.split()
    result = np.array([*map(lambda x: dic[x], line)])
    return result



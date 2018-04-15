# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    wordlist = [words(get_text(files[i])) for i in range(len(files))]
    table = htable(4011)


    for i in range(len(files)):
        for j in range(len(wordlist[i])):
            htable_put(table, wordlist[i][j], set())


    for i in range(len(files)):

        for j in range(len(wordlist[i])):

            htable_get(table, wordlist[i][j]).add(i)
    return table

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """

    termlist = set()

    for i in range(len(terms)):
        for j in range(len(terms[i].split(" "))):
            termlist.add(terms[i].split(" ")[j])

    indexlist = [htable_get(index, w) for w in termlist]
    indexlist = filter(None, indexlist)

    if indexlist !=[]:
        intersect = list(set.intersection(*indexlist))
        return [files[x] for x in intersect]
    else:
        return None

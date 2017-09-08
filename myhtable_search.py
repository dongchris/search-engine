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
    # print htable_get(table, wordlist[0][0]).add(1)
    return table

    # wlen = len(wordlist[0])
    # #print wlen
    # hset = [set() for i in range(wlen)]
    # #print hset
    # print hset
    #
    # print len(wordlist[0])
    # wordset = set()
    # for word in wordlist[0]:
    #     wordset.add(word)
    # print wordset



    #print len(hset)
    # hset[0].add(('test',0))
    # print hset[0]
    #
    # for i in range(len(files)):
    #
    #
    #     for j in range(wlen):
    #         hset[j].add(i)
    #         #htable_put(table, wordlist[0][j], hset[j])
    # #print hset
    # return table

files = ["/home/chris/data/berlitz1/HistoryHawaii.txt","/home/chris/data/berlitz1/HandRHongKong.txt",
             "/home/chris/data/berlitz1/HandRIbiza.txt"]
index = myhtable_create_index(files)
    #
    # #table = htable(4011)
    # table = htable(4011)
    # hashlist = [hashcode(w) % len(table) for w in wordlist[i]]
    # #for j in range(len(hashlist)):
    #     # htable_put(table, hashlist[j], 0)
    #     #print hashlist[j]
    # for i in range(1000):
    #
    #     htable_put(table, hashlist[i], 0)
    # # htable_put(table, hashlist[1], 0)
    # # htable_put(table, hashlist[2], 0)
    # # #print len(hashlist)
    # print table
    # #print table

    #htable_put(table, hashlist[0], 0)

    #print table[0]
    # for i in range(len(files)):
    #     hashlist = [hashcode(w) % len(table) for w in wordlist[i]]
    #     for j in range(len(hashlist)):
    #         htable_put(table, hashcode(hashlist[j]), i )
    # return table
    # print table
    # #combinelist = defaultdict(set)


    # for i in range(len(files)):
    #     d = dict.fromkeys(wordlist[i], i)
    #     for key, value in d.items():
    #         combinelist[key].add(value)

    # return combinelist
# index = myhtable_create_index(["/home/chris/data/berlitz1/HandRHawaii.txt",
#                        "/home/chris/data/berlitz1/HandRHongKong.txt",
#                        "/home/chris/data/berlitz1/HandRIbiza.txt"])
# print htable_get(index, 'poster')
# print index
# table = htable(3)
# htable_put(table, 1, 0)
# htable_put(table, 11, 1)
# htable_put(table, 21, 2)
# htable_put(table, 31, 3)
# print 'fdsf'
# print table
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

# files = ["/home/chris/data/berlitz1/HistoryHawaii.txt",
#          "/home/chris/data/berlitz1/HandRHongKong.txt",
#          "/home/chris/data/berlitz1/HandRIbiza.txt"]
# index = myhtable_create_index(files)
# # #
# doc = myhtable_index_search(files, index, ["missspellinnng"])
# print filenames(doc)







#print htable_get(index, terms[0])

    #print [w for w in terms]
    # indexlist = [htable_get(index, w) for w in terms]
    #
    # intersect = list(set.intersection(*indexlist))
    #
    # return [files[x] for x in intersect]
    #


#     termlist = set()
#
#     for i in range(len(terms)):
#         for j in range(len(terms[i].split(" "))):
#             termlist.add(terms[i].split(" ")[j])
#     print 'testin'
#     print htable_get(index, 'hawaii')
#     indexlist = [htable_get(index, w) for w in termlist]
#     print 'index lst'
#     print indexlist
#     print indexlist[0]
#     #indexlist =
#     print 'dsf'
#     intersect = list(set.intersection(*indexlist))
#
#     print intersect
#
#     return [files[x] for x in intersect]
#
#
#
# files = ["/home/chris/data/berlitz1/HistoryHawaii.txt",
#                        "/home/chris/data/berlitz1/HandRHongKong.txt",
#                         "/home/chris/data/berlitz1/HandRIbiza.txt"]
# index = myhtable_create_index(files)
# # #
#myhtable_index_search(files, index, ["hawaii travel"])
# #print htable_get(index, 'hawaii')

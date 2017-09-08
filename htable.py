
"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for i in range(nbuckets)]

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if(type(o)==int): return o
    elif type(o)==str:
        ord_sum = 0
        for c in o:
            ord_sum = ord_sum*31 + ord(c)
        return ord_sum

def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """





def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append value
    to that bucket. If the bucket for key already has a (key,value) pair
    with that key then replace it.  Make sure that you are only adding
    (key,value) associations to the buckets.
    """
    bucket_index = hashcode(key) % len(table)

    # # check if empty
    # if table[bucket_index]:
    #     print 'hi'
    #     table[bucket_index] = (key, value)
    #else:

    bucket = table[bucket_index]
    exist = False
    # check if key exists in bucket, if yes, then replace
    for i in range(len(table[bucket_index])):

        if bucket[i][0]==key:
            bucket[i] = (key, value)
            exist = True

    # if key does not exist, then append the bucket
    if exist == False:
        bucket.append((key, value))


table = htable(5)
key = 'f'
value = 99
# print "hashcode =", hashcode(key)
# bucket_index = hashcode(key) % len(table)
# print "bucket_index =", bucket_index
# bucket = table[bucket_index]
# bucket.append( (key,value) )
# # print 'fjdisf'
# # print bucket
# print table
# key = 'gddffff'
# value = 100
# bucket = table[bucket_index]
# htable_put(table, key, value)
# print table
# print hashcode('f') % len(table)
# htable_put(table, "ronald",{2,3})
# print table
# htable_put(table, "roadfsnaldd",{2,3})
# print table
# htable_put(table, "roadfsndaldd",{2,5})
# print table
# htable_put(table, "ddrdsfsdfodadfsndaldd",{2,5})
# print table
# print 'test'
# htable_put(table, "ddrdsfsdfodadfsndaldd",{2,6})
# print table
# htable_put(table, "ddrdsfsdfodadfsndaldd",{3,7})
# print table
# print bucket_indexof(table, "ronald")
# print bucket_indexof(table, 'f')
# htable_put(table, "parrt", [99])
# print table
# htable_put(table, "ronald", {9,3})
#
# print table
# print hashcode("ronald2") % len(table)
# htable_put(table, "ronald2", {9,3})
# print table
# print hashcode("ronald3") % len(table)
# htable_put(table, "ronald3", {1,3})
# print table
#
# htable_put(table, "ronald4", {9,3})
# print table
#print 'hi'
#print bucket_indexof(table, "ronald")

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket_index = hashcode(key) % len(table)

    #print bucket_index
    for i in range(len(table[bucket_index])):

        if table[bucket_index]==[] or table[bucket_index][i]==None: # empty
            return None
        else:
            if table[bucket_index][i][0]==key:
                return table[bucket_index][i][1]

            #print 'hdfs'




# print 'testssfd'
# print table
# print htable_put(table, key, value)
# print 'sfdsdfs'
# print #print hashcode('fdddsddddsfa') & leprn(table)
# print htable_get(table, 'f')


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    #print 'h'
    #print ",".join([str(x[1]) for x in table[4]])





    s = ""

    for i in range(len(table)):
        s = s + str(i).rjust(4,'0') + \
            '->' + ", ".join([str(x[0]) +
            ':' + str(x[1]) for x in table[i]]) + '\n'
        #if s < len(table):
        #   s = s + '\n'
        #s = s + '0'*3 + str(i) + '->\n'
    # add last row

    return s
# print "*"*10
#
# htable_put(table, 'fred',[3.14])
# print htable_buckets_str(table)
def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    # print table
    begin = htable_buckets_str(table).split("\n")
    begin = filter(None, begin)
    print begin
    # print begin
    # print 'hi'
    # print table[0]
    begin = ", ".join([begin[i][6:] for i in range(len(begin)) if table[i] != []])
    return '{' + begin + '}'

#
# dict = {'a':'hi', 'b':'bye'}
#
# # print str(dict)
# # print 'fdsfd'
# # print htable_str(table)
#
# table = htable(5)
# #print len(table)
# print htable_buckets_str(table)
# print htable_str(table)
#
# table = htable(5)
# htable_put(table, "parrt", 99)
# print htable_buckets_str(table)
# print htable_str(table)
#
# table = htable(5)
# htable_put(table, "parrt", set([99]))
# print htable_buckets_str(table)
# print htable_str(table)
#
# table = htable(5)
# for i in range(1, 11):
#     htable_put(table, i, i)
# print htable_buckets_str(table)
# print htable_str(table)
#
# table = htable(5)
# htable_put(table, "a", "x")
# htable_put(table, "b", "y")
# htable_put(table, "c", "z")
# htable_put(table, "f", "i")
# htable_put(table, "g", "j")
# htable_put(table, "k", "k")
# print htable_buckets_str(table)
# print htable_str(table)
#
#
# table = htable(5)
# htable_put(table, "parrt", [2, 99, 3942])
# htable_put(table, "tombu", [6, 3, 1024, 99, 102342])
# print htable_buckets_str(table)
# print htable_str(table)
#
# print [c for c in htable_buckets_str(table)]
# print [c for c in """0000->
# 0001->tombu:[6, 3, 1024, 99, 102342]
# 0002->
# 0003->parrt:[2, 99, 3942]
# 0004->
# """]
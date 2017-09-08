
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

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket_index = hashcode(key) % len(table)

    for i in range(len(table[bucket_index])):

        if table[bucket_index]==[] or table[bucket_index][i]==None: # empty
            return None
        else:
            if table[bucket_index][i][0]==key:
                return table[bucket_index][i][1]

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

    s = ""

    for i in range(len(table)):
        s = s + str(i).rjust(4,'0') + \
            '->' + ", ".join([str(x[0]) +
            ':' + str(x[1]) for x in table[i]]) + '\n'
    return s

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    begin = htable_buckets_str(table).split("\n")
    begin = filter(None, begin)
    begin = ", ".join([begin[i][6:] for i in range(len(begin)) if table[i] != []])
    return '{' + begin + '}'

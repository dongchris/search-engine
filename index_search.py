from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """

    wordlist = [words(get_text(files[i])) for i in range(len(files))]

    combinelist = defaultdict(set)

    for i in range(len(files)):
        d = dict.fromkeys(wordlist[i], i)
        for key, value in d.items():
            combinelist[key].add(value)

    return combinelist

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    doc IDs whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """


    termlist = set()

    for i in range(len(terms)):
            for j in range(len(terms[i].split(" "))):

                termlist.add(terms[i].split(" ")[j])

    indexlist = [index[w] for w in termlist]

    intersect = list(set.intersection(*indexlist))

    return [files[x] for x in intersect]

# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words, filelist


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    storefname = list()

    for file in files:
        wordlist = words(get_text(file))

        count = 0
        for term in terms:
            if term in wordlist:
                count = count + 1

        # if contain all search terms
        if count == len(terms):
            storefname.append(file)


    return storefname


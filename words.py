import os
import re
import string
import glob



def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""

    allfiles = list()
    if bool(re.search("(.)txt",os.listdir(root)[0], ))==False:
        for x in glob.glob(root + "/*"):
            allfiles.append(glob.glob(x + "/*"))
        allfiles = sum(allfiles, [])
    else:
        allfiles = [root + "/" +  x for x in os.listdir(root)]
    return allfiles

def get_text(fileName):
    f = open(fileName)
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words

def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """

    header = "<html>\n<body>\n<h2>Search results for <b>" + " ".join(terms) + "</b> in "
    numfiles = str(len(docs)) + " files</h2>\n\n"

    doclist = list()


    for i in range(len(docs)):
        # if i>100:
        #     break
        webpath = '<p><a href="file://'
        webpathname = docs[i] + '">' + docs[i]+ "</a><br>\n"
        webtext = get_text(docs[i])
        webtext = webtext.strip().replace("  ","")



        index = webtext.lower().find(terms[0].lower())
        endindex = webtext.find("\n", index)
        startindex = webtext.rfind("\n", 0, endindex)
        searchtext = webtext[startindex:endindex].lstrip()

        index2 = webtext.lower().rfind(terms[0].lower())

        #find second occurence
        if index != index2:
            searchtext = webtext[startindex:endindex].lstrip() + "<br>"
            endindex2 = webtext.find("\n", index2)
            startindex2 = webtext.rfind("\n", 0, endindex2)
            searchtext2 = webtext[startindex2:endindex2].lstrip()
            searchtext = searchtext + searchtext2

        combine = webpath + webpathname + searchtext + "<br><br>"
        doclist.append(combine)

    return header + numfiles + "\n\n".join(doclist) + "\n\n</body>\n</html>"
    #return doclist




 #   print header + numfiles + webpath + webpathname + webtext[1]
#s = results(["/home/chris/data/slate/1/Article247_42.txt",
 #       "/home/chris/data/slate/10/Article247_3363.txt",
  #      "/home/chris/data/slate/11/Article247_3408.txt"], ["reagan"])
#print s

def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

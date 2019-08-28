# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    final_list = []
    set_terms = set(terms)
    for article in files:
    	data = get_text(articles)
    	new_data = set(words(data))
    	if set_terms.issubset(new_data):
    		final_list.append(articles)
    return final_list

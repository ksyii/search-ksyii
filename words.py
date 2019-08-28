import os
import re
import string
from jinja2 import Template


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    my_list = []
    for root, direct, files in os.walk("root"):
        for names in files:
            my_list.append(os.path.join(root,names))
    return my_list
        

def get_text(fileName):
    f = open(fileName, encoding='latin-1')
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
    full_qualifed = filelist(???)
    qual_name = filenames(full_qualifed)
    if len(qual_name) > 99:
    	header = qual_name[:99]
    else:
    	header = qual_name [:(max(qual_name))]

    data??

	# complete jinja2 template
	complete_data = """
	<html>
	<body>
	<table>
	<tr>{% for item in header %}<th>{{item}}</th>{% endfor %}</tr>
	{% for item in data %}<tr>{% for parts in item %}<td>{{parts}}</td>\
	{% endfor %}</tr>\n{% endfor %}\
	</table>
	</body>
	</html>
	"""

	# call the Template class and render the template
	template = Template(complete_data)
	template = template.render(header=header, data=data)



def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

import collections

DOCUMENT_DOES_NOT_EXIST = 'The specified document does not exist'
TERM_DOES_NOT_EXIST = 'The specified term does not exist'

def stem(term):
    """ Perform various stemming methods to clean the input token """

    # Reduces plural words down to their root
    if term.endswith('ly'):
        term = term[:-2]

    return term


def toLower(term):
    """ Converts tokens to lowercase"""
    return term.lower()


class InvertedIndex:
    """
    InvertedIndex structure in the form of a hash table implementation.
    """

    def __init__(self):
        """
        Construct a new HashedIndex.
        """
        self._documents = collections.Counter()
        self._terms = {}

    def clear(self):
        """ Resets the HashedIndex to a clean state without any terms or documents. """

        self._terms = {}
        self._documents = collections.Counter()

    def add_term_occurrence(self, term, document):
        """ Adds an occurrence of the term in the specified document. """

        term = toLower(term)

        term = stem(term)

        if document not in self._documents:
            self._documents[document] = 0

        if term not in self._terms:
            self._terms[term] = collections.Counter()

        if document not in self._terms[term]:
            self._terms[term][document] = 0

        self._documents[document] += 1
        self._terms[term][document] += 1

    def get_documents(self, term):
        """ Returns all documents containing the searched input word """

        if term not in self._terms:
            return None
        else:
            return self._terms[term]

    def terms(self):
        """ Returns the total terms stored in the in-memory db"""

        return list(self._terms)

    def documents(self):
        """ Returns the total documents stored in the in-memory db"""

        return list(self._documents)

    def items(self):
        """ Returns the inverted hash-table"""

        return self._terms

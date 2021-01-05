from ranker import Ranker
import utils
import nltk

nltk.download('lin_thesaurus')
from nltk.corpus import lin_thesaurus as thes


# DO NOT MODIFY CLASS NAME
class Searcher:
    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit. The model 
    # parameter allows you to pass in a precomputed model that is already in 
    # memory for the searcher to use such as LSI, LDA, Word2vec models. 
    # MAKE SURE YOU DON'T LOAD A MODEL INTO MEMORY HERE AS THIS IS RUN AT QUERY TIME.
    def __init__(self, parser, indexer, model=None, is_thesaurus=None):
        self.parser = parser
        self.indexer = indexer
        self.ranker = Ranker()
        self._model = model
        self.is_thesaurus = is_thesaurus

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def search(self, query, k=None):
        """ 
        Executes a query over an existing index and returns the number of 
        relevant docs and an ordered list of search results (tweet ids).
        Input:
            query - string.
            k - number of top results to return, default to everything.
        Output:
            A tuple containing the number of relevant search results, and 
            a list of tweet_ids where the first element is the most relavant 
            and the last is the least relevant result.
        """
        query_as_list = self.parser.parse_sentence(query)

        if self.is_thesaurus:
            query_as_list_with_synonym = self.thesaurus_method(query_as_list[0])
            query_as_list = [query_as_list_with_synonym, None]

        relevant_docs = self.relevant_docs_from_posting(query_as_list)
        ranked_doc_ids = Ranker.rank_relevant_docs(relevant_docs)
        if k:
            ranked_doc_ids = Ranker.retrieve_top_k(ranked_doc_ids, k)
        n_relevant = len(ranked_doc_ids)
        return n_relevant, ranked_doc_ids

    # feel free to change the signature and/or implementation of this function 
    # or drop altogether.
    def relevant_docs_from_posting(self, query_as_list):
        """
        This function loads the posting list and count the amount of relevant documents per term.
        :param query_as_list: parsed query tokens
        :return: dictionary of relevant documents mapping doc_id to document frequency.
        """
        relevant_docs = {}
        for term in query_as_list[0]:  # query[0] because of the adittinonal dict to the end of capital
            try:
                if term in self.indexer.inverted_idx.keys():
                    all_docs_for_term = self.indexer.inverted_idx[term] # { "tweetID": (tf,max_tf,uniqe,rt)}
                    if term not in relevant_docs.keys():
                        relevant_docs[term] = []
                        relevant_docs[term].extend(all_docs_for_term)  # insert tweet information & tweet score
                    else:
                        relevant_docs[term].extend(all_docs_for_term)
            except:
                # print('term {} not found in posting'.format(term))
                pass

        return relevant_docs

    def thesaurus_method(self, query_list):
        """
        This function use thesaurus synonym addition of one synonym per token in the query list.
        There is limitation to one synonym per token.
        Returns the new tokens list including the originn and the synonyms
        """
        new_query_list = []
        for token in query_list:
            for synonym_term in thes.synonyms(token, fileid="simN.lsp"):
                new_query_list.append(synonym_term)
                break
        query_list.extend(new_query_list)

        return query_list

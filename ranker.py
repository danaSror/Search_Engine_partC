# you can change whatever you want in this module, just make sure it doesn't 
# break the searcher module
import math


class Ranker:
    def __init__(self):
        pass

    @staticmethod
    def rank_relevant_docs(relevant_docs, k=None):
        """
        This function provides rank for each relevant document and sorts them by their scores.
        The current score considers solely the number of terms shared by the tweet (full_text) and query.
        :param k: number of most relevant docs to return, default to everything.
        :param relevant_docs: dictionary of documents that contains at least one term from the query.
        :return: sorted list of documents by score
        """
        # ranked_results = sorted(relevant_docs.items(), key=lambda item: item[1], reverse=True)
        # if k is not None:
        #     ranked_results = ranked_results[:k]
        # return [d[0] for d in ranked_results]
        rank_doc_dict = {}  # dict lookes like : {"term" : Wij }
        for term in relevant_docs:
            for tweet_tuple in relevant_docs[term][1]:
                fij = tweet_tuple[4]  # - The number of times term i shows in tweet j
                tweet_len = int(tweet_tuple[1])  # - The number of terms shows in the current tweet
                dfi = relevant_docs[term][0]  # - The number of tweets/docs which term i show in all the corpus
                #wij = (fij / tweet_len) * math.log10(1000000 / dfi)  # - The score for term i in doc j
                max_tf = tweet_tuple[2]
                wij = (fij / max_tf) * math.log10(1000000 / dfi)  # - The score for term i in doc j

                if tweet_tuple[5] == 1:  # if it's a retweet so increase the score
                   wij += 1.8

                if tweet_tuple[0] not in rank_doc_dict:
                    rank_doc_dict[tweet_tuple[0]] = wij
                else:
                    rank_doc_dict[tweet_tuple[0]] += wij  # sim(dij,query) = sum(wij*wiq) , in this case wiq = 1

        return sorted(rank_doc_dict, key=rank_doc_dict.__getitem__, reverse=True)

    @staticmethod
    def retrieve_top_k(sorted_relevant_doc, k=2000):
        """
        return a list of top K tweets based on their ranking from highest to lowest
        :param sorted_relevant_doc: list of all candidates docs.
        :param k: Number of top document to return
        :return: list of relevant document
        """
        return sorted_relevant_doc[:k]


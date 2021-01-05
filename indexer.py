# DO NOT MODIFY CLASS NAME
import os
import pickle


class Indexer:
    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def __init__(self, config):
        self.inverted_idx = {}  # { "term" : [ frequency , [documets array] ] }
        self.config = config
        self.entities_dict = {}
        self.global_dict = {}


    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def add_new_doc(self, document):
        """
        This function perform indexing process for a document object.
        Saved information is captures via two dictionaries ('inverted index' and 'posting')
        :param document: a document need to be indexed.
        :return: -
        """
        # ------------------------ entitys & names ---------------------------
        for entity in document.entities_set:
            if entity not in self.entities_dict.keys():
                self.entities_dict[entity] = 0
            else:
                self.entities_dict[entity] += 1
        doc_capitals = document.capital_dict
        for word in doc_capitals:
            if word not in self.global_dict:
                self.global_dict[word] = doc_capitals[word]
            else:
                if not doc_capitals[word]:
                    self.global_dict[word] = False
        # ---------------------------------------------------------------------

        document_dictionary = document.term_doc_dictionary
        # Go over each term in the doc
        for term in document_dictionary.keys():
            try:
                # Update inverted index and posting
                if term not in self.inverted_idx.keys():
                    self.inverted_idx[term] = [1, {}] # empty dict for the posting dict
                else:
                    self.inverted_idx[term][0] += 1

                fij = len(document_dictionary[term])

                if len(self.inverted_idx[term][1]) == 0:
                    self.inverted_idx[term][1] = []
                    self.inverted_idx[term][1].append( (document.tweet_id,
                                                  document.doc_length,
                                                  document.max_tf,
                                                  document.unique_terms_in_doc,
                                                  fij,
                                                  document.are_rt) )
                else:
                    self.inverted_idx[term][1].append((document.tweet_id,
                                                       document.doc_length,
                                                       document.max_tf,
                                                       document.unique_terms_in_doc,
                                                       fij,
                                                       document.are_rt))

            except:
                print('problem with the following key {}'.format(term[0]))

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def load_index(self, fn):
        """
        Loads a pre-computed index (or indices) so we can answer queries.
        Input:
            fn - file name of pickled index.
        """
        dict = {}
        with open(os.path.join('', fn) , 'rb') as pickle_file:
            while True:
                try:
                    dict = pickle.load(pickle_file)
                except:
                    return dict
        #raise NotImplementedError
        dict = {}
        # with open(os.path.join(path, name) + '.pkl', 'rb') as pickle_file:
        #     while True:
        #         try:
        #             pair = pickle.load(pickle_file)
        #             dict[pair[0]] = pair[1]
        #         except:
        #             return dict

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def save_index(self, fn):
        """
        Saves a pre-computed index (or indices) so we can save our work.
        Input:
              fn - file name of pickled index.
        """
        with open(os.path.join('', fn) + '.pkl', 'wb') as pickle_file:
            pickle.dump(self.inverted_idx, pickle_file, pickle.HIGHEST_PROTOCOL)
        #raise NotImplementedError


    # feel free to change the signature and/or implementation of this function 
    # or drop altogether.
    def _is_term_exist(self, term):
        """
        Checks if a term exist in the dictionary.
        """
        return term in self.postingDict

    # feel free to change the signature and/or implementation of this function 
    # or drop altogether.
    def get_term_posting_list(self, term):
        """
        Return the posting list from the index for a term.
        """
        return self.postingDict[term] if self._is_term_exist(term) else []

    def fix_inverted_index(self):
        for term in list(self.inverted_idx.main_dict):
            should_append = True
            # if it is a named entity and it exists in less than 2 tweets, erase this term.
            if term in self.entities_dict and self.entities_dict[term] < 2:
                should_append = False
                self.inverted_idx.remove(term)
            # update terms with capital letters
            if term in self.global_capitals and self.global_capitals[term]:
                term_info = self.inverted_idx.get_term_info(term)
                self.inverted_idx.remove(term)
                term = term.upper()
                self.inverted_idx.insert_entry(term, term_info)
                # TODO check the amount of min df
            if term in self.inverted_idx.main_dict and self.inverted_idx.get_df(term) < 15:
                should_append = False
                self.inverted_idx.remove(term)
            if should_append:
                term_idf = self.calculate_idf(term)
                tweets = self.inverted_idx.get_tweets_with_term(term)
                # for each tweet, update current term's tf-idf
                # for tweet_id in tweets:
                #     tf_idf = self.inverted_idx.get_tf_idf(term, tweet_id) * term_idf
                #     self.inverted_idx.set_tf_idf(term, tweet_id, tf_idf)
                #     self.document_dict[tweet_id][1] += math.pow(tf_idf, 2)
        return self.inverted_idx, self.document_dict
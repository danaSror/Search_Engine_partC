class Document:

    def __init__(self, tweet_id, tweet_date=None, full_text=None, url=None, retweet_text=None, retweet_url=None,
                 quote_text=None, quote_url=None, term_doc_dictionary=None, doc_length=0,
                 max_tf=0, unique_terms_in_doc=0, are_rt=0,capital_dict=None,entities_set=None):
        """
        :param tweet_id: tweet id
        :param tweet_date: tweet date
        :param full_text: full text as string from tweet
        :param url: url
        :param retweet_text: retweet text
        :param retweet_url: retweet url
        :param quote_text: quote text
        :param quote_url: quote url
        :param term_doc_dictionary: dictionary of term and documents.
        :param doc_length: doc length
        :param max_tf
        :param unique_terms_in_doc
        :param are_rt
        :param capital_letter_indexer
        :param named_entities
        """
        self.tweet_id = tweet_id
        self.tweet_date = tweet_date
        self.full_text = full_text
        self.url = url
        self.retweet_text = retweet_text
        self.retweet_url = retweet_url
        self.quote_text = quote_text
        self.quote_url = quote_url
        self.term_doc_dictionary = term_doc_dictionary
        self.doc_length = doc_length
        self.max_tf = max_tf
        self.unique_terms_in_doc = unique_terms_in_doc
        self.are_rt = are_rt
        self.capital_dict = capital_dict
        self.entities_set = entities_set

import re
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity


class SearchEngine:


    def __init__(self, documents, tokenizer = None, model = None):

        self.documents = documents
        if tokenizer == None and model == None:
            self.tokenizer, self.model = self.model()
        
        else:
            self.tokenizer = tokenizer
            self.model = model


    def model(self):

        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')

        return tokenizer, model


    def preprocess(self, text):

        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text


    def get_embeddings(self, text):

        inputs = self.tokenizer(text, return_tensors = 'pt', max_length = 512, truncation = True, padding = True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim = 1).squeeze().numpy()


    def search(self, query, top_k = 3):
        
        preprocessed_documents = [self.preprocess(doc) for doc in self.documents]
        document_embeddings = [self.get_embeddings(doc) for doc in preprocessed_documents]

        query = self.preprocess(query)
        query_embedding = self.get_embeddings(query).reshape(1, -1)

        similarities = cosine_similarity(query_embedding, document_embeddings)
        similarities = similarities.flatten()

        top_k_indices = similarities.argsort()[-top_k:][::-1]

        results = [(self.documents[idx], similarities[idx]) for idx in top_k_indices]

        return results
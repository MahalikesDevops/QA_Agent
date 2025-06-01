from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# to query the question and search for answer from the embeddings
def query_index(question, index, texts, urls, embeddings, top_k=5):
    q_embed = embed_model.encode([question]).astype('float32')
    D, I = index.search(q_embed, top_k)
    return [(texts[i], urls[i]) for i in I[0]]

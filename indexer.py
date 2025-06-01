import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load the embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to split long text into smaller chunks (inline instead of splitter.py)
def split_text(text, max_words=200):
    words = text.split()
    chunks = [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks

# Function to create FAISS index from documents
def create_index(docs):
    texts = []
    urls = []
    embeddings = []

    for url, doc in docs:
        chunks = split_text(doc, max_words=200)
        for chunk in chunks:
            texts.append(chunk)
            urls.append(url)
            embeddings.append(embed_model.encode(chunk))

    # Create FAISS index
    embedding_matrix = np.vstack(embeddings).astype('float32')
    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)

    return index, texts, urls, embedding_matrix

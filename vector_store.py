import faiss
import numpy as np
from typing import List

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.embeddings = []

    def add(self, embedding: np.ndarray, text: str):
        self.index.add(np.array([embedding]).astype('float32'))
        self.texts.append(text)
        self.embeddings.append(embedding)

    def search(self, embedding: np.ndarray, top_k: int = 3):
        D, I = self.index.search(np.array([embedding]).astype('float32'), top_k)
        return [(self.texts[i], D[0][idx]) for idx, i in enumerate(I[0]) if i < len(self.texts)]

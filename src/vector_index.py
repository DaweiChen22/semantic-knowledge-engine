import numpy as np
from sklearn.preprocessing import normalize

class HybridVectorIndex:
    """Enterprise-grade vector index with L2 normalization and hybrid search capabilities."""
    def __init__(self, dim: int):
        self.dim = dim
        self.index = np.empty((0, dim))
        self.metadata = []

    def add_vectors(self, vecs: np.ndarray, meta: List[str]):
        norm_vecs = normalize(vecs, axis=1)
        self.index = np.vstack([self.index, norm_vecs])
        self.metadata.extend(meta)

    def search(self, query_vec: np.ndarray, k: int = 5):
        """Optimized inner-product search (equivalent to cosine on normalized vectors)."""
        query_norm = normalize(query_vec.reshape(1, -1))
        scores = np.dot(self.index, query_norm.T).flatten()
        top_indices = np.argsort(scores)[-k:][::-1]
        return [(self.metadata[i], scores[i]) for i in top_indices]

if __name__ == "__main__":
    idx = HybridVectorIndex(128)
    data = np.random.rand(10, 128)
    idx.add_vectors(data, [f"Doc_{i}" for i in range(10)])
    res = idx.search(np.random.rand(128))
    print(f"Top Semantic Match: {res[0]}")

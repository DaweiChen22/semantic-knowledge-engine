import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class KnowledgeGraphRetriever:
    """Advanced semantic retrieval system for high-dimensional entity facts."""
    def __init__(self, embedding_model=None):
        self.entities = {}
        self.embeddings = []
        self.id_map = []

    def add_knowledge_node(self, entity_id: str, fact_embedding: np.ndarray, metadata: dict):
        """Registers a new fact in the semantic index."""
        self.entities[entity_id] = metadata
        self.embeddings.append(fact_embedding)
        self.id_map.append(entity_id)

    def query_semantic_context(self, query_vec: np.ndarray, top_k: int = 5):
        """Retrieves most relevant knowledge nodes based on latent proximity."""
        if not self.embeddings: return []
        sims = cosine_similarity(query_vec.reshape(1, -1), np.array(self.embeddings))
        top_indices = np.argsort(sims[0])[-top_k:][::-1]
        return [(self.id_map[i], sims[0][i]) for i in top_indices]

if __name__ == "__main__":
    engine = KnowledgeGraphRetriever()
    print("Semantic retriever initialized.")

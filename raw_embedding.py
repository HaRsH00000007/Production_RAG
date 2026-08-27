# Using embedding model for the convo

from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Test text
text = "What is the capital of France?"

# Generate embedding
embedding = model.encode(text)

print("Embedding:")
print(embedding)

print("\nEmbedding dimensions:")
print(len(embedding))
import json
import math
import ollama


# -----------------------------
# Load stored embeddings
# -----------------------------

with open("embeddings.json", "r", encoding="utf-8") as file:
    embedded_chunks = json.load(file)


# -----------------------------
# Cosine similarity function
# -----------------------------

def cosine_similarity(vector_a, vector_b):

    dot_product = 0
    magnitude_a = 0
    magnitude_b = 0

    for i in range(len(vector_a)):

        dot_product += vector_a[i] * vector_b[i]

        magnitude_a += vector_a[i] ** 2

        magnitude_b += vector_b[i] ** 2

    magnitude_a = math.sqrt(magnitude_a)
    magnitude_b = math.sqrt(magnitude_b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    similarity = dot_product / (magnitude_a * magnitude_b)

    return similarity


# -----------------------------
# User question
# -----------------------------

question = "What keyword is used for inheritance in Java?"


# -----------------------------
# Create embedding for question
# -----------------------------

response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

question_embedding = response["embeddings"][0]


# -----------------------------
# Compare question with chunks
# -----------------------------

results = []

for chunk in embedded_chunks:

    score = cosine_similarity(
        question_embedding,
        chunk["embedding"]
    )

    results.append({
        "chunk_id": chunk["chunk_id"],
        "text": chunk["text"],
        "score": score
    })


# -----------------------------
# Sort by similarity
# -----------------------------

results.sort(
    key=lambda x: x["score"],
    reverse=True
)


# -----------------------------
# Display results
# -----------------------------

print("\nQuestion:")
print(question)

print("\nSemantic Search Results:")

for result in results:

    print("\n-----------------------------")

    print("Chunk ID:", result["chunk_id"])

    print("Similarity Score:", result["score"])

    print("Text:")
    print(result["text"])
    
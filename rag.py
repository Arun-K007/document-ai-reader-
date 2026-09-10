import json
import math
import ollama


# -----------------------------
# Configuration
# -----------------------------

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "gemma3:latest"

SIMILARITY_THRESHOLD = 0.60
TOP_K = 2


# -----------------------------
# Load document embeddings
# -----------------------------

def load_embeddings(embeddings_path):

    with open(embeddings_path, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# Cosine similarity
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

    return dot_product / (magnitude_a * magnitude_b)


# -----------------------------
# Search document
# -----------------------------

def search_documents(question, embedded_chunks):

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=question
    )

    question_embedding = response["embeddings"][0]

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

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    relevant_chunks = []

    for result in results:

        if result["score"] >= SIMILARITY_THRESHOLD:
            relevant_chunks.append(result)

    return relevant_chunks[:TOP_K]


# -----------------------------
# Create context
# -----------------------------

def create_context(chunks):

    context = ""

    for chunk in chunks:

        context += chunk["text"] + "\n\n"

    return context


# -----------------------------
# Generate answer using Gemma
# -----------------------------

def generate_answer(question, context):

    prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the information provided in the context.

Do not use your general knowledge.

If the answer is not present in the context, respond exactly with:

The information is not present in the document.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# -----------------------------
# Ask question
# -----------------------------

def ask_question(question, embeddings_path="embeddings.json"):

    embedded_chunks = load_embeddings(
        embeddings_path
    )

    relevant_chunks = search_documents(
        question,
        embedded_chunks
    )

    # -----------------------------
    # Check if information exists
    # -----------------------------

    if len(relevant_chunks) == 0:

        return "The information is not present in the document."

    # -----------------------------
    # Create context
    # -----------------------------

    context = create_context(
        relevant_chunks
    )

    # -----------------------------
    # Generate answer
    # -----------------------------

    answer = generate_answer(
        question,
        context
    )

    return answer


# -----------------------------
# Main program
# -----------------------------

if __name__ == "__main__":

    question = input(
        "\nAsk a question about the document: "
    )

    answer = ask_question(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)
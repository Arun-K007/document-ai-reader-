import ollama
import json

from document_processor import extract_text, create_chunks


# -----------------------------
# Configuration
# -----------------------------

EMBEDDING_MODEL = "nomic-embed-text"


# -----------------------------
# Create embeddings
# -----------------------------

def create_embeddings(pdf_path, output_path="embeddings.json"):

    # Extract text from PDF
    text = extract_text(pdf_path)

    # Create chunks
    chunks = create_chunks(text)

    print("Total characters:", len(text))
    print("Total chunks:", len(chunks))

    # Create embeddings
    embedded_chunks = []

    for i, chunk in enumerate(chunks):

        response = ollama.embed(
            model=EMBEDDING_MODEL,
            input=chunk
        )

        embedding = response["embeddings"][0]

        embedded_chunks.append({
            "chunk_id": i,
            "text": chunk,
            "embedding": embedding
        })

    # Save embeddings
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(embedded_chunks, file)

    print("\nEmbeddings created successfully!")
    print("Number of chunks:", len(embedded_chunks))
    print("Embedding dimensions:", len(embedded_chunks[0]["embedding"]))
    print(f"Embeddings saved to {output_path}")


# -----------------------------
# Main program
# -----------------------------

if __name__ == "__main__":

    pdf_path = input("\nEnter PDF file path: ")

    create_embeddings(pdf_path)
def create_chunks(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks


text = """
Java is a programming language.
Java supports object-oriented programming.
Inheritance allows a child class to acquire properties
and methods from a parent class.
Java uses the extends keyword for inheritance.
Polymorphism allows an object to take multiple forms.
"""

chunks = create_chunks(text)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)
import fitz


def extract_text(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text

def create_chunks(text, chunk_size=500, overlap=50):
    words = text.split()

    chunks = []

    current_chunk = []
    current_length = 0

    for word in words:

        word_length = len(word) + 1

        if current_length + word_length > chunk_size:

            chunks.append(" ".join(current_chunk))

            # Keep words from the end for overlap
            overlap_words = []
            overlap_length = 0

            for previous_word in reversed(current_chunk):

                if overlap_length + len(previous_word) + 1 > overlap:
                    break

                overlap_words.insert(0, previous_word)
                overlap_length += len(previous_word) + 1

            current_chunk = overlap_words
            current_length = sum(len(w) + 1 for w in current_chunk)

        current_chunk.append(word)
        current_length += word_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

pdf_path = "sample.pdf"

text = extract_text(pdf_path)

chunks = create_chunks(text)

print("Total characters:", len(text))
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:5]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)
    
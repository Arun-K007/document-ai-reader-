# AI-Powered Document Question Answering System

An AI-powered application that allows users to upload documents and interact with them using natural language.

The goal of this project is to build a document intelligence system that can understand the content of a user's document, retrieve relevant information, and generate answers based only on the information available in the uploaded document.

 Project Goal

Large documents can be difficult and time-consuming to read and understand.

This project aims to provide an AI assistant that can:

- Answer questions based on uploaded documents
- Simplify complex content
- Summarize large sections of documents
- Explain content in simple language
- Provide personalized responses based on the document
- Refuse to answer when the requested information is not available in the document

### Example

If a document contains information about Java inheritance and the user asks:

> What keyword is used for inheritance in Java?

The system should retrieve the relevant information and answer:

> The `extends` keyword is used for inheritance in Java.

If the user asks:

> Who created Java?

and that information does not exist in the uploaded document, the system should respond:

> This information is not present in the uploaded document.

The system should not use unrelated external knowledge to answer unsupported questions.

---

## 🧠 Planned AI Architecture

The final system will use a Retrieval-Augmented Generation (RAG) architecture.

```text
User Uploads Document
          │
          ▼
   Document Processing
          │
          ▼
      Text Extraction
          │
          ▼
       Text Chunking
          │
          ▼
       Embeddings
          │
          ▼
    Vector Database
          │
          │
     User Question
          │
          ▼
    Query Embedding
          │
          ▼
      Retrieval
          │
          ▼
 Relevant Document Chunks
          │
          ▼
     Relevance Check
          │
       ┌──┴──┐
       │     │
      YES    NO
       │     │
       ▼     ▼
      LLM   "Information
       │     not present"
       ▼
  Grounded Answer

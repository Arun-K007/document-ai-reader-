import streamlit as st

from embeddings import create_embeddings
from rag import ask_question


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Document AI",
    page_icon="📄",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("📄 Document AI")

st.write(
    "Upload a PDF and ask questions using "
    "AI-powered document search."
)


# -----------------------------
# Initialize Session State
# -----------------------------

if "document_processed" not in st.session_state:
    st.session_state["document_processed"] = False

if "embeddings_path" not in st.session_state:
    st.session_state["embeddings_path"] = None

if "uploaded_filename" not in st.session_state:
    st.session_state["uploaded_filename"] = None

if "messages" not in st.session_state:
    st.session_state["messages"] = []


# -----------------------------
# Upload PDF
# -----------------------------

st.subheader("1️⃣ Upload Document")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


# -----------------------------
# Process PDF
# -----------------------------

if uploaded_file is not None:

    pdf_path = "uploaded_document.pdf"
    embeddings_path = "uploaded_document_embeddings.json"

    # Save uploaded PDF
    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.info(
        f"Selected document: **{uploaded_file.name}**"
    )

    if st.button("🔄 Process Document"):

        with st.spinner(
            "Reading document and creating embeddings..."
        ):

            create_embeddings(
                pdf_path,
                embeddings_path
            )

        st.session_state["document_processed"] = True
        st.session_state["embeddings_path"] = embeddings_path
        st.session_state["uploaded_filename"] = uploaded_file.name

        # Clear old chat when a new document is processed
        st.session_state["messages"] = []

        st.success(
            "✅ Document processed successfully!"
        )


# -----------------------------
# Document Status
# -----------------------------

if st.session_state["document_processed"]:

    st.divider()

    st.subheader("2️⃣ Document Status")

    st.success(
        f"✅ Ready: {st.session_state['uploaded_filename']}"
    )


    # -----------------------------
    # Chat History
    # -----------------------------

    st.subheader("3️⃣ Document Chat")


    # Display previous messages

    for message in st.session_state["messages"]:

        with st.chat_message("user"):
            st.write(message["question"])

        with st.chat_message("assistant"):
            st.write(message["answer"])


    # -----------------------------
    # Question Input
    # -----------------------------

    question = st.chat_input(
        "Ask something about the document..."
    )


    if question:

        # Display user question immediately
        with st.chat_message("user"):
            st.write(question)


        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner(
                "Searching the document..."
            ):

                answer = ask_question(
                    question,
                    st.session_state["embeddings_path"]
                )

            st.write(answer)


        # Save conversation
        st.session_state["messages"].append({
            "question": question,
            "answer": answer
        })
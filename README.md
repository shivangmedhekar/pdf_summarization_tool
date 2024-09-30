
# PDF Summarization App

  

## Overview
The **PDF Summarization App** is a Streamlit-based web application that allows users to upload a PDF document and generate a concise summary of its contents in just a few seconds. The app leverages advanced Natural Language Processing (NLP) techniques, utilizing OpenAI's GPT models and LangChain's embedding-based text processing to provide accurate and relevant summaries of uploaded PDFs.

  

## Features
-  **Upload PDF**: Easily upload your PDF documents.
-  **Generate Summary**: Quickly generate a summary of the uploaded PDF with the click of a button.
-  **Powered by OpenAI GPT**: Utilizes OpenAI's `gpt-3.5-turbo-16k` model for high-quality summaries.
-  **Advanced NLP Processing**: Uses LangChain and HuggingFace's embeddings for efficient text processing and summarization.

  

## Technologies Used
-   **Streamlit**: For building the interactive web interface.
-   **OpenAI API**: To leverage GPT models for generating summaries.
-   **LangChain**: For efficient text processing and chain management.
-   **HuggingFace Transformers**: For embedding text chunks.
-   **PyPDF2**: For extracting text from PDF documents.
-   **FAISS**: For similarity search and efficient retrieval of relevant text chunks.
-   **python-dotenv**: For managing environment variables securely.

  

### Installation

1.  **Clone the Repository**

```bash
git clone https://github.com/shivangmedhekar/pdf_summarization_tool.git
cd pdf_summarization_tool
```

2.  **Create a Virtual Environment (Optional but Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```
  
3. **Install Dependencies**
```bash
pip  install  -r  requirements.txt
```

4. **Set Up Environment Variables**
- Create a `.env` file in the root directory.
- Add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key
```



## Usage

1.  **Run the Application**

    ```bash
	streamlit run code/pdf.py
	```
    
2.  **Interact with the App**
    - Open the provided URL in your web browser.
    - Upload your PDF document using the file uploader.
    - Click the "Generate Summary" button to receive a concise summary of your PDF.

## Code Structure

### `pdf.py`
-   **Purpose**: Serves as the main entry point of the application.
-   **Functionality**:
    -   Sets up the Streamlit user interface.
    -   Handles PDF uploads and user interactions.
    -   Calls the `summarizer` function from `backend.py` to generate summaries.
    -   Displays the generated summary on the web page.

### `backend.py`
-   **Purpose**: Contains the core logic for processing PDFs and generating summaries.
-   **Key Components**:
    -   **Text Processing**:
        -   Splits extracted text into manageable chunks using `CharacterTextSplitter`.
        -   Embeds text chunks using HuggingFace's `all-MiniLM-L6-v2` model.
        -   Creates a FAISS-based knowledge base for efficient similarity search.
    -   **Summarization**:
        -   Extracts text from the uploaded PDF using `PyPDF2`.
        -   Searches for relevant text chunks related to the summarization query.
        -   Utilizes OpenAI's GPT model (`gpt-3.5-turbo-16k`) via LangChain's `ChatOpenAI` for generating the summary.


## Environment Variables

The application requires an OpenAI API key to function correctly. Store your API key in a `.env` file in the root directory:

```bash
OPENAI_API_KEY = #your_openai_api_key
``` 


## License

This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)




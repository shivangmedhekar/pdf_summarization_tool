import streamlit as st
import os
from dotenv import load_dotenv

from backend import *
load_dotenv()

def main():
    
    st.set_page_config(page_title='PDF Summarizer')
    
    st.title("PDF Summarization App")
    st.write("Summarize your pdfs in few seconds.")
    st.divider()
    
    pdf = st.file_uploader('Upload your PDF Document', type='pdf')
    
    submit = st.button('Generate Summary')
    
    os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
    
    if submit:
        response = summarizer(pdf)
        
        st.subheader('Summary of File')
        st.write(response)
        
    
    
if __name__ == '__main__':
    main()
from dotenv import load_dotenv
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Qdrant")
    st.header("Ask your remote database 💬")

    # show user input
    user_question = st.text_input("Ask a question about your PDF:")
        
if __name__ == '__main__':
    main()

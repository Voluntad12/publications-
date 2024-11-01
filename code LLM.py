import os 
import streamlit as st 
import pickle 
import time 
import langchain 
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.document_loaders import UnstructuredURLLoader 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

st.title("News Research Tool")
st.sidebar.title("New Article URLs")

for i in range(3): 
    st.sidebar.text_input(f"URL {i+1}")

process_url_clicked=st.sidebar.button("Process URLs")

if process_url_clicked: 
    #loading
    loader=UnstructuredURLLoader(urls=urls)
    data=loader.load()
    #splitting 
    text_splitter=RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','], 
        chunk_size=1000
    )
    docs=text_splitter.split_documents(data)
    embeddings=OpenAIEmbeddings()
    vectorstore_openai=FAISS.from_documents(docs,embeddings)
    with open(file_path,"wb") as f : 
        pickle.dump(vectorstore_openai,f)
        chain=RetrivalQWAithSourceChain.from_llm(llm=llm,retriever=vectorstore.as_retriever())
        result=chain({"question":query}, return_only_outputs=True)
        st.header
        st.subheader(result["answer"])
        #to display sources for every result founded 
        sources=results.get("sources","")
        if sources : 
            st.subheader("sources:")
            sources_list=sources.split("\n")
            for source in sources_list : 
                st.write(source)
                
        
        



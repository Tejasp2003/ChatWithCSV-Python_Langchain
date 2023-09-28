import streamlit as st
from  langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv() # load env variables
    st.set_page_config(page_title="Chat With CSV 📊") # set page title means change the tab name
    st.header("Chat With CSV 📊") # header is the title of the page

    user_csv= st.file_uploader("Upload Your CSV", type=["csv"]) # upload csv file

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV") # ask question
        llm = OpenAI(temperature=0)
        agent  =  create_csv_agent(llm, user_csv, Verbose=True) # create agent

        if user_question is not None or user_question != " ":
            answer = agent.run(user_question) # run agent and get 
            st.write(answer)

            # Store the conversation
            conversation = []
            conversation.append({"role": "user", "content": user_question})
            conversation.append({"role": "assistant", "content": answer})

            # Display the conversation
            

            # Empty the input field
            user_question = ""
        
if __name__ == "__main__":  # if this file is run directly, then run main()
    main()

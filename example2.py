##intergrate our code with open ai api
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st 
os.environ["OPENAI_API_KEY"]=openai_key

#streamlit framework

st.title('celebrity search Reasults')
input_text=st.text_input("search the topic you want")

#prompt template
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="tell me about celebrity {name}"
    )

##OPENAI LLM MODEL
llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True)




if input_text:
    st.write(chain.run(input_text))


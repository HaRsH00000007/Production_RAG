from dotenv import load_dotenv
load_dotenv()

#from langchain_core import __version__ as core_version
#from langgraph import __version__ as lg_version 
#from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic

from importlib.metadata import version as get_version
from langchain_core import __version__ as core_version
from langchain_groq import ChatGroq

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {get_version('langgraph')}")  

def main():
    # Testing Groq
    llm=ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    response= llm.invoke("Say set up complete in one word")
    print(f"Response from GROQ:{response}")
    
    print ("Set up Complete")
    
if __name__=="__main__":
  main()
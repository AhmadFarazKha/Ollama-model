from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="gemma:2b")  # Make sure the model is downloaded

chain = prompt | model

result = chain.invoke({"question": "Highest AI skill in demand in saudi arabia?"})

print(result)
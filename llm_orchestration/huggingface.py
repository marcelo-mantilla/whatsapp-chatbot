from langchain import PromptTemplate, HuggingFaceHub, LLMChain

from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
flan_t5 = HuggingFaceHub(
    repo_id="google/flan-t5-xl",
    model_kwargs={"temperature": 1e-10},
)

template = """Question: {question}
Answer:
"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(
    prompt=prompt,
    llm=flan_t5,
)

question = 'Which NFL team won the Super Bowl in the 2010 season?'

print(llm_chain.run(question))

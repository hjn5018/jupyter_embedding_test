from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
# print(type(llm.invoke("안녕?")))

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 월드 클라스 기술 문서 작성 전문가야"),
    ("user", "{input}")
])

chain = prompt | llm

# print(chain.invoke({"input": "DRF는 어떤 장점이 있어?"}))
# print(chain.invoke({"input": "프로그래밍실에 일찍 오는 사람의 이름을 알려줘."}))

from langchain.chains.combine_documents import create_stuff_documents_chain

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("""주어진 context에만 기반해서 다음에 주어지는 질문에 답하도록
                                          
                                          <context>
                                          {context}
                                          </context>
                                          
                                          질문: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

from langchain_core.documents import Document

print(document_chain.invoke({
    "input": "프로그래밍실에 일찍 오는 사람의 이름을 알려줘.",
    "context": [
        Document(page_content="프로그래밍실에 일찍 오는 사람은 지뇽이야.")
    ]
}))
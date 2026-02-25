#code to configure our model
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationalBufferMemory
from config import config

class LLMService:
    def __init(self, vector_store):
        self.llm = ChatOpenAI(
            temperature =0.7,
            model_name="gpt-4.1",
            openai_api_key=config.OPEN_AI_KEY
        )

        self.memory=ConversationalBufferMemory(
            memory_key="chat_history",
            return_message=True
        )

        self.chain = ConversationalRetrievalChain(
            llm= self.llm,
            retriever= vector_store.vectorstore.as_retriever()
            memory=self.memory
        )

        def get_response(self, query):
            try:
                response = self.chain({"question": query})
                return response['answer']
            except Exception as e:
                print(f"error getting LLM response : {e}"
                return "I encountered an error processing your request"
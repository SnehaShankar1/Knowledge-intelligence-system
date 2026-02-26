#code to configure our model
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import Config

class LLMService:
    def __init__(self, vector_store):
        self.llm = ChatOpenAI(
            temperature =0.7,
            model_name="gpt-4o mini",
            openai_api_key=Config.OPENAI_API_KEY
        )

        self.memory=ConversationBufferMemory(
            memory_key="chat_history",
            return_message=True
        )

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.vector_store.as_retriever(),
            memory=self.memory
        )

    def get_response(self, query):
        try:
            response = self.chain({"question": query})
            return response['answer']
        except Exception as e:
            print(f"error getting LLM response : {e}")
            return "I encountered an error processing your request"


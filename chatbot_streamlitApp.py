import streamlit as st
import cassio
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster


# Initialize Streamlit app
st.title("Health-Care-Genie")

# API keys from Streamlit secrets
ASTRA_DB_APPLICATION_TOKEN = st.secrets["ASTRA_DB_APPLICATION_TOKEN"]
ASTRA_DB_ID = st.secrets["ASTRA_DB_ID"]
ASTRA_DB_API_ENDPOINT = st.secrets["ASTRA_DB_API_ENDPOINT"]
ASTRA_DB_KEYSPACE = st.secrets["ASTRA_DB_KEYSPACE"]
ASTRA_DB_REGION = st.secrets["ASTRA_DB_REGION"]

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]



# Initialize database and OpenAI components
# cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)


llm = OpenAI(api_key=OPENAI_API_KEY)
embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# try:
#     # Initialize the Astra client
#     client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)
#     db = client.get_database_by_api_endpoint(ASTRA_DB_API_ENDPOINT)
#     # print(f"Connected to Astra DB: {db.list_collection_names()}")
# except Exception as e:
#     st.error(f"Error checking data existence: {e}")


llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)



session_init = cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)


session = Cluster(
    cloud={"secure_connect_bundle": st.secrets["ASTRA_DB_SECURE_BUNDLE_PATH"]}, 
    auth_provider=PlainTextAuthProvider("token", ASTRA_DB_APPLICATION_TOKEN),
).connect()

astra_vector_store = Cassandra(
    embedding=embedding,
    table_name="usa_health_care_DB",
    session=session,
    keyspace=None,
)


astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask your healthcare related question:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    

    with st.chat_message("user"):
        st.markdown(prompt)
    
    # assistant's response
    with st.chat_message("assistant"):
        response = astra_vector_index.query(prompt, llm=llm).strip()
        st.markdown(response)
    
    # Add response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

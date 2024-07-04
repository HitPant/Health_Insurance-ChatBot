# Health_Insurance-ChatBot

![chatbot](https://github.com/HitPant/Health_Insurance-ChatBot/assets/30971790/283df540-37a2-427c-a2cb-4726f4b43d25)


## Introduction
This project aims to assist both U.S. residents and international students in understanding the complexities of the U.S. medical insurance system. It provides insights into how the system operates, the various types of insurance available, and key policy-related terms and information.

Utilizing specialized dataset focused on insurance, this chatbot has been designed to provide precise and accurate answers to your queries, ensuring you have the information you need at your fingertips.

## Objective
Develop a Retrieval-Augmented Generation (RAG) based chatbot using LangChain and OpenAI in Python. Extract data from various PDFs, split it into text chunks, and convert these chunks into vectors using OpenAI Embeddings. Store the vectors in a Cassandra database. Upon user query, perform a similarity search in the vector database to provide relevant responses.

## Tech Stack
#### Streamlit
Used for building the web application interface for the chatbot.
#### LangChain
- Manages vector storage using Cassandra.
- Wrap vector store for indexing and querying.
#### OpenAI
OpenAIEmbeddings: Converts text chunks into vector embeddings using OpenAI.
OpenAI's language models for generating responses.
#### Cassandra
Used for connecting to and authenticating with the Cassandra database.

## Future 
- Add more related data.
- Improvise the chatbot interface
- Advance and Efficient search methods

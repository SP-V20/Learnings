What is LangChain?
A Python framework that makes it easy to build applications using LLMs. Instead of writing complex API code yourself, LangChain gives you ready-made building blocks.

Think of it like this:
Without LangChain:
  You write 100 lines to connect OpenAI + search + memory + output
With LangChain:
  Same thing in 10 lines using pre-built components
  
5 Core Building Blocks:
  1. LLM          → the AI brain (OpenAI, Claude, Llama)
  2. Prompt       → template for your instructions to the LLM
  3. Chain        → connects prompt + LLM + output together
  4. Retriever    → fetches relevant documents (RAG)
  5. Memory       → remembers previous conversation turns

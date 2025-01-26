# Ollama Deep Researcher

Ollama Deep Researcher is a web research and summarization assistant that autonomously goes down the rabbit-hole of any user-defined topic. It uses a local LLM hosted by [Ollama](https://ollama.com/search) to generate a search query based on the user's topic, gets web search results, and uses an LLM to summarize the results. It then uses the same LLM to reflect on the summary, examine knowledge gaps, and generate a new search query to fill the gaps. This repeats for a user-defined number of cycles, iteratively updating and improving the summary with new information from web search and providing the user a final markdown summary with all sources used. It is configured to run with fully local any LLMs (via [Ollama](https://ollama.com/search)). 

![research-rabbit](https://github.com/user-attachments/assets/4308ee9c-abf3-4abb-9d1e-83e7c2c3f187)

## 🚀 Quickstart

Pull a local LLM that you want to use from [Ollama](https://ollama.com/search):
```bash
ollama pull llama3.2
ollama pull deepseek-r1:1.5b
```

For free web search (up to 1000 requests), [you can use the Tavily API](https://tavily.com/):
```bash
export TAVILY_API_KEY=<your_tavily_api_key>
```

Clone the repository and launch the assistant with the LangGraph server:
```bash
git clone https://github.com/sheikhDipta003/deep-researcher.git
cd ollama-deep-researcher
python .\main.py
```

You should see the final output in the form of a json object which is basically the graph state.

In the [configuration.py](configuration.py) file:
* You can set the name of your local LLM to use with Ollama (it will by default be `deepseek-r1:1.5b`) `local_llm: str = "deepseek-r1:1.5b"`
* You can set the depth of the research iterations (it will by default be `3`) `max_web_research_loops: int = 3`

## How it works

Research Rabbit is a AI-powered research assistant that:
- Given a user-provided topic, uses a local LLM (via [Ollama](https://ollama.com/search)) to generate a web search query
- Uses a search engine (configured for [Tavily](https://www.tavily.com/)) to find relevant sources
- Uses a local LLM to summarize the findings from web search related to the user-provided research topic
- Then, it uses the local LLM to reflect on the summary, identifying knowledge gaps
- It generates a new search query to address the knowledge gaps
- The process repeats, with the summary being iteratively updated with new information from web search
- It will repeat down the research rabbit hole 

This is inspired by [IterDRAG](https://arxiv.org/html/2410.04343v1#:~:text=To%20tackle%20this%20issue%2C%20we,used%20to%20generate%20intermediate%20answers.), which handles complex queries by decomposing the query into simpler sub-queries. This follows a sequential, interleaved process where each sub-query depends on the answer retrieved from the previous one, enabling dynamic query decomposition and adaptive retrieval.

## Outputs

The output of the graph is a json object (currently printed in console) containing the research summary, with citations to the sources used.

All sources gathered during research are saved to the graph state. 



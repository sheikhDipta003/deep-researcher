import asyncio
from graph import graph
from state import SummaryStateInput

async def main():
    inputs = SummaryStateInput(research_topic="The creation and evolution of japanese manga strictly within 500 words.")
    results = await graph.ainvoke(inputs)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
    
    
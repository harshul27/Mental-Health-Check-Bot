from dotenv import load_dotenv; load_dotenv()
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from gemini_setup import llm, prompt, parser
from schema import MoodResponse

agent = create_tool_calling_agent(llm = llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_history = []

print("Welcome to the Mental Health Check-in Bot!(Type 'exit' to quit)")

while True:
    q = input("You: ")
    if q.lower() == 'exit': break
    chat_history.append(HumanMessage(content=q))
    response  = executor.invoke({"query": q, "chat_history": chat_history})

    try:
        output = parser.parse(response['output'])
        print("\n How are you feeling:", output.mood_summary)
        print("Suggested activity:", output.suggestions)
        print("Log status:", output.log_status)
        chat_history.append(AIMessage(content=output.mood_summary))
        
    except Exception as e:
        print("Error parsing response:", e)
        print("Response:", response.get('output'))

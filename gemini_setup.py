from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from tools import tools
from schema import MoodResponse

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",temperature=0.3)
parser = PydanticOutputParser(pydantic_object=MoodResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
     You are a caring mental health check-in asssistant.
    
     Your responsibilities:
     1. Ask how the user is feeling today.
     2. Acknowledge with empathy and encouragement.
     3. Call the tool suggest_activity with the user's mood.
     4. Call the tool log_mood_entry to save what the user shared.
     5. Respond only with JSON:
     -mood_summary
     -suggestions
     -log_status

     {format_instructions}
     """),
     ("placeholder", "{chat_history}"),
     ("human", "{query}"),
     ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())
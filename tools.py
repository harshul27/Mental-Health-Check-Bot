import os, datetime
from langchain.tools import Tool

#log the user's check-in to a dated log file

def log_mood_entry(entry:str):
    os.makedirs('logs', exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}_mood_log.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {entry}\n")
    return f"Logged mood entry: {entry} at {timestamp}"

#Suggest self-care  activity based on emotional state
def suggest_activity(mood:str):
    mood = mood.lower()
    if "anxious" in mood or "stressed" in mood:
        return "Consider taking a short walk, practicing deep breathing, or meditating."
    elif "sad" in mood or "depressed" in mood:
        return "Listening to your favorite music or talking to a friend can help lift your spirits."
    elif "happy" in mood or "excited" in mood:
        return "Consider doing something creative, like drawing or writing, to express your emotions."
    elif "angry" in mood:
        return "Pause and do a quick grounding exercise, like counting to ten or focusing on your breath."
    elif "tired" in mood:
        return "Make sure to rest and consider taking a short nap or practicing some gentle stretching."
    elif "calm" in mood or "relaxed" in mood:
        return "Great! Keep up the good work. Maybe do some light reading or enjoy a hobby. Maybe write in your gratitude journal or listen to your favorite song"
    else:
        return "It's important to acknowledge your feelings. Consider talking to someone you trust or writing in a journal about how you feel."
    
    #Register the tools for use in the LangChain framework
    
    tools =[
        Tool(name="log_mood_entry", func=log_mood_entry, description="Log the user's mood check-in to a file"),
           Tool(name="suggest_activity", func=suggest_activity, description="Suggest a self-care activity based on the user's mood")
           
    ]
import os
import json
from dotenv import load_dotenv
from typing import TypedDict, List
from fuzzywuzzy import fuzz
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

# Load environment variables
load_dotenv()
BOT_NAME = os.getenv("BOT_NAME", "FAQ Bot")

# Load FAQ data from JSON file
with open("faq_data.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

# Define the state structure
class FAQBotState(TypedDict):
    messages: List[str]

# Fuzzy match function
def find_faq_answer(state: FAQBotState) -> FAQBotState:
    user_question = state["messages"][-1].strip().lower()
    best_score = 0
    best_answer = "Sorry, I couldn't find an answer to your question."

    for question, answer in faq_data.items():
        score = fuzz.partial_ratio(user_question, question.lower())
        if score > best_score:
            best_score = score
            best_answer = answer

    # Threshold can be tuned
    if best_score >= 70:
        return {"messages": state["messages"] + [best_answer]}
    else:
        return {"messages": state["messages"] + ["Sorry, I couldn't find an answer to your question."]}

# LangGraph flow
graph = StateGraph(FAQBotState)
graph.add_node("faq_lookup", RunnableLambda(find_faq_answer))
graph.set_entry_point("faq_lookup")
faq_bot = graph.compile()

def chat():
    print(f"🤖 Welcome to {BOT_NAME}! Type 'exit' to quit.\n")
    messages = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        messages.append(user_input)
        state = {"messages": messages}
        result = faq_bot.invoke(state)
        messages = result["messages"]
        print(f"{BOT_NAME}: {messages[-1]}")

if __name__ == "__main__":
    chat()

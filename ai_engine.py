from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
import os
from dotenv import load_dotenv
import openai
# Load environment variables
load_dotenv()
# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# AI Model Config
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)
# combined_input=""
# theme=""
# desired_standard=""
# tone=""


def generatePlan(combined_input: str, theme: str, desired_standard: str, tone: str):
    prompt_build = f"""
    You are a curriculum co-design assistant helping a teacher build a new lesson from source material.

    --- START MATERIAL ---
    {combined_input}
    --- END MATERIAL ---

    Please respond with the following:
    1. Learning Objectives (aligned to ELA standards)
    2. Scaffolded Supports for student understanding
    3. Instructional Protocols to boost engagement
    4. Student Voice or Identity-Driven Prompt

    Theme focus: {theme}
    Targeted Standards: {desired_standard}
    Tone: {tone}
    """
    
    prompt = ChatPromptTemplate.from_template(
        str(prompt_build)
    )
    response = llm(prompt.format_messages(combined_input=combined_input, theme=theme, desired_standard=desired_standard, tone=tone))
    return response.content


# Graph-based AI processing using LangGraph

class skaiGraph(StateGraph):
    def __init__(self):
        super().__init__()
        self.add_node("generate_plan", generatePlan, END)
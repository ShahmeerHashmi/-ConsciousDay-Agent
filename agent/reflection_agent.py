import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = st.secrets["OPENROUTER_API_KEY"]
llm = ChatOpenAI(
    model="deepseek/deepseek-r1:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENAI_API_KEY"],
    temperature=0.7,
)

prompt_template = """
You are a daily reflection and planning assistant...

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy
"""

def generate_reflection(journal, dream, intention, priorities):
    prompt = PromptTemplate.from_template(prompt_template)
    final_prompt = prompt.format(
        journal=journal,
        dream=dream,
        intention=intention,
        priorities=priorities
    )
    response = llm.invoke([HumanMessage(content=final_prompt)])
    parts = response.content.split("4. Suggested Day Strategy")
    return {
        "reflection": parts[0].strip(),
        "strategy": parts[1].strip() if len(parts) > 1 else "N/A"
    }

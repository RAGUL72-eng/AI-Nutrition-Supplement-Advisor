
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


def ask_nutrition_question(question):
    if not question.strip():
        return "Please enter a question."

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return (
            "Groq API key not found. "
            "Please add GROQ_API_KEY to your .env file."
        )

    try:
        model_name = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile"
        )

        model = ChatGroq(
            model=model_name,
            api_key=api_key,
            temperature=0.3,
            max_retries=2
        )

        response = model.invoke([
            SystemMessage(
                content=(
                    "You are a friendly AI nutrition and fitness "
                    "education assistant. Explain things simply. "
                    "Give general nutrition information, meal ideas, "
                    "and basic supplement education. Do not diagnose "
                    "medical conditions or prescribe medication. "
                    "Do not recommend extreme diets. "
                    "For medical conditions, allergies, pregnancy, "
                    "or medication use, advise the user to consult "
                    "a qualified healthcare professional."
                )
            ),
            HumanMessage(content=question)
        ])

        return response.content

    except Exception as exc:
        return f"Groq chatbot error: {exc}"

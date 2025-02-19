import operator
from dotenv import load_dotenv
import os

from groq import Groq  # Using Groq's deepseek-r1-distill-llama-70b model
import streamlit as st

def configure():
    load_dotenv()
    
configure()
   

# Initialize Groq client
client = Groq(api_key=os.environ.get("api_key"))

# Dictionary to map operators to functions
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod
}

def evaluate_expression(expression):
    """Evaluates a mathematical expression with multiple operands and operators."""
    try:
        # Validate and evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, operations)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def generate_ai_explanation(expression, result):
    """Generates a step-by-step AI-powered explanation for the given calculation."""
    prompt = f"Explain step by step how to solve the mathematical expression: {expression}. The result is {result}."

    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor that explains calculations step by step."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=False,
        reasoning_format="raw"
    )
    return completion.choices[0].message.content

def generate_ai_learning_suggestion(expression):
    """Generates AI-powered personalized learning suggestions based on user input patterns."""
    prompt = f"Based on the user's frequent mistakes in calculations like {expression}, suggest personalized learning tips to improve their math skills."

    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {"role": "system", "content": "You are a math tutor that provides personalized learning suggestions based on user mistakes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=False,
        reasoning_format="raw"
    )
    return completion.choices[0].message.content

# Streamlit UI
def main():
    
    st.title("AI-Powered Calculator with Learning Suggestions")

    # Display available operations
    st.write("**Available Operations:** +, -, *, /, ** (power), % (modulo)")

    expression = st.text_input("Enter a mathematical expression (e.g., 3 + 5 * 2)")

    if st.button("Calculate"):
        result = evaluate_expression(expression)

        if isinstance(result, str) and result.startswith("Error"):
            st.error(result)
        else:
            explanation = generate_ai_explanation(expression, result)
            learning_suggestion = generate_ai_learning_suggestion(expression)


            st.subheader("Step-by-Step Explanation")
            st.write(explanation)

           
            st.subheader("Result:")
            st.write(result)

            st.subheader("Personalized Learning Suggestion")
            st.write(learning_suggestion)

if __name__ == "__main__":
    main()
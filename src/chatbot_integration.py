import openai
import os
from chatbot import search_recipes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to handle user queries
def ask_chatbot(prompt):
    # Use the ChatCompletion API instead of Completion
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Ensure this is a valid ChatCompletion model name
        messages=[
            {"role": "system", "content": "You are a cooking assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    # The chat completion response has a different structure
    return response["choices"][0]["message"]["content"]

# Example combined interaction: Using dataset + OpenAI
def chatbot_query(query_type, **kwargs):
    if query_type == "ingredient":
        ingredient = kwargs.get("ingredient")
        result = search_recipes(ingredient=ingredient)
        if result.empty:
            return f"No recipes found for ingredient: {ingredient}"
        return result.head().to_string(index=False)

    elif query_type == "openai":
        prompt = kwargs.get("prompt")
        return ask_chatbot(prompt)

    else:
        return "Unsupported query type."

# Test the chatbot
if __name__ == "__main__":
    # Example: Search recipes with an ingredient
    print(chatbot_query(query_type="ingredient", ingredient="chicken"))
    # Example: Use OpenAI for a general cooking query
    print(chatbot_query(query_type="openai", prompt="How do I make a chocolate cake?"))

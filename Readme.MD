# Cooking Chatbot

![APP Screenshot](https://github.com/Manuele-T/Chatbot-recipes/blob/main/screenshots/Chatbot.jpg)

This project is a cooking assistant chatbot that suggests recipes based on user-provided ingredients. It uses a language model to interpret free-text inputs and generate coherent, context-aware recipe suggestions. Users can list what they have in their kitchen and receive a step-by-step cooking idea in return.

The chatbot was built in Python and uses the OpenAI API for natural language processing. The goal was to create a lightweight prototype that turns basic input into useful cooking instructions.

## Key Features
- Accepts natural language ingredient input (e.g., *"I have eggs, spinach, and cheese"*)
- Returns a complete recipe with instructions
- Lightweight UI built for quick testing and usability
- Modular codebase organized across `src/` and `notebooks/` for experimentation and development

## Development Notes
- The model is stateless — it doesn’t remember past interactions.
- A `.env` file with an OpenAI API key is required to run the application.
- The interface is intentionally minimal, with screenshots available in the `screenshots/` folder.

> ⚠️ **Note**: Running the app requires both a valid OpenAI API key and a local dataset file, neither of which are included in this repository.  
> If you’re interested in seeing the system in action, I’d be happy to demonstrate it via an online call.

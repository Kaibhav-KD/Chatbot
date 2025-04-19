import google.generativeai as genai
from datetime import datetime
import os

# ✅ Set your API Key directly here
genai.configure(api_key="AIzaSyBKtpGdHGnXDRTqzYzsI6fHMHfS_jJD6Wk")

# ✅ Configure model behavior
generation_config = {
    "temperature": 0.7,  # Controls randomness: 0.0 = deterministic, 1.0 = creative
    "top_p": 0.8,       # Controls diversity of responses
    "top_k": 40,        # Controls diversity of responses
    "max_output_tokens": 2048,  # Maximum length of response
}

# ✅ Configure safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# ✅ System instructions to guide Mitra's behavior
system_instructions = """
You are Mitra, a helpful and friendly AI assistant. Your responses should be:
1. Clear and concise
2. Professional yet approachable
3. Focused on being helpful
4. Factual and accurate
5. Culturally sensitive and inclusive
6. Always response like a friend or explain like teacher.
7. Being coversational and friendly. And Ask the user name and answer by him or her name .
"""

# ✅ Load the Gemini model with configurations
model = genai.GenerativeModel(
    "gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_instructions
)

def get_time_based_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 22:
        return "Good evening"
    else:
        return "Good night"

def log_conversation(user_name, user_input, bot_response):
    # Create chatlogs directory if it doesn't exist
    if not os.path.exists('chatlogs'):
        os.makedirs('chatlogs')
    
    # Create a log file with current date
    log_file = f'chatlogs/chat_{datetime.now().strftime("%Y-%m-%d")}.txt'
    
    # Format the conversation entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n[{timestamp}]\n{user_name}: {user_input}\nMitra: {bot_response}\n"
    
    # Append to the log file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)

# ✅ Start chat loop
def chat():
    print("🤖 Mitra is ready!\n")
    chat_session = model.start_chat(history=[])
    
    # Get user's name
    user_name = input("🤖 Mitra: What's your name? ")
    greeting = get_time_based_greeting()
    print(f"\n🤖 Mitra: {greeting}, {user_name}! How can I help you today?\n")

    while True:
        user_input = input(f"🧑 {user_name}: ")
        if user_input.lower() in ["exit", "quit"]:
            print(f"\n👋 Goodbye, {user_name}! Have a great day!")
            break

        try:
            response = chat_session.send_message(user_input)
            bot_response = response.text.strip()
            print("\n🤖 Mitra:", bot_response, "\n")
            
            # Log the conversation
            log_conversation(user_name, user_input, bot_response)
            
        except Exception as e:
            print("\n⚠️ Error:", e, "\n")

if __name__ == "__main__":
    chat()

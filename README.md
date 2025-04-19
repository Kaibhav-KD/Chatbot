# Chatbot
A simple terminal-based chatbot using Google's Gemini 1.5 Pro model via google-generativeai. Chat in real-time, get smart responses, and exit anytime. Lightweight, beginner-friendly, and easy to set up. Just install, add your API key, and start chatting in your terminal instantly!


🚀 Features
Chat in real-time using the Gemini 1.5 Pro model

Clean and minimal terminal interface

Handles continuous conversations

Safe exit using exit or quit

Fully written in Python

🛠️ Requirements
Python 3.8+

google-generativeai package

📦 Installation
>>bash
Copy
Edit
pip install google-generativeai
🔑 API Setup
Get your API key from Google AI Studio.

Paste it into the script or set it as an environment variable:

python
Copy
Edit
genai.configure(api_key="YOUR_API_KEY")
📄 Usage
bash
Copy
Edit
python chatbot.py
Then just start chatting!

bash
Copy
Edit
🧑 You: What is Python?
🤖 Gemini: Python is a high-level, interpreted programming language known for its readability and flexibility...
📁 File Structure
css
Copy
Edit
chatbot.py   # Main chatbot code
🤖 Model Used
gemini-1.5-pro – Google’s latest large language model designed for reasoning and creative tasks.

💡 Ideas for Extension
Add chat history or memory

Voice input/output using Speech Recognition

GUI version with Tkinter or PyQt

Web version using Flask or FastAPI


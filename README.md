# LumaChat
🌟 About LumaChat
LumaChat is a modern AI chatbot interface built using Streamlit and Google's Gemini API. It mimics a real chat app experience with a stylish UI, dark/light themes, typing animation, and user-friendly design. Whether you're building AI-powered tools or just experimenting with generative models, LumaChat gives you a sleek platform to start with.
![brave_screenshot_lumachat streamlit app](https://github.com/user-attachments/assets/71da774c-f38e-4c25-8f51-de07c8113c0e)
🛠 How to Clone and Run LumaChat from GitHub
Step 1: Clone the Repository
Open your terminal or command prompt and run:

bash
Copy
Edit
git clone https://github.com/Arihant2312/LumaChat.git
cd LumaChat
Step 2: Set Up the Environment
If you haven’t already, install Python and pip, then create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Step 3: Add Your Google API Key
Create a .env file in the project root.

Add your API key like this:

ini
Copy
Edit
GOOGLE_API_KEY=your-api-key-here
You can get your Gemini API key from: https://aistudio.google.com/app/apikey

Step 4: Run the App
Start the Streamlit server:

bash
Copy
Edit
streamlit run app.py
Then open your browser and go to:
http://localhost:8501


# Local LLM Web Assistant
This project is a lightweight Flask web application that allows users to upload .txt or .pdf files and interact with them using a locally hosted Large Language Model (LLM) like TinyLLaMA. It supports answering user queries based on the uploaded content.

🚀 Features

Upload .txt or .pdf documents
Ask natural language questions about the uploaded content
Get concise answers using a local LLM (e.g., TinyLLaMA)
Simple and clean web interface
Extensible: keywords extraction, paraphrasing, and question generation (commented out in current version)


🛠️ Setup and Run

1. Clone the repository
git clone https://github.com/yourusername/local-llm-web-assistant.git
cd local-llm-web-assistant

2. Install dependencies
Ensure you have Python 3.8+ and then:
pip install -r requirements.txt
Make sure your environment can run the TinyLLaMA or your preferred local model.

3. Start the app
python app.py
Then open your browser and go to http://127.0.0.1:5000

📄 Usage : 

Upload a .txt or .pdf file using the upload field.
Enter your question related to the content.
Click "Submit" and wait for the response from the local LLM.


🔧 Customization: 

Model Personal & Name 
Change the model and persona used in LocalLLM inside app.py:
llm = LocalLLM(persona="webassistant", model="tinyllama")
Enable More LLM Features


Uncomment the lines in app.py to use:

Keyword Extraction
Paraphrasing
Question Generation

📌 Dependencies : 

Flask
PyMuPDF / pdfminer (for PDF reading)
Your local LLM serving framework (e.g., HuggingFace Transformers, llama.cpp)

📬 TODO
Add session history or chat memory
Improve UI/UX
Deploy with Docker or Streamlit alternative
Add support for other document types (e.g., .docx)

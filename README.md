# Local LLM Web Assistant

This project is a lightweight Flask web application that allows users to upload .txt or .pdf files and interact with them using a locally hosted Large Language Model (LLM) like TinyLLaMA. It supports answering user queries based on the uploaded content.

# 🚀 Features

1.Upload .txt or .pdf documents

2.Ask natural language questions about the uploaded content

3.Get concise answers using a local LLM (e.g., TinyLLaMA)

4.Simple and clean web interface

5.Extensible: keywords extraction, paraphrasing, and question generation (commented out in current version)


# 🛠️ Setup and Run

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

# 📄 Usage : 

1.Upload a .txt or .pdf file using the upload field.

2.Enter your question related to the content.

3.Click "Submit" and wait for the response from the local LLM.


# 🔧 Customization: 

1.Model Personal & Name 

2.Change the model and persona used in LocalLLM inside app.py

3.llm = LocalLLM(persona="webassistant", model="tinyllama")

4.Enable More LLM Features


# Uncomment the lines in app.py to use:

1.Keyword Extraction

2.Paraphrasing

3.Question Generation


# 📌 Dependencies : 

1.Flask

2.PyMuPDF / pdfminer (for PDF reading)

3.Your local LLM serving framework (e.g., HuggingFace Transformers, llama.cpp)

# 📬 TODO: 

1.Add session history or chat memory

2.Improve UI/UX

3.Deploy with Docker or Streamlit alternative

4.Add support for other document types (e.g., .docx)


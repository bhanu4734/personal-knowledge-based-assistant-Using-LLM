from flask import Flask, render_template, request, redirect, url_for
from local_llm import LocalLLM
from file_loader import load_txt, load_pdf
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

llm = LocalLLM(persona="web assistant", model="tinyllama")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    # Hide keywords, paraphrased, questions by default
    keywords = None
    paraphrased = None
    questions = None
    MAX_RESULT_LEN = 1000  # Show more of the answer
    if request.method == 'POST':
        file = request.files.get('file')
        query = request.form.get('query')
        content = ''
        if file and file.filename:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            if filename.lower().endswith('.txt'):
                content = load_txt(filepath)
            elif filename.lower().endswith('.pdf'):
                content = load_pdf(filepath)
            else:
                content = "Unsupported file type."
        else:
            content = request.form.get('content', '')
        # Only process if content is not empty and not just whitespace
        if content and content.strip():
            if query and query.strip():
                # Use the full LLM response as the answer
                result = llm.answer(query, content)
                if result and len(result) > MAX_RESULT_LEN:
                    result = result[:MAX_RESULT_LEN] + '... [truncated]'
                # Hide keywords, paraphrased, questions by default
                # Uncomment below if you want to show them again
                # keywords = llm.list_keywords(content)[:5]
                # paraphrased = llm.paraphrase(content)[:400]
                # questions = llm.question_generation(content)[:3]
            else:
                result = "No query provided."
        else:
            result = "No content provided."
    else:
        content = ''
    return render_template('index.html', result=result, keywords=keywords, paraphrased=paraphrased, questions=questions, content=content)

if __name__ == '__main__':
    app.run(debug=True)

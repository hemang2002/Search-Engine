from flask import Flask, request, render_template, send_from_directory
import os
from transformers import BertTokenizer, BertModel
from ReadFile import ReadFile
from SearchEnigine import SearchEngine


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():

    query = request.form.get('search-bar')
    top_k = int(request.form.get('top-bar'))
    file = request.files.get('file')
    
    if not query or not file:
        return render_template('index.html', error="Please provide a query and upload a file.")
    
    filename = file.filename
    read = ReadFile(app.config['UPLOAD_FOLDER'], filename)
    file.save(read.file_path)
    text, txt = read.OpenFile()   

    if text == None:
        return render_template('index.html', error="Unsupported file type.")
        
    results = SearchEngine(text, tokenizer, model)
    results = results.search(query, top_k)
    
    return render_template('result.html', query=query, text=txt, results=results)


if __name__ == '__main__':
    
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
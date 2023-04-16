import os
from flask import Flask, redirect, render_template, request, url_for
from fpdf import FPDF

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # Get the text input from the form
        text_input = request.form['text_input']
        
        # Generate a PDF file with the input text
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=text_input, ln=1)
        pdf.output("static/output.pdf")
        
        # Return a response to the user with a link to download the PDF file
        return f'<a href="/download">Download PDF</a>'
        
    # If the request method is GET, show the form to the user
    return render_template('index.html')

@app.route('/download')
def download():
    # Return the PDF file to the user for download
    return app.send_static_file('output.pdf')
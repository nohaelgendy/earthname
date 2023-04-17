import os
from flask import Flask, redirect, render_template, request, url_for
from fpdf import FPDF
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # Get the text input from the form
        name = request.form['text_input']
        if not name: name = "Muhammed"

        title = 'Earth & '+ name

        #
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name),
            max_tokens=1000,
            n=1,
            stream=False,
            stop=None,
            temperature=0.5,)

        result=response.choices[0].text
        
        # Generate a PDF file with the input text
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=20, style="B")
        pdf.cell(0, 10, title, ln=1, align="C")

        pdf.set_font("Arial", size=14)
        pdf.multi_cell(0, 10, result, 0, 'L')
        print(result)
        # Add an image to the PDF
        pdf.image('static/img/earth.jpeg', x=10, y=140, w=200)
        
        pdf.output("static/earth.pdf")
        
        # Return a response to the user with a link to download the PDF file
        return f'<a href="/download">Download PDF</a>'
        
    # If the request method is GET, show the form to the user
    return render_template('index.html')

@app.route('/download')
def download():
    # Return the PDF file to the user for download
    return app.send_static_file('earth.pdf')

def generate_prompt(name):
    return """generate story in two paragraph about planet 
    earth and how to save  earth suitable to kids by character
    input kid name :{} """.format(name.capitalize())
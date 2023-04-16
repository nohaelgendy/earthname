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
        text_input = request.form['text_input']

        #
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(),
            temperature=0.6,
        )
        result=response.choices[0].text
        print("response: -----> ",response)
        print("result: -----> ",result)
        
        # Generate a PDF file with the input text
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=text_input, ln=1)

        # Add an image to the PDF
        pdf.image('static/img/earth.jpeg', x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=150, h=150)
        pdf.cell(40, 10, result)
    
        pdf.output("static/output.pdf")
        
        # Return a response to the user with a link to download the PDF file
        return f'<a href="/download">Download PDF</a>'
        
    # If the request method is GET, show the form to the user
    return render_template('index.html')

@app.route('/download')
def download():
    # Return the PDF file to the user for download
    return app.send_static_file('output.pdf')

def generate_prompt():
    return """Can you provide fun and educational facts in 10 words
     about planet Earth that would be suitable for kids to learn?
    The information should be easy to understand and engaging,
    and cover topics such as the planet's size, environment,
    and unique features. Please also include any interesting
    facts about Earth's place in the solar system and the 
    importance of taking care of our planet."""
import os
from flask import Flask, redirect, render_template, request, url_for
from fpdf import FPDF
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['text_input']
        title = f'"Earth & {name}"'
        result = generate_story(name)
        pdf = create_pdf(title, result)
        pdf.output("static/earth.pdf")
        
        return app.send_static_file("earth.pdf")
    
    return render_template("index.html")

# @app.route("/download")
# def download():
#     return app.send_static_file("earth.pdf")

def generate_story(name):
    prompt = f"""generate story in two paragraph about planet earth and how to save earth 
                suitable to kids by character input kid name: {name.capitalize()} and suggest which job in the field of environment he/she can work """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=125,
        n=1,
        stream=False,
        stop=None,
        temperature=1,
    )
    return response.choices[0].text

def create_pdf(title, result):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=20, style="B")
    pdf.cell(0, 10, title, ln=1, align="C")

    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 10, result, 0, "L")

    pdf.image("static/img/earth.jpeg", x=10, y=140, w=200)

    pdf.set_y(pdf.h-35)
    pdf.set_font("Arial", size=8)
    pdf.cell(0, 10, "earthname.com", 0, 0, "C")

    return pdf

import os
from flask import Flask, redirect, render_template, request, url_for, send_file
from fpdf import FPDF
import openai
import io 
import tempfile

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['text_input'].capitalize()
        title = f'"Earth & {name}"'
        file_name = f'{name}.pdf'
        result = generate_story(name)
        pdf = create_pdf(title, result)
        # Because Vercel is read only. we have to change this logic of pdf write/read
        # pdf.output("static/earth.pdf")
        # return app.send_static_file("earth.pdf")

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_file = os.path.join(tmp_dir, file_name)
            pdf.output(tmp_file)
            return send_file(tmp_file, attachment_filename=file_name, as_attachment=True)
    
    return render_template("index.html")

def generate_story(name):
    prompt = f"""generate story in two paragraph about planet earth and how to save earth 
                suitable to kids by character input kid name: {name.capitalize()} """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=125,
        n=1,
        stream=False,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

def create_pdf(title, result):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=20, style="B")
    pdf.cell(0, 0, title, ln=1, align="C")

    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 8, result, 0, "L")

    pdf.image("static/img/earth.jpeg", x=10, y=140, w=200)

    pdf.set_y(pdf.h-35)
    pdf.set_font("Arial", size=8)
    pdf.cell(0, 10, "earthname.com", 0, 0, "C")

    return pdf

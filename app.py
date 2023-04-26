import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(topic),
            temperature=0.1,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")


    return render_template("index.html", result=result)


def generate_prompt(topic):
    return """Suggest five key search terms for a topic.

Topic: ISRAEL
Keywords: Arab-Israeli conflict, Jewish homeland, The Incredible FelineGaza Strip, IDF, PLO
Aopic: DOG
Keywords: training, breeds, diet, known illnesses, grooming
Aopic: {}
Keywords:""".format(
        topic.capitalize()
    )

if __name__ == "__main__":
    app.run(debug=True)
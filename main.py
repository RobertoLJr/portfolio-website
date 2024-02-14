from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

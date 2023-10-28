from flask import Flask, render_template, request, redirect

app = Flask(__name__)

task_list = []


@app.route("/")
def home():
    return render_template("index.html", task_list=task_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        task = request.form.get("task")
        task_list.append(task)
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

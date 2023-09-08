from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./public/tinnydev.html')

@app.route('/main')
def main():
    return render_template('./public/main.html', condition=condition_variable)


if __name__ == '__main__':
    app.run(debug=True)

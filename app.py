from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    name = "MrTG-CodeBot"
    server = "Flask"
    return render_template('about.html', user_name=name, server=server)

if __name__ == '__main__':
    app.run(debug=True)

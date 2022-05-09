from flask import Flask, render_template

# intialize Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('admin.html')


if __name__ == '__main__':

    # to run the flask app in the debug mode (app will start automatically)
    app.run(debug=True)

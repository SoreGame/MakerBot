from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    global FirstGet
    global LastGet
    FirstGet = request.GET['username']
    LastGet = request.GET['username']

if __name__ == "__main__":
    app.run()



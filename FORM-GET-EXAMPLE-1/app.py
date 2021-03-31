from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    if request.args:

        # request.args: the key/value pairs in the URL query string
        # print(request.args['firstname'])
        # print(request.args['lastname'])

        lst = {
            'first_name': request.args['firstname'],
            'last_name': request.args['lastname']
        }

        return render_template('index.html', list=lst)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)

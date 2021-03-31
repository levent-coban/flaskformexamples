from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # The form data is available in request.form dictionary. Stripping it to remove leading and trailing whitespaces
        firstname = request.form['firstname'].strip()
        lastname = request.form['lastname'].strip()
        print(firstname)
        print(lastname)
        print(request.form.to_dict())

    return render_template('index.html')


''' Print the all form data to the console
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')  
            # firstname: A  
            # lastname: B
            
        print(request.form.to_dict())  
        # {'firstname': 'a', 'lastname': 'b'}

    return render_template('index.html')
'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)


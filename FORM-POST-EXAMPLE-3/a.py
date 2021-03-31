from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        # The form data is available in 'request.form dictionary'.
        # Stripping it to remove leading and trailing whitespaces
        firstname = request.form.get('firstname', None).strip()
        lastname = request.form.get('lastname', None).strip()
        # firstname = request.form['firstname'].strip()
        # lastname = request.form['lastname'].strip()

        # Check if all the fields are non-empty and raise an error otherwise
        if not firstname or not lastname:  # or not gender or not username or not password:
            print('Please enter all the fields.')
        else:
            print(firstname)
            print(lastname)
            print(request.form.to_dict())
            
            # Print the form data to the console
            for key, value in request.form.items():
                print(f'{key}: {value}')
                # firstname: A
                # lastname: B

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)


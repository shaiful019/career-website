from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'AI Engineer',
        'location': 'Remote',
        'salary': '60,000 BDT'
    },
    {
        'id': 2,
        'title': 'Full-stack Developer',
        'location': 'Remote',
        'salary': '60,000 BDT'
    },
    {
        'id': 3,
        'title': 'Junior Machine Learning Engineer',
        'location': 'Dhaka, Bangladesh',
        'salary': '25,000 BDT'
    },
    
    {
        'id': 4,
        'title': 'Data Annotator',
        'location': 'Remote',
        'salary': '20,000 BDT'
    }
    
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = jobs)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from csv import reader

app = Flask(__name__)


@app.route('/')
def home():
    with open('personalwebsite.csv', newline='', encoding="ISO-8859-1") as csv_file:
        csv_data = reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('index.html', projects=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

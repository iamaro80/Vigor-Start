from flask import Flask, render_template, request, redirect
from vsearch import search4letters
import os

app = Flask(__name__)


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/')
def start() ->'html':
    return render_template('start.html')
    

@app.route('/entry')
def entry_page() ->'html':
    title = 'Welcome to search4letters on the web!'
    return render_template(
        'entry.html', 
        the_title=title)


@app.route('/search4', methods=['POST'])
def do_search() ->'html':
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template(
        'results.html',
        the_title=title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results)


def log_request(req: 'flask_request', res: str) -> None:
    os.chdir('D:/GitHub/vigor-start/01_Head_First/HF_Project/webapp/log')
    with open('vsearch.log', 'a') as log:
        print(req,, res, file=log)


# units = {'kg', 'liter', 'box', 'packet', 'unit', }
# units = set()
# for x in range(1980, 2019, 1):
#     units.add(x)
# print(units)

# @app.route('/list')
# def load_list_items() ->'html':
#     title = 'En Units list'
#     return render_template(
#           'list.html',
#           the_title=title,
#           the_units=sorted(units))

if __name__ == '__main__':
    app.run(debug=True)

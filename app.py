from flask import Flask, render_template, url_for, request, redirect, make_response
from werkzeug.utils import redirect
import sql as SQL

app = Flask(__name__)

@app.route("/")
def login():
    url_for('static', filename='login.js')
    url_for('static', filename='login.css')
    return render_template('login.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        userInfo = SQL.query('SELECT * FROM users WHERE username = \'' + username + '\' OR email = \'' + email + '\'')
        if (len(userInfo) > 0):
            return render_template('register.html', errorMessage = 'Username taken or email already registered.')
        else:
            SQL.insert('INSERT INTO users (username, pw, email) VALUES (\'' + username + '\', \'' + password + '\', \'' + email + '\')')
            resp = make_response(redirect('/homepage'))
            resp.set_cookie('signedIn', 'true')
            return resp
    else:
        url_for('static', filename='register.js')
        url_for('static', filename='register.css')
        return render_template('register.html')

@app.route("/signIn", methods=['POST', 'GET'])
def signIn():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        userInfo = SQL.query('SELECT * FROM users WHERE username = \'' + username + '\' AND pw = \'' + password + '\'')
        if (len(userInfo) > 0):
            resp = make_response(redirect('/homepage'))
            resp.set_cookie('signedIn', 'true')
            return resp
        else:
            return render_template('signIn.html', errorMessage = 'Username or password incorrect')
    else:
        url_for('static', filename='signIn.js')
        url_for('static', filename='signIn.css')
        return render_template('signIn.html')

@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        resp = make_response(redirect('/'))
        resp.set_cookie('signedIn', 'false')
        return resp

@app.route("/homepage")
def homepage():
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true': 
        url_for('static', filename='homepage.js')
        url_for('static', filename='homepage.css')
        return render_template('homepage.html')
    else:
        return redirect('/')

@app.route("/sample")
def sample():
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true':
        url_for('static', filename='sample.js')
        url_for('static', filename='sample.css')

        data = SQL.query('SELECT TOP(10) * FROM households INNER JOIN transactions ON households.HSHD_NUM = transactions.HSHD_NUM INNER JOIN products ON transactions.PRODUCT_NUM = products.PRODUCT_NUM WHERE households.HSHD_NUM = 10')
        for m in range(len(data)):
                for n in range(len(data[m])):
                    if isinstance(data[m][n], str):
                        data[m][n] = data[m][n].strip()

        finalData = []
        for i in range(10):
            finalRow = []

            finalRow.append(data[i][0])
            finalRow.append(data[i][9])
            finalRow.append(data[i][11])
            finalRow.append(data[i][12])
            finalRow.append(data[i][19])
            finalRow.append(data[i][20])
            finalRow.append(data[i][13])
            finalRow.append(data[i][14])
            finalRow.append(data[i][15])
            finalRow.append(data[i][16])
            finalRow.append(data[i][17])
            finalRow.append(data[i][1])
            finalRow.append(data[i][2])
            finalRow.append(data[i][3])
            finalRow.append(data[i][4])
            finalRow.append(data[i][5])
            finalRow.append(data[i][6])
            finalRow.append(data[i][7])
            finalRow.append(data[i][8])

            finalData.append(finalRow)

        return render_template('sample.html', data=finalData)
    else:
        return redirect('/')

@app.route("/search")
def search():
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true':
        url_for('static', filename='search.js')
        url_for('static', filename='search.css')
        return render_template('search.html')
    else:
        return redirect('/')

@app.route("/results/<int:HSHD_NUM>/<SORT>/<SORT_VALUE>")
def searchResults(HSHD_NUM, SORT, SORT_VALUE):
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true':
        url_for('static', filename='results.js')
        url_for('static', filename='results.css')

        SORT_VALUE = SORT_VALUE.upper()

        finalData = []
        counter = 0
        if (SORT != 'COMMODITY' and SORT != 'DEPARTMENT'):
            if SORT == 'DATE':
                data = SQL.query('SELECT * FROM households INNER JOIN transactions ON households.HSHD_NUM = transactions.HSHD_NUM INNER JOIN products ON transactions.PRODUCT_NUM = products.PRODUCT_NUM WHERE households.HSHD_NUM = ' + str(HSHD_NUM) + ' AND transactions.PURCHASE_DATE = \'' + str(SORT_VALUE) + '\'')
            else:
                data = SQL.query('SELECT * FROM households INNER JOIN transactions ON households.HSHD_NUM = transactions.HSHD_NUM INNER JOIN products ON transactions.PRODUCT_NUM = products.PRODUCT_NUM WHERE households.HSHD_NUM = ' + str(HSHD_NUM) + ' AND transactions.' + SORT + ' = ' + str(SORT_VALUE))

            for m in range(len(data)):
                for n in range(len(data[m])):
                    if isinstance(data[m][n], str):
                        data[m][n] = data[m][n].strip()
            while (len(finalData) < 25 and counter < len(data)):
                finalRow = []

                finalRow.append(data[counter][0])
                finalRow.append(data[counter][9])
                finalRow.append(data[counter][11])
                finalRow.append(data[counter][12])
                finalRow.append(data[counter][19])
                finalRow.append(data[counter][20])
                finalRow.append(data[counter][13])
                finalRow.append(data[counter][14])
                finalRow.append(data[counter][15])
                finalRow.append(data[counter][16])
                finalRow.append(data[counter][17])
                finalRow.append(data[counter][1])
                finalRow.append(data[counter][2])
                finalRow.append(data[counter][3])
                finalRow.append(data[counter][4])
                finalRow.append(data[counter][5])
                finalRow.append(data[counter][6])
                finalRow.append(data[counter][7])
                finalRow.append(data[counter][8])

                finalData.append(finalRow)
                counter += 1
        else:
            data = SQL.query('SELECT * FROM households INNER JOIN transactions ON households.HSHD_NUM = transactions.HSHD_NUM INNER JOIN products ON transactions.PRODUCT_NUM = products.PRODUCT_NUM WHERE households.HSHD_NUM = ' + str(HSHD_NUM) + ' AND products.' + SORT + ' = \'' + SORT_VALUE + '\'')
            for m in range(len(data)):
                    for n in range(len(data[m])):
                        if isinstance(data[m][n], str):
                            data[m][n] = data[m][n].strip()
            while(len(finalData) < 25 and counter < len(data)):            
                finalRow = []

                finalRow.append(data[counter][0])
                finalRow.append(data[counter][9])
                finalRow.append(data[counter][11])
                finalRow.append(data[counter][12])
                finalRow.append(data[counter][19])
                finalRow.append(data[counter][20])
                finalRow.append(data[counter][13])
                finalRow.append(data[counter][14])
                finalRow.append(data[counter][15])
                finalRow.append(data[counter][16])
                finalRow.append(data[counter][17])
                finalRow.append(data[counter][1])
                finalRow.append(data[counter][2])
                finalRow.append(data[counter][3])
                finalRow.append(data[counter][4])
                finalRow.append(data[counter][5])
                finalRow.append(data[counter][6])
                finalRow.append(data[counter][7])
                finalRow.append(data[counter][8])

                finalData.append(finalRow)
                counter += 1

        return render_template('results.html', data=finalData)
    else:
        return redirect('/')
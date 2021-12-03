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

@app.route('/question1')
def question1():
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true':
        url_for('static', filename='question1.js')
        url_for('static', filename='question1.css')

        sum2018 = SQL.query('SELECT SUM(transactions.SPEND) FROM transactions WHERE transactions.YEAR = 2018')
        sum2018 = str(sum2018[0][0])
        sum2018 = sum2018.split('.')[0] + '.' + sum2018.split('.')[0][:2]

        sum2019 = SQL.query('SELECT SUM(transactions.SPEND) FROM transactions WHERE transactions.YEAR = 2019')
        sum2019 = str(sum2019[0][0])
        sum2019 = sum2019.split('.')[0] + '.' + sum2019.split('.')[0][:2]

        sum2020 = SQL.query('SELECT SUM(transactions.SPEND) FROM transactions WHERE transactions.YEAR = 2020')
        sum2020 = str(sum2020[0][0])
        sum2020 = sum2020.split('.')[0] + '.' + sum2020.split('.')[0][:2]

        return render_template('question1.html', sum2018=sum2018, sum2019=sum2019, sum2020=sum2020)
    else:
        return redirect('/')

@app.route('/question2')
def question2():
    signedIn = request.cookies.get('signedIn')
    if signedIn == 'true':
        url_for('static', filename='question2.js')
        url_for('static', filename='question2.css')
        
#       GRAPH 1
        singleL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.MARITAL = \'Single\'')
        singleL = int(singleL[0][0])
        
        marriedL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.MARITAL = \'Married\'')
        marriedL = int(marriedL[0][0])
        
        maritalComp = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE NOT households.MARITAL = \'null\'')
        maritalComp = int(maritalComp[0][0])
        
#       GRAPH 2
        oneL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'1 Adult\'')
        oneL = int(oneL[0][0])
        
        twoL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'2 Adults\'')
        twoL = int(twoL[0][0])
        
        maleL =  SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'Single Male\'')
        maleL = int(maleL[0][0])
        
        femaleL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'Single Female\'')
        femaleL = int(femaleL[0][0])
        
        oneL = oneL + maleL + femaleL

        skidL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'1 Adult and Kids\'')
        skidL = int(skidL[0][0])

        mkidL = SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE households.HSHD_COMPOSITION = \'2 Adults and Kids\'')
        mkidL = int(mkidL[0][0])

        householdComp =  SQL.query('SELECT COUNT(CASE WHEN households.L = \'Y\' THEN 1 ELSE null END) FROM households WHERE NOT households.HSHD_COMPOSITION = \'null\'')
        householdComp = int(householdComp[0][0])

        return render_template('question2.html', singleL=singleL, marriedL=marriedL, maritalComp=maritalComp, oneL=oneL, twoL=twoL, skidsL=skidL, mkidsL=mkidL, householdComp=householdComp)
    else:
        return redirect('/')

from flask import Flask, render_template, url_for
import sql as SQL

app = Flask(__name__)

@app.route("/")
def homepage():
    url_for('static', filename='index.js')
    url_for('static', filename='index.css')
    return render_template('index.html')

@app.route("/sample")
def sample():
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

@app.route("/search")
def search():
    url_for('static', filename='search.js')
    url_for('static', filename='search.css')
    return render_template('search.html')

@app.route("/results/<int:HSHD_NUM>/<SORT>/<SORT_VALUE>")
def searchResults(HSHD_NUM, SORT, SORT_VALUE):
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
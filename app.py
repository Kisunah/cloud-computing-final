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

    # This sample query needs to be reworked like the user search queries below
    householdData = SQL.query('SELECT * FROM households WHERE HSHD_NUM = 10')
    for i in range(len(householdData)):
        for j in range(len(householdData[i])):
            if isinstance(householdData[i][j], str):
                householdData[i][j] = householdData[i][j].strip()

    transactionData = SQL.query('SELECT * FROM transactions WHERE HSHD_NUM = 10')
    for i in range(len(transactionData)):
        for j in range(len(transactionData[i])):
            if isinstance(transactionData[i][j], str):
                transactionData[i][j] = transactionData[i][j].strip()

    finalData = []
    for i in range(10):
        finalRow = []
        finalRow.append(householdData[0][0])
        finalRow.append(transactionData[i][0])
        finalRow.append(transactionData[i][2])
        finalRow.append(transactionData[i][3])
        productData = SQL.query('SELECT * FROM products WHERE PRODUCT_NUM = ' + str(transactionData[i][3]))
        for m in range(len(productData)):
            for n in range(len(productData[m])):
                if isinstance(productData[m][n], str):
                    productData[m][n] = productData[m][n].strip()

        finalRow.append(productData[0][1])
        finalRow.append(productData[0][2])
        finalRow.append(transactionData[i][4])
        finalRow.append(transactionData[i][5])
        finalRow.append(transactionData[i][6])
        finalRow.append(transactionData[i][7])
        finalRow.append(transactionData[i][8])
        finalRow.append(householdData[0][1])
        finalRow.append(householdData[0][2])
        finalRow.append(householdData[0][3])
        finalRow.append(householdData[0][4])
        finalRow.append(householdData[0][5])
        finalRow.append(householdData[0][6])
        finalRow.append(householdData[0][7])
        finalRow.append(householdData[0][8])
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
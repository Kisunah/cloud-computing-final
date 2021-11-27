from flask import Flask, render_template, url_for
import sql as SQL

app = Flask(__name__)

@app.route("/")
def homepage():
    url_for('static', filename='index.js')
    return render_template('index.html')

@app.route("/sample")
def sample():
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
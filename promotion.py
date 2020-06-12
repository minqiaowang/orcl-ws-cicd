"""
Simple Python application to show CI/CD capabilities.
"""

from bottle import Bottle, run
import cx_Oracle

app = Bottle()


@app.route('/addition/<salary>/<amount>')
def addition(salary, amount):
    return str(int(salary) + int(amount))


@app.route('/increment/<salary>/<percentage>')
def increment(salary, percentage):
    return str(int(salary) * (1 + int(percentage)/100))


@app.route('/decrease/<salary>/<amount>')
def decrease(salary, amount):
    return str(int(salary) - int(amount))


@app.route('/conn')
def conn():
    return str(connection.version)


if __name__ == '__main__':
    DBUSER = 'hr'
    DBPASS = 'WelCom3#2020_'
    DBSERV = 'VLTDB_TP'
    conn_string = DBUSER + '/' + DBPASS + '@' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    run(app, host='0.0.0.0', port=8080)
    connection.close()

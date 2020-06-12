"""
Simple Python application to show CI/CD capabilities.
"""

from bottle import Bottle, run
import cx_Oracle
import os

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


@app.route('/employees')
def emp():
    sql = '''select FIRST_NAME, LAST_NAME, SALARY, COMMISSION_PCT,
                    SALARY * (1 + nvl(COMMISSION_PCT,0)) as "Total"
             from EMPLOYEES order by 1,2'''
    employees = '''<table border=1><tr><td>First Name</td><td>Last Name</td>
                   <td>Salary</td><td>Commission</td><td>Total</td></tr>'''
    cursor = connection.cursor()
    for res in cursor.execute(sql):
        employees += '<tr><td>' + res[0] + '</td><td>' + res[1] + '</td><td>'
        employees += str(res[2]) + '</td><td>' + str(res[3]) + '</td><td>'
        employees += str(res[4]) + '</td></tr>'
    employees += '</table>'
    return str(employees)


@app.route('/salary_increase/<percentage>')
def sal_inc(percentage):
    sql = '''select FIRST_NAME, LAST_NAME, SALARY, COMMISSION_PCT,
                    SALARY * (1 + nvl(COMMISSION_PCT,0)) as "Total",
                    SALARY * (1 + ''' + percentage + '''/100) as "New Salary",
                    SALARY * (1 + ''' + percentage + '''/100) * (1 + nvl(COMMISSION_PCT,0)) as "New Total"
             from EMPLOYEES order by 1,2'''
    employees = '''<table border=1><tr><td>First Name</td><td>Last Name</td>
                   <td>Salary</td><td>Commission</td><td>Total</td>
                   <td>New Salary</td><td>New Total</td></tr>'''
    cursor = connection.cursor()
    for res in cursor.execute(sql):
        employees += '<tr><td>' + res[0] + '</td><td>' + res[1]
        employees += '</td><td>' + str(res[2]) + '</td><td>' + str(res[3])
        employees += '</td><td>' + str(res[4]) + '</td><td>' + str(res[5])
        employees += '</td><td>' + str(res[6]) + '</td></tr>'
    employees += '</table>'
    return str(employees)


@app.route('/add_commission/<value>')
def add_commp(value):
    sql = '''select FIRST_NAME, LAST_NAME, SALARY, COMMISSION_PCT,
                    SALARY * (1 + nvl(COMMISSION_PCT,0)) as "Total",
                    nvl(COMMISSION_PCT,0) + ''' + value + ''' as "New Commission",
                    SALARY * (1 + nvl(COMMISSION_PCT,0) + ''' + value + ''') as "New Total"
             from EMPLOYEES order by 1,2'''
    employees = '''<table border=1><tr><td>First Name</td><td>Last Name</td>
                   <td>Salary</td><td>Commission</td><td>Total</td>
                   <td>New Commission</td><td>New Total</td></tr>'''
    cursor = connection.cursor()
    for res in cursor.execute(sql):
        employees += '<tr><td>' + res[0] + '</td><td>' + res[1]
        employees += '</td><td>' + str(res[2]) + '</td><td>' + str(res[3])
        employees += '</td><td>' + str(res[4]) + '</td><td>' + str(res[5])
        employees += '</td><td>' + str(res[6]) + '</td></tr>'
    employees += '</table>'
    return str(employees)


if __name__ == '__main__':
    DBUSER = os.getenv('DB_USER')
    DBPASS = os.getenv('DB_PASSWORD')
    DBSERV = os.getenv('DB_SERVICE')
    conn_string = DBUSER + '/' + DBPASS + '@' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    run(app, host='0.0.0.0', port=8080)
    connection.close()

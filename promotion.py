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


if __name__ == '__main__':
    DBUSER = 'hr'
    DBPASS = 'WelCom3#2020_'
    DBSERV = 'VLTDB_TP'
    conn_string = DBUSER + '/' + DBPASS + '@' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    run(app, host='0.0.0.0', port=8080)
    connection.close()

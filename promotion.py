"""
Simple Python application to show CI/CD capabilities.
"""

from bottle import Bottle, run

app = Bottle()


@app.route('/addition/<salary>/<amount>')
def addition(salary, amount):
    return salary + amount


@app.route('/increment/<salary>/<percentage>')
def increment(salary, percentage):
    return salary * (1 + percentage/100)


@app.route('/decrease/<salary>/<amount>')
def decrease(salary, amount):
    return salary - amount


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080)

from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
# here in above i can any name or any things
def calculator_page():
    return render_template('index_cal.html')

@app.route("/math",methods = ['POST'])
def calculator_test():
    ops = request.form['operation']
    first_nums = int(request.form['num1'])
    second_nums = int(request.form['num2'])

    if (ops == 'add'):
        r = first_nums + second_nums
        return f"Addition of {first_nums} and {second_nums} is: {r} "
    if (ops == 'subtract'):
        r = first_nums - second_nums
        return f"Substraction of {first_nums} and {second_nums} is: {r} "
    if (ops == 'multiply'):
        r = first_nums * second_nums
        return f"Multipication of {first_nums} and {second_nums} is: {r} "
    if (ops == 'divide'):
        r = first_nums / second_nums
        return f"Division of {first_nums} and {second_nums} is: {r} "
   


    
if __name__ == '__main__':
    app.run(host ='0.0.0.0',port = 5002)

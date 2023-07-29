from flask import Flask,request,render_template

obj=Flask(__name__)


@obj.route('/')
def welcome():
    return "Welcome to Flask"

@obj.route('/cal',methods=["GET"])
def math_operators():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*int(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return "The operation is {} and the result is {}".format(operation,result)




@obj.route('/calculator',methods=["GET","POST"])
def math_operator():
    if request.method == 'GET':
        return render_template('calculator.html')
    else:
        operation=request.form["operation"]
        number1=int(request.form["number1"])
        number2=int(request.form["number2"])
        
        if operation=="add":
            result=number1+number2
        elif operation=="multiply":
            result=number1*number2
        elif operation=="division":
            result=number1/number2
        else:
            result=number1-number2
        return "The operation is {} and the result is {}".format(operation,result)
        
    


print(__name__)

if __name__ == '__main__':
    obj.run(debug=True)
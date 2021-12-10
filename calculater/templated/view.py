from flask import *  
app = Flask(__name__)  
  
  
@app.route('/view') 
 
def cal():  
    
    num1=request.args.get('num1')  
    num2=request.args.get('num2')
    if request.args.get('Add'):
        return num1+num2
    elif request.args.get('sub'):
        return num1-num2

   
if __name__ == '__main__':  
   app.run(debug = True)  
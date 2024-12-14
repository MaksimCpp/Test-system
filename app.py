from flask import *
import subprocess
import sys

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])
def test():
    answer = 108
    code = None
    response = None
    result_code = None
    result = ""

    
    if request.method == 'POST':
        try:
            out = sys.stdout
            code = request.form['code']
            response = subprocess.run(['python', '-c', code], capture_output=True)
            result_code = response.stdout.decode()

            if int(result_code) == answer:
                result = "Ответ верный"
            elif int(result_code) != answer:
                result = "Ответ неверный"
   
        except Exception as e:
            response = subprocess.run(['python', '-c', code], capture_output=True)
            result = response.stderr.decode()
    

    return render_template('index.html', result=result)
   

if __name__ == '__main__':
    app.run(debug=True)

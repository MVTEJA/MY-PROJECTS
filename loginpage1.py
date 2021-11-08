from flask import Flask, render_template , request
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '*******' , database = 'flaskapp')
app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        # so to store user data
        userdetails = request.form
        name = userdetails['email']
        email = userdetails['password']
        cur = mydb.cursor()
        k = ('INSERT INTO users(name , email) VALUES(%s , %s)')
        l = (name , email)
        cur.execute(k ,l)
        mydb.commit()
        cur.close()
        return 'success'
    return render_template('bootindex.html')

if __name__ == '__main__':
    app.run(debug = True)

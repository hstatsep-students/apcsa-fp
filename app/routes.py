from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/unit1')
def unit1():
    return render_template('unit_1.html')
    
@app.route('/unit2')
def unit2():
    return render_template('unit_2.html')
    
@app.route('/unit3')
def unit3():
    return render_template('unit_3.html')
    
@app.route('/unit4')
def unit4():
    return render_template('unit_4.html')
    
@app.route('/unit5')
def unit5():
    return render_template('unit_5.html')
    
@app.route('/unit6')
def unit6():
    return render_template('unit_6.html')
    
@app.route('/unit7')
def unit7():
    return render_template('unit_7.html')
    
@app.route('/unit8')
def unit8():
    return render_template('unit_8.html')
    
@app.route('/unit9')
def unit9():
    return render_template('unit_9.html')
    
@app.route('/unit10')
def unit10():
    return render_template('unit_10.html')
    
    
    
#importamos las clases y metodos 
import datetime
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', "POST"])
def aritmetica():
    if request.method == "POST":
        # valores que recibo del form n1,n2 son pasados
        num1=float(request.form.get('n1'))
        num2=float(request.form.get('n2'))

        #realizamos operaciones aritmeticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_division=division ) 
    return render_template('index.html')
@app.route('/divisas', methods=['GET', "POST"])
def divisas():
    if request.method == "POST":
        #valores que recibo de divisas
        divisas=float(request.form.get('divisas'))
        
        #realizamos operaciones aritmeticas
        dolares= divisas / 4224,21
        euros= divisas / 46553,00
        pesosM= divisas /218,00
        return render_template('divisas.html', total_dolares= dolares,
                                                total_euros=euros,
                                                total_pesosM=pesosM)
    return render_template('divisas.html')
@app.route('/longitudes', methods=['GET', "POST"])
def longitudes():
    if request.method == "POST":
       #valores que recibo de longitudes
       longitudes=float(request.form.get('longitudes'))

       #realizamos operaciones aritmeticas
       centimetros= longitudes / 100
       kilometros= longitudes * 1000
       milimetros= longitudes* 1000  
       return render_template('longitudes.html', total_cen=centimetros,
                                                total_kil=kilometros,
                                                total_mil=milimetros)
    return render_template('longitudes.html')
if __name__ == "__main__":
    app.run(debug=True)
   

    



















































































































































































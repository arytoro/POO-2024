from datetime import datetime
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Sucursal, Paquete, Repartidor, Transporte

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/usuario_despachante',methods=['GET','POST'])
def usuario_despachante():
    return render_template('usuario_despachante.html', sucursales = Sucursal.query.order_by(Sucursal.numero.desc()).all()) #el order_by es para ordenarlo y el .desc() es para que sea descendiente

@app.route('/acciones_despachante/<sucuOpe>',methods=['GET','POST'])
def acciones_despachante(sucuOpe):
    return render_template('acciones_despachante.html',sucursal=sucuOpe)

@app.route('/registrar_paquete/<sucuOpe>', methods = ['GET','POST'])
def registrar_paquete(sucuOpe):
    if request.method == 'POST':
        if  not request.form['peso'] or not request.form['nombre'] or not request.form['direccion']:
            return render_template('error.html', error="Error. Por favor ingrese los datos requeridos")
        elif request.form['peso'].replace('.',"").replace(',',"").replace(' ','').isnumeric() is False:
            return render_template('error.html', error="Error. El peso del paquete solo debe contener numeros y/o separador decimal")
        elif request.form['nombre'].replace(' ','').isalpha() is False:
            return render_template('error.html', error="Error. El nombre del destinatario solo debe contener letras")
        else:
            with app.app_context():
                numeroEnvio_nuevoPaquete=Paquete.query.count()*20+1000
                #ultimoPaquete= Paquete.query.order_by(Paquete.numeroenvio.desc()).first()
                #numeroEnvio_nuevoPaquete= ultimoPaquete.numeroenvio+20

            nuevo_paquete = Paquete(numeroenvio=numeroEnvio_nuevoPaquete, peso = float(request.form['peso'].replace(',','.')), nomdestinatario= request.form['nombre'],dirdestinatario= request.form['direccion'],idsucursal=sucuOpe,entregado=False,idtransporte=0,idrepartidor=0)
            db.session.add(nuevo_paquete)
            db.session.commit()
            return render_template('aviso.html', mensaje="El paquete se registró exitosamente")
    else:
        return render_template('registrar_paquete.html',sucursales = Sucursal.query.order_by(Sucursal.numero.desc()).all())

@app.route('/salida_transporte/<sucuOpe>',methods = ['GET','POST'])
def salida_paquete(sucuOpe):
    if request.method=='POST':
        if request.form['sucursal_destino']=='':
            return render_template('error.html',error='ERROR. No seleccionó una sucursal destino')
        else:
            return redirect(url_for('paquetes_pendientes',sucu=request.form['sucursal_destino']))
    return render_template('salida_transporte.html',sucursales=Sucursal.query.all())

@app.route('/paquetes_pendientes/<sucu>',methods= {'GET','POST'})
def paquetes_pendientes(sucu):
    if request.method=='POST':
        lista_paquetes=request.form.getlist('paquetes_elegidos')
        print(lista_paquetes)
        if len(lista_paquetes)==0:
            return render_template('error.html',error='ERROR. Debe seleccionar al menos un paquete')
        else:
            for i in range(len(lista_paquetes)):
                with app.app_context():
                    ultimoTransporte= Transporte.query.order_by(Transporte.numerotransporte.desc()).first()
                    numeroTransporte_nuevoTransporte = ultimoTransporte.numerotransporte+1
                nuevo_transporte= Transporte(numerotransporte=numeroTransporte_nuevoTransporte, fechahorasalida = datetime.now(), idsucursal= sucu)
                db.session.add(nuevo_transporte)
                db.session.commit()
            return render_template('aviso.html', mensaje="El transporte se registró exitosamente")
    return render_template('paquetes_pendientes.html',paquetes=Paquete.query.filter(Paquete.entregado==False,Paquete.idrepartidor==0).all())

@app.route('/llegada_transporte/<sucuOpe>',methods= {'GET','POST'})
def llegada_transporte(sucuOpe):
    if request.method=='POST':
        if request.form['transporte_elegido']=='':
            return render_template('error.html',error= 'ERROR. Debe seleccionar un transporte')
        else:
            transporte_seleccionado=Transporte.query.filter_by(id=request.form['transporte_elegido']).first()
            transporte_seleccionado.fechahorallegada=datetime.now()
            db.session.commit()
            return render_template('aviso.html',mensaje="La llegada se registró exitosamente")
    return render_template('llegada_transporte.html',transportes=Transporte.query.filter(Transporte.fechahorallegada==None,Transporte.idsucursal==sucuOpe).all())

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
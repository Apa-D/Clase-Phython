from flask import Flask, request, render_template, redirect, flash
import time
import uuid

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

recordatorioList = []              ## lista
idActual = int(uuid.uuid4())       ## id UUID
CreateAt= int(time.time() * 1000)  ## Creado el 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Recordatorio")
def quienes_somos():
    return render_template("Recordatorios.html", recordatorio = recordatorioList)

@app.post("/crear-recordatorio")
def crear_recordatorio():
    global idActual
    datos = request.form
    texto = datos.get("texto")

    if texto is None or len(texto) < 1:
        flash("El texto del recordatorio debe tener caracteres", "warning")
        return redirect("/Recordatorio")               #salta correctamente
    
    nueva_redimers = nueva_redimers = { "id": idActual, "texto": texto, "CreateAt": CreateAt,"Importante": False }
    idActual += 1
    recordatorioList.append(nueva_redimers)            #no da error

    flash("Recordatorio creada exitosamente", "success") 
    return redirect("/Recordatorio")


@app.route('/borrar-recordatorio/<int:id>', methods=['POST'])
def borrar_recordatorio(id):
    global recordatorioList
    recordatorioList = [r for r in recordatorioList if r.id != id]
    flash("Recordatorio borrado exitosamente", "success")
    return redirect("/Recordatorio") 


@app.route('/editar-recordatorio/<int:id>', methods=['GET', 'POST'])
def editar_recordatorio(id):
    recordatorio = next((r for r in recordatorioList if r.id == id), None)
    if request.method == 'POST':
        nuevo_texto = request.form['texto']
        if recordatorio:
            recordatorio.texto = nuevo_texto
            flash("Recordatorio actualizado", "success")
        return redirect("/Recordatorio")
    return render_template('editar.html', recordatorio=recordatorio)

@app.route("/Recordatorio/<int:id>", methods=["PATCH"])
def actualizar_recordatorio(id):
    for redimers in recordatorioList:
        if redimers["id"] == id:
            redimers["Importante"] = not redimers["Importante"]
            return redimers
    return "Recordatorio no encontrada", 404


@app.route("/Recordatorio/<int:id>", methods=["DELETE"])
def borrar_Recordatorio(id):
    for index, redimers in enumerate(recordatorioList):
        if redimers["id"] == id:
            del recordatorioList[index]
            return '', 204
    return "Recordatorio no encontrada", 404

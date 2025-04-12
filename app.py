from flask import Flask, request, render_template, redirect, flash
import time
import uuid

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

recordatorioList = []              ## lista
idActual = int(uuid.uuid4())       ## id UUID
CreateAt= int(time.time() * 1000)  ## Creado el "dia-mes-año"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Recordatorio")
def quienes_somos():
    return render_template("Recordatorios.html", recordatorio = recordatorioList)

@app.post("/crear-recordatorio")
def crear_tarea():
    global idActual
    datos = request.form
    texto = datos.get("texto")

    if texto is None or len(texto) < 5:
        flash("El texto de la tarea debe tene como mínimo 5 caracteres", "warning")
        return redirect("/Recordatorio")
    
    nueva_tarea = nueva_tarea = { "id": idActual, "texto": texto, "CreateAt": CreateAt,"Importante": False }
    idActual += 1
    recordatorioList.append(nueva_tarea)

    flash("Recordatorio creada exitosamente", "success")
    return redirect("/Recordatorio")


@app.route("/api/Recordatorio/<int:id>", methods=["PATCH"])
def api_actualizar_tarea(id):
    for tarea in recordatorioList:
        if tarea["id"] == id:
            tarea["Importante"] = not tarea["Importante"]
            return tarea
    return "Recordatorio no encontrada", 404

@app.route("/api/Recordatorio/<int:id>", methods=["DELETE"])
def api_borrar_Recordatorio(id):
    for index, Recordatorio in enumerate(recordatorioList):
        if Recordatorio["id"] == id:
            del recordatorioList[index]
            return '', 204
    return "Recordatorio no encontrada", 404

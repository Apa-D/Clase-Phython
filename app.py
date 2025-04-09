from flask import Flask, request, render_template, redirect, flash
import time
import uuid

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

recordatorioList = [] ##lista
idActual = str(uuid.uuid4())
CreateAt= int(time.time() * 1000)  ##Creado el "dia-mes-año"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reminders")
def Cargar_reminders():
    return render_template("Recordatorios.html")

@app.post("/crear-tarea")
def crear_tarea():
    global idActual
    datos = request.form
    texto = datos.get("texto")

    if texto is None or len(texto) < 5:
        flash("El texto de la tarea debe tene como mínimo 5 caracteres", "warning")
        return redirect("/tareas")
    
    nueva_tarea = nueva_tarea = { "id": idActual, "texto": texto,"CreatAt":CreateAt, "completado": False }
    idActual += 1
    recordatorioList.append(nueva_tarea)

    flash("Tarea creada exitosamente", "success")
    return redirect("/tareas")


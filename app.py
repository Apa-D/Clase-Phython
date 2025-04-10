from flask import Flask, request, render_template, redirect, flash
import time
import uuid

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

recordatorioList = []              ## lista
idActual = str(uuid.uuid4())       ## id UUID
CreateAt= int(time.time() * 1000)  ## Creado el "dia-mes-año"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reminders")
def Cargar_reminders():
    return render_template("Recordatorios.html")

@app.post("/api/reminder")
def crear_reminders():
    global idActual
    datos = request.form
    texto = datos.get("texto")

    if texto is None or len(texto) < 5:
        flash("El texto del recordatorio debe tene como mínimo 5 caracteres", "warning")
        return redirect("Recordatorios.html")
    
    nueva_reminders = nueva_reminders = { "id": idActual, "texto": texto,"CreatAt":CreateAt, "completado": False }
    recordatorioList.append(nueva_reminders)

    flash("Recordatorio creada exitosamente", "success")
    return nueva_reminders, 201


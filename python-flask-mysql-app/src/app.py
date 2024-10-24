from flask import Flask, render_template
import os
print(os.getcwd())  # Para ver tu directorio de trabajo actual

template_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de aplicacion
@app.route('/')
def home():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True, port=4000)
    
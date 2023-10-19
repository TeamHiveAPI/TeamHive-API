from flask import Flask, render_template, url_for

app = Flask(
	__name__,
	template_folder="templates"
)

#Rota pagina inicial
@app.route('/')
def index():
    return render_template('index.html', nav='active')

#Rota pagina blog 
@app.route('/blog')
def blog():
    return render_template('blog.html', nav='active')

#Rota pagina dados 
@app.route('/dados')
def dados():
    return render_template('dados.html', nav='active')
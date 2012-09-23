# -*- encoding: utf-8 -*-
from flask import Flask, render_template, flash, request
from forms import ClienteForm
from flask.ext.mongoengine import MongoEngine
from mongoengine import NotUniqueError

app = Flask(__name__)

app.debug = True
app.config["MONGODB_DB"] = "cadcli"
app.config["SECRET_KEY"] = "FeDs03hisS3@%#34"

db = MongoEngine(app)

#=================================================================== MODELS

class Endereco(db.Document):
	cidade = db.StringField()
	estado = db.StringField()
	rua = db.StringField()

class Cliente(db.Document):
	nome = db.StringField()
	endereco = db.ReferenceField(Endereco, reverse_delete_rule=db.CASCADE)
	telefone_res = db.StringField()
	telefone_cel = db.StringField()
	telefone_com = db.StringField()
	email = db.EmailField(unique=True)
	data_nascimento = db.DateTimeField()
	ativo = db.BooleanField()

#=================================================================== VIEWS

@app.route("/")
def home():
    clientes = Cliente.objects.all()
    return render_template('index.html', clientes=clientes)

@app.route("/cadastro/")
def cadastro():
	form = ClienteForm()
	return render_template('cadastro.html', form=form, active='cad')

@app.route("/delete/<cliente_id>/")
def delete(cliente_id):
	cliente = Cliente.objects.get(id=cliente_id)
	cliente.

@app.route("/salvar", methods=['POST'])
def salvar():
	form = ClienteForm(request.form)
	if form.validate():
		obj = Cliente()
		obj.nome = form.nome.data
		endereco = Endereco()
		endereco.cidade = form.endereco.data['cidade']
		endereco.estado = form.endereco.data['estado']
		endereco.rua = form.endereco.data['rua']
		endereco.save()
		obj.endereco = endereco
		obj.telefone_res = form.telefone_res.data
		obj.telefone_com = form.telefone_com.data
		obj.telefone_cel = form.telefone_cel.data
		obj.email = form.email.data
		obj.ativo = form.ativo.data
		obj.data_nascimento = form.data_nascimento.data
		try:
			obj.save()
		except NotUniqueError:
			flash(u'Já existe um cliente com este email cadastrado.')
		else:
			flash(u"Novo cliente salvo com sucesso!")
	else:
		flash(u"Algum dado está incorreto. Corrija e repita a operação.")
	return render_template('cadastro.html', form=form, active='cad')

if __name__ == "__main__":
    app.run()
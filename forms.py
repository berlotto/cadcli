# -*- encoding: utf-8 -*-
from wtforms import Form, BooleanField, TextField, PasswordField, DateField, SelectField, FormField, FloatField, FieldList

class EnderecoForm(Form):
    cidade = TextField('Cidade')
    estado = SelectField('Estado', choices=[('ac','AC'),
('al','AL'),
('ap','AP'),
('am','AM'),
('ba','BA'),
('ce','CE'),
('df','DF'),
('es','ES'),
('go','GO'),
('ma','MA'),
('mt','MT'),
('ms','MS'),
('mg','MG'),
('pa','PA'),
('pb','PB'),
('pr','PR'),
('pe','PE'),
('pi','PI'),
('rj','RJ'),
('rn','RN'),
('rs','RS'),
('ro','RO'),
('rr','RR'),
('sc','SC'),
('sp','SP'),
('se','SE'),
('to','TO')])
    rua = TextField(u'Rua e Número')


class ClienteForm(Form):
    nome = TextField('Nome')
    endereco = FormField(EnderecoForm, u'Endereço')
    telefone_cel = TextField('Telefone Celular')
    telefone_res = TextField('Telefone Residencial')
    telefone_com = TextField('Telefone Comercial')
    email = TextField('Email')
    data_nascimento = DateField('Data de Nascimento', format='%d/%m/%Y', default=None)
    ativo = BooleanField('Cliente ativo')

class ProdutoForm(Form):
	nome = TextField('Nome do Produto')
	tipo = FieldList('Tipo', choices=[('perfume','Perfume'),('maquiagem','Maquiagem'),('outro','Outros')])
	valor_compra = FloatField('Valor de Compra')
	valor_venda = FloatField('Valor de Venda')
	valor_final = FloatField('Valor Final')


class VendaForm(Form):
	data_venda = DateField('Data da Venda')
	cliente = FormField(ClienteForm)
	produtos = FieldList(FormField(ProdutoForm))
	total = FloatField('Total da Venda')

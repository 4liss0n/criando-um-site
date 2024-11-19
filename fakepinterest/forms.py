from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError  

class FormLogin(FlaskForm):  
    email = StringField("E-mail", validators=[DataRequired(), Email()])  # Campo de email do usuário com validadores que exigem preenchimento e formato de email válido.
    senha = PasswordField("Senha", validators=[DataRequired()])  # Campo de senha com validador que exige preenchimento.
    botao_confirmacao = SubmitField("Fazer Login")  # Botão de envio do formulário de login com o rótulo "Fazer Login".

class FormCriarConta(FlaskForm):  
    email = StringField("E-mail", validators=[DataRequired(), Email()])  # Campo de email com validadores que exigem preenchimento e verificam o formato do email.
    usarname = StringField("Nome de usuário", validators=[DataRequired()])  # Campo de nome de usuário com validador que exige preenchimento.
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])  # Campo de senha, com validadores que exigem preenchimento e limitam 
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])  # Campo de confirmação de senha, obrigatório e que 
    botao_confirmacao = SubmitField("Criar Conta")  # Botão de envio do formulário de criação de conta com o rótulo "Criar Conta".

    def validade_email(self, email):  
         from fakepinterest import Usuario
         usuario = Usuario.query.filter_by(email=email.data).first()  # Consulta no banco para verificar se o email já está cadastrado. O "email.data" acessa o valor do campo.
         if usuario:  # Se o email já estiver cadastrado, exibe uma mensagem de erro personalizada.
            return ValidationError("E-mail já cadastrado, faça login para continuar")




from django.shortcuts import render
from .forms import PacienteForm, PesquisaForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Paciente, Medico, Especialidade 
from io import BytesIO
from reportlab.pdfgen import canvas
from django.db import connection

# Create your views here.
# Convert tuple in dictionary
def dictfetchall(cursor):
	desc = cursor.description
	return [dict(zip([call[0] for call in desc],raw)) for raw in cursor.fetchall()]

def get_medico(especialidade):
	medico_filtro = connection.cursor()
	medico_filtro.execute(" select medico_nome from hospital_medico, hospital_especialidade   where medico_especialidade_id=hospital_especialidade.id and medico_especialidade_id =%d" %especialidade);
	return dictfetchall(medico_filtro)

def index(request):

	return render(request,'index.html',)

def home(request):
	especialidade_id=0
	if request.method =='POST':
		form = PacienteForm(request.POST)
		if form.is_valid():
			raw_especialidade = form.cleaned_data['especialidade']
			raw_medico = form.cleaned_data['medico']
			medico_nome = Medico.objects.get(medico_nome=raw_medico)
			especialidade_nome = Especialidade.objects.get(especialidade_nome=raw_especialidade)
			especialidade_id = int(especialidade_nome.id)
			paciente_nome = form.cleaned_data['nome']
			data_nascimento = form.cleaned_data['data_nascimento']
			sexo = form.cleaned_data['sexo']
			naturalidade = form.cleaned_data['naturalidade']
			estado_civil = form.cleaned_data['estado_civil']
			numero_bi = form.cleaned_data['numero_bi']
			data_de_emissao_bi = form.cleaned_data['data_de_emissao_bi']
			data_de_validade = form.cleaned_data['data_de_validade']
			data_da_consulta = form.cleaned_data['data_da_consulta']
			new_paciente, created = Paciente.objects.get_or_create(paciente_nome=paciente_nome, paciente_data_nascimento = data_nascimento, paciente_bilhete_identidade=numero_bi,
				paciente_bi_emissao = data_de_emissao_bi, paciente_bi_validade = data_de_validade, 
				paciente_data_consulta = data_da_consulta, paciente_sexo = sexo,
				paciente_especialidade=especialidade_nome, paciente_medico=medico_nome, paciente_naturalidade = naturalidade,
				paciente_estado_civil = estado_civil)
			return HttpResponseRedirect('/show-consultas/')
			
	else:
		form = PacienteForm()
	especialidade_lista = Especialidade.objects.order_by('especialidade_nome')
	#medico_lista = get_medico(especialidade_id)
	medico_lista =Medico.objects.order_by('medico_nome')
	template = 'home.html'
	return render(request, template, {'form':form, 'medico_lista':medico_lista, 'especialidade_lista':especialidade_lista})



def show_consultas(request):
	dados = Paciente.objects.last()
	template = 'show-consultas.html'
	return render(request, template,{'dados':dados})

#Query_Pesquisa


def get_consulta(nome,data):
    resultado_search = connection.cursor()
    resultado_search.execute("select paciente_nome, paciente_data_consulta, especialidade_nome, medico_nome from hospital_paciente, hospital_especialidade, hospital_medico where paciente_especialidade_id=hospital_especialidade.id and paciente_medico_id=hospital_medico.id and hospital_paciente.paciente_nome='%s' and paciente_data_consulta='%s'"%(nome,data));
    return dictfetchall(resultado_search)

def get_lista_pacientes():
    lista_todos = connection.cursor()
    lista_todos.execute("select paciente_nome, paciente_data_consulta, especialidade_nome, medico_nome from hospital_paciente, hospital_especialidade, hospital_medico where paciente_especialidade_id=hospital_especialidade.id and paciente_medico_id=hospital_medico.id order by paciente_nome");
    return dictfetchall(lista_todos)


def pesquisa(request):
	content=''
	mensagem = 'Resultados da Pesquisa:'
	msg ='Nao foram encontrados resultados!'
	nome = request.GET.get('nome')
	data = request.GET.get('data')
	if nome:
		resultado = get_consulta(nome, data)
		content = {'query': nome, 'resultado': resultado,'mensagem':mensagem}
		if resultado ==[]:
			content = {'msg':msg}
			
	template = 'pesquisa.html'
	return render(request,template,content)

def lista_pacientes(request):
	paciente = get_lista_pacientes()
	template = 'lista_pacientes.html'
	return render(request, template, {'paciente':paciente})


def some_view(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    other = Paciente.objects.last()
    nome = other.paciente_nome
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dados_marcacao.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100,800, "Dados da Marcacao")
    p.drawString(100,770,nome)


    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response




from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from .models import Proyecto,Usuario,UsuarioProyecto
from mysite import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
import csv
import datetime

def Proyectos(request):
	proyectos_disponibles = Proyecto.objects.order_by('-pub_date')
	context = {'proyectos_disponibles': proyectos_disponibles}
	return render(request, 'inscripciones/index.html', context)

def AddProyecto(request):
    if request.user.is_staff and request.method == "POST":
        nombre = request.POST['nombre']
        cupo = request.POST['cupo']
        descripcion = request.POST['descripcion']
        lugar = request.POST['lugar']
        horario = request.POST['horario']
        categoria = request.POST['categoria']
        url  = request.POST['url']
        
        proyecto = Proyecto(nombre=nombre, cupo=cupo, descripcion=descripcion,
            lugar=lugar,horario=horario,categoria=categoria,url=url)
        proyecto.save()
        return render_to_response('inscripciones/add_proyecto_exitoso.html', {'proyecto': proyecto}, RequestContext(request))

    return render_to_response('inscripciones/add_proyecto.html',  RequestContext(request))

def DeleteProyecto(request,proyecto_id):
    if request.user.is_staff :
        
        usuarioproy = UsuarioProyecto.objects.filter(proyecto__codigo = proyecto_id)
        for up in usuarioproy:
            up.delete()

        proyecto = Proyecto.objects.get(pk=proyecto_id)
        proyecto.delete()

        return render(request,'inscripciones/delete_proyecto.html')

    return HttpResponseRedirect('/proyectos/'+proyecto_id)

    
    



def Detail(request,proyecto_id):

    try:
        proyecto = Proyecto.objects.get(pk=proyecto_id)
    except Proyecto.DoesNotExist:
        raise Http404("No existe ese proyecto")
    if request.user.is_staff:
        up = UsuarioProyecto.objects.filter(proyecto__codigo = proyecto_id)
        return render(request,'inscripciones/detail.html',{'proyecto':proyecto,'up':up})
    return render(request, 'inscripciones/detail.html', {'proyecto': proyecto})

def DetailUsuario(request,m_id):
    if not request.user.is_authenticated():
        return render(request, 'inscripciones/login.html')
    else:
        try:
            usuarioBuscado = Usuario.objects.get(matricula=m_id)
        except User.DoesNotExist:
            raise Http404("No existe ese usuario")

        #if request.user.is_staff:
        return render(request,'inscripciones/usuario.html',{'usuario':usuarioBuscado})
        #elif request.user.id
            #return render(request,'inscripciones/login.html')

    return render(request,'inscripciones/login.html')

def DeleteUsuario(request,m_id):
    if request.user.is_staff :
        
        usuarioproy = UsuarioProyecto.objects.filter(usuario__matricula = m_id)
        for up in usuarioproy:
            up.delete()

        usuario = Usuario.objects.get(matricula=m_id)
        user = User.objects.get(username=m_id)

        usuario.delete()
        user.delete()

        return render(request,'inscripciones/delete_usuario.html')

    return HttpResponseRedirect('/usuario/'+m_id)

    
    


def ListaUsuarios(request):
    if not request.user.is_authenticated():
        return render(request, 'inscripciones/login.html')
    else:
        lista_usuarios = Usuario.objects.order_by('-first_name')
        if request.user.is_staff:
            return render(request,'inscripciones/lista_usuarios.html',{'lista_usuarios':lista_usuarios})
        #elif request.user.id
            #return render(request,'inscripciones/login.html')
    if request.user.is_authenticated():
        return HttpResponseRedirect('/proyectos/')
    return render(request,'inscripciones/login.html')

def ProyectosUsuario(request,m_id):
    if not request.user.is_authenticated():
        return render(request, 'inscripciones/login.html')
    else:
        try:
            usuarioBuscado = Usuario.objects.get(matricula=m_id)
        except User.DoesNotExist:
            raise Http404("No existe ese usuario")

        proyectos =  UsuarioProyecto.objects.filter(usuario__matricula=usuarioBuscado.matricula)

        #if request.user.is_staff:
        return render(request,'inscripciones/usuario_proyectos.html',{'usuario':usuarioBuscado,'proyectos':proyectos})
        #elif request.user.usuario.matricula == m_id:
            #return render(request,'inscripciones/usuario_proyectos.html',{'usuario':usuarioBuscado,'proyectos':proyectos})

    return render(request,'inscripciones/login.html')

def Login(request):
    next = request.GET.get('next', '/proyectos/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/proyectos/')

    return render(request, "inscripciones/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/proyectos/')

def Registro(request):
    next = request.GET.get('next', '/proyectos/')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        edad = request.POST['edad']
        direccion = request.POST['direccion']
        escuela  = request.POST['escuela']
        telefono  = request.POST['telefono']
        nombre_padre= request.POST['nombre_padre']

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        usuario = Usuario(
            first_name=first_name,last_name=last_name,password=password,
            email=email,user=user)
        usuario.last_name = last_name
        usuario.edad = edad
        usuario.telefono = telefono
        usuario.direccion = direccion
        usuario.escuela = escuela
        usuario.nombre_padre = nombre_padre
        usuario.save()

        user.username=usuario.matricula
        user.save()
        
        #send_mail('Bienvenido a Incubadora Caracol', ':', 'noreply@incubadoracaracol.com',[usuario.email], fail_silently=False)
        return render_to_response('inscripciones/registro_exitoso.html', {'user': usuario}, RequestContext(request))
    return render_to_response('inscripciones/registro.html',  RequestContext(request))

def inscribir_curso(request,proyecto_id, m_id ):
    
    try:
        proyecto = Proyecto.objects.get(pk=proyecto_id)
    except Proyecto.DoesNotExist:
        raise Http404("No existe ese proyecto")
    try:
        user = Usuario.objects.get(matricula=m_id)

    except User.DoesNotExist:
        raise Http404("No existe ese usuario")

    pro = UsuarioProyecto.objects.filter(usuario__matricula=user.matricula, proyecto__codigo=proyecto.codigo)
    
    if not pro :
        usuarioproyecto = UsuarioProyecto(usuario=user,proyecto=proyecto)
        usuarioproyecto.save()

    return HttpResponseRedirect('/proyectos/')

def getCsvUsuarios(request):
    if request.user.is_staff:

        usuario  = Usuario.objects.order_by('-first_name')
        if usuario:
            # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Lista_Completa_de_Alumnos.csv"'
            writer = csv.writer(response)

            writer.writerow(['Incubadora Caracol'])
            writer.writerow(['Fecha:', datetime.datetime.now()])
            writer.writerow([''])
            writer.writerow([''])
            writer.writerow([''])
            writer.writerow(['#','Matricula', 'Nombre del Beneficiario', 'Edad','Direccion','Telefono','Correo','Escuela','Nombre del Padre','Fecha Agregado'])
            cont = 1
            for u in usuario:
                writer.writerow([cont,u.matricula,u.first_name +' '+ u.last_name, u.edad,u.direccion,
                    u.telefono,u.email,u.escuela,u.nombre_padre,u.added])
                cont = cont + 1
            return response
        
    return HttpResponseRedirect('/usuario/')


def getCsv(request,proyecto_id):
    if request.user.is_staff:

        proyecto = Proyecto.objects.get(pk=proyecto_id)
        up  = UsuarioProyecto.objects.filter(proyecto__codigo = proyecto_id)
        if up:
            # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(content_type='text/csv')
            disposition = 'attachment; filename="Lista_Alumnos_' + proyecto.nombre + '.csv"'
            response['Content-Disposition'] = disposition
            writer = csv.writer(response)

            writer.writerow(['Proyecto:', proyecto.nombre])
            writer.writerow(['Codigo:', proyecto.codigo])
            writer.writerow(['Lugar:', proyecto.lugar])
            writer.writerow(['Horario:', proyecto.horario])
            writer.writerow([''])
            writer.writerow([''])
            writer.writerow([''])
            writer.writerow(['#','Matricula', 'Nombre del Beneficiario', 'Edad','Direccion','Telefono','Correo','Escuela','Nombre del Padre','Fecha de inscripcion'])
            cont = 1
            for proy in up:
                writer.writerow([cont,proy.usuario.matricula,proy.usuario.first_name +' '+ proy.usuario.last_name, 
                    proy.usuario.edad,proy.usuario.direccion,proy.usuario.telefono,proy.usuario.email,
                    proy.usuario.escuela,proy.usuario.nombre_padre,proy.date])
                cont = cont + 1
            return response
        
    return HttpResponseRedirect('/proyectos/'+proyecto_id)
        
from django.shortcuts import render,redirect # type: ignore
#importando el modelo cargo
from .models import Cargo
from django.contrib import messages # type: ignore

# Create your views here.
#Funcion para renderizar el listado de cargos
def inicio(request):
    listadoCargos=Cargo.objects.all()
    return render(request,"inicio.html",{'cargos':listadoCargos})
#Renderizando el formulario de nuevo cargo
def nuevoCargo(request):
    return render(request,"nuevoCargo.html")
#ALmacenando los datos de cargo en la Bdd
def guardarCargo(request):
    nombre=request.POST["nombre"]    
    funciones=request.POST["funciones"]    
    horario=request.POST["horario"]    
    requisitos=request.POST["requisitos"]    
    sueldo=request.POST["sueldo"]  

    #subiendo archivo
    logoSubido=request.FILES.get("logo")

    nuevoCargo=Cargo.objects.create(nombre=nombre,funciones=funciones,
        horario=horario,requisitos=requisitos,sueldo=sueldo, logo=logoSubido)
    
    #Mensaje de confirmacion
    messages.success(request,"Cargo GUARDADO exitosamente")
    return redirect('/')
#Eliminando cargo por ID
def eliminarCargo(request,id):
    cargoEliminar=Cargo.objects.get(id=id)
    cargoEliminar.delete()

    messages.success(request,"Cargo ELIMINADO exitosamente")
    return redirect('/')

#Mostrando el formulario de edicion
def editarCargo(request,id):
    cargoEditar=Cargo.objects.get(id=id)
    return render(request, "editarCargo.html", {'cargoEditar': cargoEditar})

def procesarEdicionCargo(request):
    id = request.POST["id"]  
    nombre=request.POST["nombre"]    
    funciones=request.POST["funciones"]    
    horario=request.POST["horario"]    
    requisitos=request.POST["requisitos"]    
    sueldo=request.POST["sueldo"].replace(',','.')
    cargo=Cargo.objects.get(id=id)
    cargo.nombre=nombre
    cargo.funciones=funciones
    cargo.horario=horario
    cargo.requisitos=requisitos
    cargo.sueldo=sueldo
    cargo.save()

    #Mensaje de confirmacion
    messages.success(request,"Cargo ACTUALIZADO exitosamente")
    return redirect('/')







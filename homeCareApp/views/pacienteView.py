"""from rest_framework import status
from rest_framework.response import Response
from homeCareApp import serializers
from homeCareApp.models.paciente import Paciente
from homeCareApp.serializers.pacienteSerializer import PacienteSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def createpaciente(request):
    if request.method == 'GET':
        modelo= Paciente.objects.all()
        serializer= PacienteSerializer(modelo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer= PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def detailpaciente(request, pk):
    if request.method == 'PUT':
        modelo= Paciente.objects.get(pk=pk)
        serializer= PacienteSerializer(modelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        modelo= Paciente.objects.get(pk=pk)
        modelo.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)"""""
        
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from homeCareApp.serializers.pacienteSerializer import PacienteSerializer
from homeCareApp.serializers.medicoSerializer import MedicoSerializer
from homeCareApp.serializers.familiarSerializer import FamiliarSerializer
from homeCareApp.serializers.enfermeroSerializer import EnfermeroSerializer
from homeCareApp.serializers.usuarioSerializer import UsuarioSerializer
from homeCareApp.models.paciente import Paciente

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Paciente")
        usuarioData = request.data.pop('usuario')           #extrae la información del diccionario que está en la llave usuario
        serializerU  = UsuarioSerializer(data=usuarioData)  #llama al serializador de usuario y le envio los datos
        serializerU.is_valid(raise_exception=True)          #valida que los datos sean válidos
        usuario = serializerU.save()                        #guarda la información en la base de datos
        enfData = request.data                              #aqui están los datos que quedaron en el diccionario para construir el objeto de medico
        enfData.update({"usuarioPaciente":usuario.id})
        serializerEnf = PacienteSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

class PacienteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)
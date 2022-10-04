from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from homeCareApp.serializers.enfermeroSerializer import EnfermeroSerializer
from homeCareApp.serializers.usuarioSerializer import UsuarioSerializer
from homeCareApp.models.enfermero import Enfermero

class EnfermeroListCreateView(generics.ListCreateAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Enfermero")
        queryset = self.get_queryset()
        serializer = EnfermeroSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Enfermero")
        usuarioData = request.data.pop('usuario')           #extrae la información del diccionario que está en la llave usuario
        serializerU  = UsuarioSerializer(data=usuarioData)  #llama al serializador de usuario y le envio los datos
        serializerU.is_valid(raise_exception=True)          #valida que los datos sean válidos
        usuario = serializerU.save()                        #guarda la información en la base de datos
        enfData = request.data                              #aqui están los datos que quedaron en el diccionario para construir el objeto de medico
        enfData.update({"usuarioEnfermero":usuario.id})
        serializerEnf = EnfermeroSerializer(data=enfData)
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

class EnfermeroRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Enfermero")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Enfermero")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)
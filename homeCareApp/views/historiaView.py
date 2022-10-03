from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from homeCareApp.serializers.historiaSerializer import HistoriaSerializer
from homeCareApp.models.usuario import Usuario
from homeCareApp.models.historiaClinica import HistoriaClinica

class HistoriaListCreateView(generics.ListCreateAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos las Historia")
        queryset = self.get_queryset()
        serializer = HistoriaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Historia")
        historiaData = request.data.pop('historiaClinica')           #extrae la información del diccionario que está en la llave usuario
        serializer  = HistoriaSerializer(data=historiaData)  #llama al serializador de usuario y le envio los datos
        serializer.is_valid(raise_exception=True)          #valida que los datos sean válidos
        serializer.save()                        #guarda la información en la base de datos
        return Response(status=status.HTTP_201_CREATED)
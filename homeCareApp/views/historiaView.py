from rest_framework import generics, status, views
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from homeCareApp.serializers.historiaSerializer import HistoriaSerializer
from homeCareApp.models.usuario import Usuario
from homeCareApp.models.historiaClinica import HistoriaClinica

class HistoriaListCreateView(generics.ListCreateAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = HistoriaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #print("POST a Historia")
        historiaData = request.data.pop('historiaClinica')
        serializer  = HistoriaSerializer(data=historiaData)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

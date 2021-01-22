from rest_framework.generics import GenericAPIView
from cliente.clienteSerializer import ClienteSerializer
from cliente.models import Cliente

from rest_framework.response import Response

class ClienteCrear(GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def post(self, request,*args,**kwargs):
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

class ClienteListar(GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request,format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes,many=True)
        return Response(serializer.data)


class Estadisticas(GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request,format=None):
        promedio = 0
        desviacion = 0

        suma_p =0
        suma_d = 0
        divisor_p=1
        divisor_d=2
        if len(Cliente.objects.all())!=0: divisor_p = len(Cliente.objects.all())
        
        for cli in Cliente.objects.all():
            suma_p = cli.edad + suma_p
        
        promedio = suma_p/divisor_p
        for cli in Cliente.objects.all():
            suma_d = (cli.edad - promedio)**2 + suma_d
        
        if len(Cliente.objects.all())>1: divisor_d = len(Cliente.objects.all())

        desviacion = (suma_d/(divisor_d-1))**0.5

        data={
            'desviacion_estandar':desviacion,
            'promedio':promedio
        }

        return Response(data)
        
        
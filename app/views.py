from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from app.serializers import SumationSerializer, HistorySerializer
from app.models import SumationRepo
from rest_framework.throttling import AnonRateThrottle

class Sum(APIView):
    throttle_classes = [AnonRateThrottle]
    
    def get(self, request, a=0, b=0):
        content = {
            'a':a,
            'b':b,
            'result':a+b
        }
        serializer = SumationSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result':serializer.validated_data['result']})


class HistoryViewSet(viewsets.ModelViewSet):

    queryset = SumationRepo.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class TotalViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        total = SumationRepo.get_total()
        return Response({'total':total})





from status.models import Status
from .serializers import StatusSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
#from rest_framework.generics import (
    #ListAPIView,
    # CreateAPIView,
    #RetrieveAPIView,
    # UpdateAPIView,
    # DestroyAPIView,
    #ListCreateAPIView,
    #RetrieveUpdateDestroyAPIView
#)
# from rest_framework.mixins import(
#     CreateModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin
# )
from rest_framework.parsers import (
    FormParser,
    MultiPartParser
)
from rest_framework.viewsets import (
    ModelViewSet
)

# Create your views here.


class StatusListCreateDetailUpdateDeleteAPIView(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [FormParser, MultiPartParser]



# class StatusAPIView(APIView):
#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)
#         return Response(status_serializer.data)


# class StatusListCreateView(ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     parser_classes = [FormParser, MultiPartParser]

# class StatusListCreateView(CreateModelMixin, ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusListAPIView(ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusCreateAPIView(CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
#     parser_classes = [FormParser, MultiPartParser]


# class StatusDetailUpdateDeleteAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class StatusDetailAPIView(RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"

    #this method is do the same as lookup_field = "id"
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get("id")
    #     return Status.objects.get(id=kw_id)


# class StatusUpdateAPIView(UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     #we dont use lookup_field here. because,
#     #we are using <pk> in urlPattern for this view
#     #we also could the same for StatusDetailAPIView


# class StatusDeleteAPIView(DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
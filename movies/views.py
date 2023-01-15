from django.shortcuts import render
from .models import Movie, QrCodePayment
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import permissions
from rest_framework.permissions import IsAuthenticated
from .forms import QrCodePaymentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import status

class MoviesListAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.order_by('?')
    # permission_classes = (permissions.IsOwner,IsAuthenticated)

class UpcomingListAPIView(ListCreateAPIView):
    serializer_class = UpcomingSerializer
    queryset = Upcoming.objects.all()

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_fields = "id"

@login_required
def qrcode_generation(request):
    if request.method == "POST":
        form = QrCodePaymentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('qrcode',form.code)
    else:
        form = QrCodePaymentForm()
    context = {'form': form}
    return render(request, 'sale.html', context)

@login_required
def gen_code(request, slug):
    code = get_object_or_404(QrCodePayment, code=slug)
    return render(request, 'qrcode.html', {'code':code})

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def qr_list(request):
    if request.method == 'GET':
        qr_code = QrCodePayment.objects.all()
        qr_serializer = QrCodeSerializer(qr_code, many=True)
        return JSONResponse(qr_serializer.data)
    elif request.method == 'POST':
        qr_data = JSONParser().parse(request)
        qr_serializer = QrCodeSerializer(data=qr_data)
        if qr_serializer.is_valid():
            qr_serializer.save()
            return JSONResponse(qr_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(qr_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_qr(request,pk):
    try:
        qr_code = QrCodePayment.objects.get(pk=pk)
    except QrCodePayment.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        qr_code_serializer = QrCodeSerializer(qr_code)
        return JSONResponse(qr_code_serializer.data)
    elif request.method == 'PUT':
        qr_code_data = JSONParser().parse(request)
        qr_code_serializer = QrCodeSerializer(qr_code, data=qr_code_data)
        if qr_code_serializer.is_valid():
            qr_code_serializer.save()
            return JSONResponse(qr_code_serializer.data)
        return JSONResponse(qr_code_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        qr_code.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
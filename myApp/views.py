# from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


# USING SELECT_RELATED:

# @api_view(["GET", "POST"])
# def ordersView(request):
#     if request.method == "GET":
#         orders = Order.objects.select_related("customer").all()
#         print(orders)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USING PREFETCH METHOD:

# @api_view(["GET", "POST"])
# def ordersView(request):
#     if request.method == "GET":
#         orders = Order.objects.prefetch_related("products").all()
#         print(orders)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------

# USING RELATED NAME without select_realted & prefetch_realted:


@api_view(["GET", "POST"])
def ordersView(request):
    if request.method == "GET":
        orders = Order.objects.all()
        # print(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

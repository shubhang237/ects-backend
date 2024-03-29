from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        desktops = Product.objects.all().filter(productType="D")
        laptops = Product.objects.all().filter(productType="L")
        printers = Product.objects.all().filter(productType="P")
        peripherals = Product.objects.all().filter(productType="O")
        apple = Product.objects.all().filter(productType="A")
        cctv = Product.objects.all().filter(productType="C")
        desktop_serializer = ProductSerializer(desktops, many = True)
        laptop_serializer = ProductSerializer(laptops, many = True)
        printer_serializer = ProductSerializer(printers, many = True)
        peripheral_serializer = ProductSerializer(peripherals, many = True)
        apple_serializer = ProductSerializer(apple, many = True)
        cctv_serializer = ProductSerializer(cctv, many = True)
        return Response({"products": {
            "desktops" : desktop_serializer.data,
            "laptops" : laptop_serializer.data,
            "printers" : printer_serializer.data,
            "peripherals" : peripheral_serializer.data,
            "apple" : apple_serializer.data,
            "cctv" : cctv_serializer.data }})

    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(),pk = pk)
        data = request.data.get('product')
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"sucess":"Product '{}' updated sucessfully".format(product_saved.name)})

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"product": "Product with id `{}` has been deleted.".format(pk)},status=204)
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response({"products":serializer.data})

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
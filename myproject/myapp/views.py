from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import read_date,write_date
from .serializers import UserSerializer

class UsetLisrView(APIView):
    def get(self,request):
        date = read_date()
        return Response(date)
    def post(self,request):
        date = read_date
        serializer = UserSerializer(date=request.date)
        if serializer.is_valid():
            new_user = serializer.date
            new_user['id'] = max([name['id'] for name in date], default=0)+1
            date.append(new_user)
            write_date(date)
            return Response(new_user,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            



# class BookDetailView(APIView):
#     def get_object(self,book_id):
#         data = read_date()
#         for book in data:
#             if book['id'] == book_id:
#                 return book
#         return None    
    
#     def get(self,request,book_id):
#         book = self.get_object(book_id)
#         if book is not None :
#             return Response(book)
#         return Response({"error","Oshibka s book_id"})   
    
#     def delete(self,request,book_id):
#         data = read_date()
#         book = self.get_object(book_id)
#         if book is None:
#             return Response(book) 
#         data = [b for b in data if b['id'] != book_id]
#         write_date(data)
#         return Response({"message","Id is deleted sucessfule"},status=status.HTTP_204_NO_CONTENT)
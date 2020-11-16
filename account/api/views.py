# from django.utils.text import slugify

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

# from ..models import Note
# from .serializers import NoteSerializer


# class NoteListCreateAPIView(ListCreateAPIView):
# 	queryset = Note.objects.all()
# 	serializer_class = NoteSerializer

# 	def perform_create(self, serializer):

# 		serializer.save(slug=slugify(self.request.POST.get("title")))

# class NoteRetrieveUpdateView(RetrieveUpdateAPIView):
# 	queryset = Note.objects.all()
# 	serializer_class = NoteSerializer


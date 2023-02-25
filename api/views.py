
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializers
from projects.models import Project


class ProjectsPageApiView(APIView):
    def get(self,request):
        projects = Project.objects.all()
        serializers = ProjectSerializers(projects,many=True)
        return  Response(serializers.data)

class ProjectsDetailPageApiView(APIView):
    def get(self,request,pk):
        projects = Project.objects.get(id=pk)
        serializers = ProjectSerializers(projects)
        return  Response(serializers.data)


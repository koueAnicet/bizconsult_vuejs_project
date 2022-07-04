import graphene
from graphene_django import DjangoObjectType
from serviceConseilApp.models import Service

class List_Service(DjangoObjectType):
    
    class Meta:
        model = Service
        fields = ('icon_service','title_service','description_service',)
         # ('icon_service','title_service','description_service',)

        
        #formatage des données en utilisant une class comm requete

class Query(graphene.ObjectType):
    all_services = graphene.List(List_Service)

    def resolve_all_services(root,info):
        return Service.objects.all()
         #return Service.objects.filter(title ="django")

#nous avons notre schema à interoger
schema = graphene.Schema(query=Query)

#pour verifier le resultat
#result = schema.execute(query=Query)

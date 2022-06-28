import graphene
from graphene_django import DjangoObjectType
from serviceConseilApp import models as modelsService

class ServiceType(DjangoObjectType):
    class Meta:
        model = modelsService.Service
         # ('icon_service','title_service','description_service',)

        
        #formatage des données en utilisant une class comm requete

class Query(graphene.ObjectType):
    all_services = graphene.List(ServiceType)
    def resolve_all_service(self):
        
        return modelsService.Service.objects.all()
         #return Service.objects.filter(title ="django")

#nous avons notre schema à interoger
schema = graphene.Schema(query=Query)

#pour verifier le resultat
#result = schema.execute(query=Query)

import graphene

from graphene_django.types import DjangoObjectType

from .models import Family , Location , Product , Transaction 

#from .models import Product ,Family ,Location ,Transaction  

class FamilyType(DjangoObjectType):
    class Meta:
        model = Family 

class LocationType(DjangoObjectType):
    class Meta:
        model = Location 

class ProductType(DjangoObjectType):
    class Meta:
        model = Product 

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class Query(graphene.AbstractType):
    all_families = graphene.List(FamilyType)
    all_locations = graphene.List(LocationType)
    all_products = graphene.List(ProductType)
    all_transactions = graphene.List(TransactionType)
    
    product = graphene.Field(ProductType,id=graphene.Int())

    def resolve_all_families(self, args, context, info):
        return Family.objects.all()

    def resolve_all_locations(self, args, context, info):
        return Location.objects.all()

    def resolve_all_products(self, args, context, info):
        return Product.objects.all()

    def resolve_all_transactions(self, args, context, info):
        return Transaction.objects.all()

    def resolve_product(self, args, context, info):
        id = args.get('id')

        if id is not None:
            return Product.objects.get(pk=id)

        return None

       
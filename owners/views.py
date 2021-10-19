import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results  = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dogs_results = []
            for dog in dogs:
                dogs_results.append(
                    {
                        "name"  : dog.name,
                        "age"   : dog.age
                    }
                )
            results.append(
            {
                "name"  : owner.name,
                "email" : owner.email,
                "age"   : owner.age,
                "dog" : dogs_results,
            }
        )
        return JsonResponse({'resutls':results}, status=200)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        dog = Dog.objects.create(
            owner = Owner.objects.get(name=data['owner']),
            name = data['dog_name'],
            age = data['dog_age']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

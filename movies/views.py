import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie

class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)

        actor = Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            movies = actor.movie_set.all()
            movie_results = []
            for movie in movies:

                movie_results.append(
                    {
                        "title" : movie.title
                    }
                )
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name"  : actor.last_name,
                    "movie"      : movie_results
                }
            )
        return JsonResponse({'resutls':results}, status=200)



class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)

        movie = Movie.objects.create(
            title = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors = movie.actors.all()
            actor_results = []
            for actor in actors:
                actor_results.append(
                    {
                        "first_name" : actor.first_name,
                    }
                )
            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "actor" : actor_results,
                }
            )
        return JsonResponse({'resutls':results}, status=200)
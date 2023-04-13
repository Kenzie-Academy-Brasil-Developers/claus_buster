from django.db import models


class Rating(models.TextChoices):
    G = 'G'
    R = 'R'
    PG = 'PG'
    PG_13 = 'PG-13'
    NC_17 = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    synopsis = models.TextField(null=True, default=None)
    rating = models.CharField(max_length=20, null=True, default=Rating.G, choices=Rating.choices)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='movies')

    def __repr__(self):
        return f'<Movie [{self.pk}] {self.title} - {self.user.username}>'
"""
Trivia!

As regras de indicação parental sobre exibição de filmes nos cinemas foram atualizadas pela última vez em setembro de 1990 pelo Sistema de classificação de filmes da Motion Picture Association, onde ficou acordado sobre as nomenclaturas e o que elas significam:

Rated G: General audiences (audiencia geral), qualquer idade permitida.
Rated PG: Parental guidance suggested (orientação parental sugerida), algumas partes podem não ser adequadas para crianças.
Rated PG-13: Parents strongly cautioned (orientação parental fortemente sugerida), algumas partes podem não ser adequadas para crianças abaixo de 13 anos.
Rated R: Restricted (restrito), pessoas abaixo de 17 anos precisam estar acompanhadas dos pais ou de supervisores adultos.
Rated NC-17: Adults Only (somente adultos), nenhuma pessoa abaixo de 17 anos é permitida.
"""

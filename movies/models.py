from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "genres"
        ordering = ["name"]
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    # Relación
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    # Auditoría (muy importante en proyectos reales)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movies"
        ordering = ["-created_at"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
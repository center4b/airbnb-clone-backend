from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by word!"
    parameter_name = "word"

    def lookups(self, request, ReviewAdmin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class BadOrGood(admin.SimpleListFilter):
    title = "Bad or Good!"
    parameter_name = "bog"

    def lookups(self, request, ReviewAdmin):
        return [
            ("bad", "Bad"),
            ("good", "Good"),
        ]

    def queryset(self, request, reviews):
        bog = self.value()
        if bog == "bad":
            return reviews.filter(rating__lte=3)
        elif bog == "good":
            return reviews.filter(rating__gte=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        BadOrGood,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )

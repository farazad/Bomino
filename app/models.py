from django.db import models


class SumationRepo(models.Model):
    a = models.IntegerField(null=False)
    b = models.IntegerField(null=False)
    result = models.IntegerField()

    @staticmethod
    def get_total():
        return SumationRepo.objects.aggregate(models.Sum('result'))['result__sum']
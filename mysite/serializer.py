# the interface with serializers
from rest_framework import serializers

from mysite import models


class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        # fields = "__all__"
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title')
    category_method = serializers.SerializerMethodField()
    status_txt = serializers.CharField(source='get_status_display')
    status_method = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        fields = "__all__"

    def get_category_method(self, obj):
        return obj.category.title

    def get_status_method(self, obj):
        return obj.get_status_display()
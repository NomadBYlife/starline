from rest_framework import serializers

from starline.models import Security, Category, Characteristic, Product, Comment


class SecuritySerializer(serializers.ModelSerializer):
    """Охранные комплексы"""
    categores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Security
        fields = ['title', 'categores']
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    """Категории комплексов"""
    class Meta:
        model = Category
        fields = ['title', ]
        depth = 1


class CharacteristicSerializer(serializers.ModelSerializer):
    """Характеристика"""

    class Meta:
        model = Characteristic
        fields = ['title', 'description']
        depth = 1


class PopularProductSerializer(serializers.ModelSerializer):
    """Популярный Товар"""
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'price_install',
            'image',
            'category',
            'presence',
        ]
        depth = 1


class NoveltiesProductSerializer(serializers.ModelSerializer):
    """Новинка Товара"""
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'price_install',
            'image',
            'category',
            'presence',
        ]
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    """Отзыв на работу"""
    class Meta:
        model = Comment
        fields = ['title', 'name', 'body']
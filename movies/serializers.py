from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_rate(self, obj):
        reviews = obj.reviews.all()
        
        if reviews:
            sum_reviews = 0
            
            for review in reviews:
                sum_reviews += review.stars
            
            reviews_count = reviews.count()
            
            return sum_reviews / reviews_count
        
        return None
    
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900.')
        return value

    def validate_resume(self, value):
        if len(value) > 1200:
            raise serializers.ValidationError('Resumo nã deve ser maior do que 1200 caracteres.')
        return value
    
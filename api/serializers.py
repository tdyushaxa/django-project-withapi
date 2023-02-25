from rest_framework import serializers
from projects.models import Project, Tag,Review
from users.models import Profile


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class ReviewsSerializers(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)
    class Meta:
        model = Review
        fields = "__all__"


class ProjectSerializers(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)
    tags = TagSerializers(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"


    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = ReviewsSerializers(reviews,many=True)
        return serializer.data

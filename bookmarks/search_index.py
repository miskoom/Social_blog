import datetime
from haystack import indexes
from accounts.models import Contact

class Contactindex(indexes.SearchIndex, indexes.indexable):
    text = indexes.CharField(document=True, use_template=True)
    user_to = indexes.CharField(model_attr='user_to')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Contact

    def index_queryset(self, using=None):
        """ Used when the entire index for model is updated"""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

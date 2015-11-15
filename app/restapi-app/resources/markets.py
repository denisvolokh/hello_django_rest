__author__ = 'denys.volokh'

from tastypie.resources import Resource
from tastypie import fields

class Market(object):
    name = fields.CharField(attribute="name", default="")


class MarketResource(Resource):
    name = fields.CharField(attribute="name", default="")

    class Meta:
        resource_name = "markets"
        object_class = Market

    def get_object_list(self, request):
        bundle = self.build_bundle(request=request)

        return self.obj_get_list(bundle)


    def obj_get_list(self, bundle, **kwargs):

        markets = [{"name" : "Australia"}, {"name" : "Japan"}]

        results = []

        for item in markets:
            obj = self.get_object_class()()
            for key in item:
                setattr(obj, key, item[key])

            results.append(obj)

        # return self.authorized_read_list(results, bundle)
        return results


    def get_object_class(self):
        return self._meta.object_class
# coding=utf-8
import datetime
import factory
import factory.fuzzy


class ElementFactory(factory.django.DjangoModelFactory):
    created = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2008, 1, 1))
    modified = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2008, 1, 1))
    name = factory.Sequence("element-name-{0}".format)
    url = factory.Sequence("element-url-{0}".format)
    visible = factory.Sequence(lambda n: n % 2 == 0)
    position = factory.Sequence(lambda n: n)

    class Meta:
        model = 'menu.Element'

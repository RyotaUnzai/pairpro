# -*- coding: utf-8 -*-

class model(object):
    def __init__(self, *args, **kwargs):
        super(model, self).__init__(*args, **kwargs)

    def debug(self):
        print ("debug")

    def replace(self, base, old, new):
        return base.replace(old, new)

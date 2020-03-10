"""Codegeneration

This module contains models for use in the codegeneration program.

Attributes
----------
model_fields_str: dict
    Django model field type: default models.py code fragment
test_str:dict
    Opinionated representation of test type: 'barebones' test_models.py code fragment

Author
------
    emilledigital@gmail.com
"""
from codegeneration.helpers import *
from codegeneration.fragments import *

class ModelField():
    def __init__(self, fieldname, djangofield):
        self.fieldname = fieldname
        self.djangofield = djangofield

    def __str__(self):
        return "{} of type {}".format(self.fieldname, self.djangofield)


class DjangoModel():
    """A representation of a models.Model
    object in Django.

    Parameters
    ----------
    modelname : type
        Description of parameter `modelname`.
    djangoapp : type
        Description of parameter `djangoapp`.
    *args : type
        Description of parameter `*args`.
    **kwargs : type
        Description of parameter `**kwargs`.

    Attributes
    ----------
    fields : type
        Description of attribute `fields`.
    isForeignkey : type
        Description of attribute `isForeignkey`.
    isForeignkeyIn : type
        Description of attribute `isForeignkeyIn`.
    foreignkey_names : type
        Description of attribute `foreignkey_names`.
    foreignkey_parent : type
        Description of attribute `foreignkey_parent`.
    models_code_fragment : type
        Description of attribute `models_code_fragment`.
    urls_code_fragment : type
        Description of attribute `urls_code_fragment`.
    serializers_code_fragment : type
        Description of attribute `serializers_code_fragment`.
    test_models_code_fragment : type
        Description of attribute `test_models_code_fragment`.
    docstring : type
        Description of attribute `docstring`.
    modelname
    djangoapp

    """
    def __init__(self, modelname, djangoapp, *args, **kwargs):
        self.fields                     = kwargs
        self.modelname                  = modelname
        self.djangoapp                  = djangoapp
        self.isForeignkey               = False
        self.isForeignkeyIn             = []
        self.foreignkey_names           = {}
        self.foreignkey_parent          = {}
        self.models_code_fragment       = ''
        self.urls_code_fragment         = ''
        self.serializers_code_fragment  = ''
        self.test_models_code_fragment  = ''
        self.docstring                  = ''

    def __str__(self):
        """TODO: Write docstring
        """
        fields = [_ for _ in self.fields.keys() if _ != 'fkeyfieldname']
        field_number = len(fields)
        if self.isForeignkey:
            return f"{self.modelname}\nForeign key in: {', '.join(self.isForeignkeyIn)}\nNumber of fields: {field_number}\nFields: {', '.join(fields)}\nNumber of foreign key fields: {len(self.foreignkey_names.values())}\nForeign key field(s): {', '.join(_ for _ in self.foreignkey_names.keys())}\n-----\n"
        return f"{self.modelname}\nNumber of fields: {field_number}\nFields: {', '.join(fields)}\nNumber of foreign key fields: {len(self.foreignkey_names.values())}\nForeign key field(s):...{', '.join(_ for _ in self.foreignkey_names.keys())}\n-----\n"

    def add_urls_code_fragment(self):
        pass

    def add_model_docstring_to_code_fragment(self):
        """Adds a docstring after adding the first line of the model's code"""
        literal   = "    \"\"\"{}\"\"\"\n"
        model_doc = literal.format(self.docstring)
        self.models_code_fragment += model_doc


    def add_field(self, djangofield, fieldname):
        """Takes two strings and updates the fields dict for
        the Django Model object"""
        self.fields[fieldname] = djangofield


    def add_foreign_keys(self, *args):
        """Takes a model or models and sets fkeyfieldname
        and isForeignkey setting so that relationships
        between models can be traced.
        """
        for model in args:
            model.isForeignkey = True
            model.isForeignkeyIn.append(self.modelname)
            fkeyfieldname = helper_return_underscore_separated_fieldname(model.modelname)
            self.foreignkey_names[model.modelname] = fkeyfieldname
            self.foreignkey_parent[fkeyfieldname] = model.djangoapp

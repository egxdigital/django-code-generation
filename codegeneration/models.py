"""Codegeneration

This module contains models for use in the codegeneration program.

Attributes
----------
model_fields_str: dict
    Django model field type: default models.py code fragment
test_str:dict
    Opinionated representation of test type: 'barebones' test_models.py code fragment

Author
-----
    emilledigital@gmail.com
"""
from codegeneration.helpers import *

model_fields_str = {
    'models.Model':     "\n\nclass {field}(models.Model):\n",
    'UUIDField':        "    {field} = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)\n",
    'DateField':        "    {field} = models.DateField(auto_now=False, auto_now_add=False)\n",
    'IntegerField':     "    {field} = models.IntegerField(null=True)\n",
    'DurationField':    "    {field} = models.DurationField(null=True)\n",
    'BooleanField':     "    {field} = models.BooleanField()\n",
    'CharField':        "    {field} = models.CharField(max_length=250)\n",
    'TextField':        "    {field} = models.TextField()",
    'ForeignKey':       "    {field} = models.ForeignKey(\'{foreignapp}.{foreignmodel}\',on_delete=models.CASCADE,)\n",
    'URLField':         "    {field} = models.URLField(null=True)\n",
}

test_str = {
    'TestCase':         "\n\nclass {}TestCase(TestCase):\n",
    'TestPrimaryKey':   "    def test_fields_{}(self):\n        pass\n\n",
    'TestisInstance':   "    def test_is_instance(self):\n        thing = mommy.make({m})\n        self.assertTrue(isinstance(thing, {m}))\n\n",
    'TestFields':       "    def test_fields_{field}(self):\n        {model} = {Model}()\n        <placeholder>\n        {model}.{field} = <placeholder>\n        {model}.save()\n        record = {Model}.objects.get({field}=<placeholder>)\n        self.assertEqual(record.{field}, <placeholder>)\n\n",
    'TestForeignKey':   "    def test_fields_{field}(self):\n        {ffield} = {fModel}()\n        {ffield}.<placeholder> = <placeholder>\n        {ffield}.save()\n        <placeholder>\n        {model} = {Model}()\n        {model}.{ffield} = {ffield}\n        {model}.<placeholder> = <placeholder>\n        {model}.save()\n        record = {Model}.objects.get({field}=<placeholder>)\n        self.assertEqual(record.{field}, <placeholder>)\n\n"
}


class ModelField():
    def __init__(self, fieldname, djangofield):
        self.fieldname = fieldname
        self.djangofield = djangofield

    def __str__(self):
        return "{} of type {}".format(self.fieldname, self.djangofield)


class DjangoModel():
    def __init__(self, modelname, djangoapp, *args, **kwargs):
        self.fields                     = kwargs
        self.modelname                  = modelname
        self.djangoapp                  = djangoapp
        self.isForeignkey               = False
        self.isForeignkeyIn             = []
        self.foreignkey_names           = {}
        self.foreignkey_parent          = {}
        self.models_code_fragment       = ''
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


    def _add_model_docstring_to_code_fragment(self):
        """Adds a docstring after adding the first line of the model's code"""
        literal   = "    \"\"\"{}\"\"\"\n"
        model_doc = literal.format(self.docstring)
        self.models_code_fragment += model_doc


    def add_line_to_models_code_fragment(self,djangofield,fieldname):
        """Concatenates a line of model code to DjangoModel.models_code_fragment
        each time a new line of the csv is read.
        """
        fmodel = helper_return_camel_case_foreign_key_modelname(fieldname)
        fapp = self.foreignkey_parent.get(fieldname)
        str = model_fields_str.get(djangofield)

        code = str.format(
                        field=fieldname,
                        foreignapp=fapp,
                        foreignmodel=fmodel
                        )

        self.models_code_fragment += code

        if djangofield == 'models.Model':
            self._add_model_docstring_to_code_fragment()


    def add_line_to_test_models_code_fragment(self, djangofield, fieldname):
        if djangofield == 'models.Model':
            str = test_str.get('TestCase')
            str2 = test_str.get('TestisInstance')
            self.test_models_code_fragment += str.format(fieldname)
            self.test_models_code_fragment += str2.format(m=fieldname)

        elif djangofield == 'UUIDField':
            str = test_str.get('TestPrimaryKey')
            self.test_models_code_fragment += str.format(fieldname)

        elif djangofield == 'ForeignKey':
            str = test_str.get('TestForeignKey')
            s = str.format(ffield=fieldname,
                           fModel=self.foreignkey_names.get(fieldname),
                           field=fieldname,
                           model='<placeholder>',
                           Model=self.modelname
                          )
            self.test_models_code_fragment += s

        else:
            if self.isForeignkey:
                str = test_str.get('TestForeignKey')
                s = str.format(ffield=fieldname,
                               fModel=self.foreignkey_names.get(fieldname),
                               field=fieldname,
                               model='<placeholder>',
                               Model=self.modelname
                                      )
                self.test_models_code_fragment += s

            else:
                str = test_str.get('TestFields')
                s = str.format(field=fieldname,
                                 model=self.modelname.lower(),
                                 Model=self.modelname
                                )
                self.test_models_code_fragment += s


    def add_field(self, djangofield, fieldname):
        """Takes two strings and updates the fields dict for
        the Django Model object"""
        self.fields[fieldname] = djangofield
        self.add_line_to_models_code_fragment(djangofield,fieldname)
        self.add_line_to_test_models_code_fragment(djangofield,fieldname)


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

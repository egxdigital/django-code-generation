"""Fragments

This module contains the format strings used throughout the
codegeneration program.

Attributes
----------
Models
    models_model_fields: dict
        The single line expressions for each Django model field
Test Models
    test_models_head
    test_models_test_case
    test_models_test_primary_key
    test_models_test_is_instance
    test_models_test_field
    test_models_test_foreign_key
Test API
    test_api_head
    test_api_list_create
    test_api_retrieve_update
URLs
    urls_skeleton
    urls_url_pattern

"""



########################################
# ADMIN                                #
########################################



admin_head = (
    "\"\"\"Admin - {djangoapp}\n\n"
    "This module contains the configuration for the Django admin site\n"
    "\"\"\"\n"
    "from django.contrib import admin\n"
    "from {djangoapp}.models import {Models}\n\n"
)

admin_class = (
    "@admin.register({Model})\n"
    "class {Model}Admin(admin.ModelAdmin):\n"
    "    pass\n\n"
)



########################################
# MODELS                               #
########################################



models_model_fields = {
    "models.Model"      :"\n\nclass {field}(models.Model):\n",
    "UUIDField"         :"    {field} = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)\n",
    "DateField"         :"    {field} = models.DateField(auto_now=False, auto_now_add=False)\n",
    "DateTimeField"     :"    {field} = models.DateTimeField(auto_now=False, auto_now_add=False)\n",
    "IntegerField"      :"    {field} = models.IntegerField(null=True)\n",
    "DurationField"     :"    {field} = models.DurationField(null=True)\n",
    "BooleanField"      :"    {field} = models.BooleanField()\n",
    "CharField"         :"    {field} = models.CharField(max_length=250)\n",
    "TextField"         :"    {field} = models.TextField()",
    "ForeignKey"        :"    {field} = models.ForeignKey(\'{foreignapp}.{foreignmodel}\',on_delete=models.CASCADE,)\n",
    "URLField"          :"    {field} = models.URLField(null=True)\n",
}

models_head = (
    "\"\"\"Models - {djangoapp}\n\n"
    "This module contains the models for the {djangoapp} application.\n\n"
    "Notes\n"
    "-----\n"
    "    Custom IDs are applied to each model using Python's uuid library\n"
    "\"\"\"\n"
    "from django.db import models\n"
    "import uuid\n"
)

models_model_str_name = (
    "def __str__(self):\n"
    "    return {desc}\n\n"
)

models_model = (
    "\n"
    "class {Model}(models.Model):\n"
    "    \"\"\"{docstring}\"\"\"\n"
    "{modelFields}"
    "\n"
    "    def __str__(self):\n"
    "        return self.{nameField}\n\n"
)

models_model_str_foreignkeys = (
    "def __str__(self):\n"
    "    return \"self.{modelField} on {foreignkey}\"\n\n"
)



########################################
# URLS                                 #
########################################



urls_register_router = (
    "router.register('api/{plural_model}', {Model}ViewSet)\n"
)

urls_router_skeleton = (
    "from django.urls import path\n"
    "from rest_framework.routers import SimpleRouter\n"
    "from {djangoapp}.api.views import {ViewSets}\n\n"
    "router = SimpleRouter()\n"
    "{contents}"
    "\n"
    "urlpatterns = router.urls"
)

urls_skeleton = (
    "from django.urls import path\n"
    "from {djangoapp}.api import views\n\n"
    "urlpatterns = [\n"
    "{contents}"
    "]\n"
)

urls_url_pattern = (
    "    path('api/{models}/',\n"
    "        views.{Model}ListCreateAPIView.as_view(),\n"
    "        name='{model}-list'),\n\n"
    "    path('api/{model}/<{lookup_field}>/',\n"
    "        views.{Model}RetrieveUpdateDestroyAPIView.as_view(),\n"
    "        name='{model}-detail'),\n\n"
)



########################################
# API                                  #
########################################



api_serializers_head = (
    "\"\"\"Serializers - {djangoapp}\n\n"
    "This module contains the serializers for the {djangoapp} application.\n"
    "\"\"\"\n"
    "from rest_framework import serializers\n"
    "from django.core.exceptions import ObjectDoesNotExist\n"
    "{externModelsSegment}"
    "{externSerializersSegment}"
    "from {djangoapp}.models import {Models}\n\n"
)

api_serializers_nested_object = (
    "    {field} = {Field}Serializer()\n"
)

api_serializers_nested_objects = (
    "class {Model}Serializer(serializers.ModelSerializer):\n"
    "{nestedObjects}\n"
    "    class Meta:\n"
    "        model = {Model}\n"
    "        fields = '__all__'\n\n"
)

api_serializers = (
    "class {Model}Serializer(serializers.ModelSerializer):\n"
    "    class Meta:\n"
    "        model = {Model}\n"
    "        fields = '__all__'\n\n"
)

api_nested_data_pop = (
    "        {field}_data = validated_data.pop('{field}')\n"
)

api_nested_try_block = (
    "        try:\n"
    "            {field}_instance = {Field}.objects.get(<chosen_field>={field}_data['<chosen_field>'])\n"
    "        except ObjectDoesNotExist:\n"
    "            {field}_instance = {Field}.objects.create(**{field}_data)\n\n"
)

api_create_with_nested = (
    "                        {field}={field}_instance,\n"
)

api_override_create = (
    "    def create(self, validated_data):\n"
    "{nestedData}"
    "\n"
    "{nestedTryBlocks}"
    "\n"
    "        {model}_instance = {Model}.objects.create(\n"
    "{nestedInstances}"
    "                        **validated_data\n"
    "                        )\n"
    "        return {model}_instance\n\n"
)

api_validated_field = (
    "        {field}_data = validated_data.get('{field}', instance.{field})\n"
)

api_instance_field = (
    "        {field} = instance.{field}\n"
)

api_instance_save = (
    "        {field}.save()\n"
)

api_instance_field_get = (
    "        {field}.{attr} = {field}_data.get(\n"
    "            '{attr}',\n"
    "            {field}.{attr}\n"
    "        )\n"
)

api_override_update = (
    "    def update(self, instance, validated_data):\n"
    "{validatedData}"
    "\n"
    "{instanceFields}"
    "\n"
    "{instanceFieldGets}"
    "\n"
    "{instanceSaves}"
    "        instance.save()\n"
    "        return instance\n\n"
)

api_views_head = (
    "\"\"\"Views - {djangoapp}\n\n"
    "This module contains the views for the {djangoapp} application.\n\n"
    "\"\"\"\n"
    "from rest_framework import generics, viewsets, permissions\n"
    "from rest_framework.permissions import IsAuthenticated, AllowAny\n"
    "from rest_framework.decorators import authentication_classes, permission_classes\n"
    "from {djangoapp}.models import {Models}\n"
    "from {djangoapp}.api.serializers import {Serializers}\n\n"
)

api_views_model_viewset = (
    "class {Model}ViewSet(viewsets.ModelViewSet):\n"
    "    queryset = {Model}.objects.all()\n"
    "    serializer_class = {Model}Serializer\n\n\n"
)



########################################
# TEST MODELS                          #
########################################



test_models_head = (
    "\"\"\"Test Models - {djangoapp}\n\n"
    "This module contains the tests for the {djangoapp} models.\n\n"
    "Example\n"
    "    python manage.py test --pattern=\"test_*\" {djangoapp}.tests.test_models\n"
    "\"\"\"\n"
    "import uuid\n"
    "import pytz\n"
    "import datetime\n"
    "from django.db import models\n"
    "from django.test import TestCase\n"
    "from model_mommy import mommy\n"
    "from {djangoapp}.models import {Models}\n\n"
)

test_models_test_field = (
    "    def test_fields_{model}_{field}(self):\n"
    "        record = {Model}.objects.get({uuidfield}=self.instance.pk)\n"
    "        self.assertEqual(record.{field}, self.instance.{field})\n\n"
)

test_models_mommy_prepare = (
    "        {model}_set = mommy.prepare(\n"
    "            _model={Model},\n"
    "{nestedAttrs}"
    "        )\n\n"
)

test_models_set_attr = (
    "           {attr} = self.data['{attr}'],\n"
)

test_models_setUp_nested = (
    "    def setUp (self):\n"
    "        self.data = {{\n"
    "{fields}"
    "        }}"
    "\n"
    "{lookups}"
    "\n"
)

test_models_setUp = (
    "    def setUp (self):\n"
    "        self.data = {{\n"
    "{fields}"
    "        }}\n"
    "\n"
    "        self.instance = mommy.make(\n"
    "           {Model},\n"
    "{attrs}"
    "        )\n"
)

test_models_class = (
    "\nclass {Model}TestCase(TestCase):\n"
    "{setUp}"
    "\n"
    "    def test_is_instance(self):\n"
    "        thing = {Model}()\n"
    "        self.assertTrue(isinstance(thing, {Model}))\n"
    "\n"
    "{testFields}"
)

test_models_nested_lookup = (
    "        self.{model}.{field} = self.data['{nestedmodel}']['{field}']\n"
)

test_models_nested_lookup_segment = (
    "\n"
    "        self.{model} = {Model}()\n"
    "{nestedLookups}"
    "\n"
    "        self.{model}.save()\n"
)

test_models_get_foreign_field = (
    "        <placeholder> = {Model}.objects.get({fuuid}=self.{model}.pk)\n"
)

test_models_set_foreign_field = (
    "        {model}.{field} = self.{instance}\n"
)

test_models_test_foreign_fields = (
    "    def test_fields_{field}(self):\n"
    "{getForeigns}"
    "\n"
    "        {model} = {Model}()\n"
    "{setForeigns}"
    "        {model}.save()\n"
    "\n"
    "        record = {Model}.objects.get({field}=<placeholder>)\n"
    "        self.assertEqual(record.{field}, self.{instance})\n\n"
)




########################################
# TEST API                             #
########################################




test_api_head = (
    "\"\"\"Test API - {djangoapp}\n\n"
    "This module cointains the test cases for the API views of the {djangoapp}\n"
    "Django application.\n\n"
    "Examples\n"
    "    python manage.py test --pattern=\"test_*\" {djangoapp}.tests\n"
    "\"\"\"\n"
    "import pprint, time, pytz, json, datetime\n"
    "from django.urls import reverse\n"
    "from django.contrib.auth.models import User\n"
    "from rest_framework.authtoken.models import Token\n"
    "from rest_framework import status\n"
    "from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient\n"
    "from rest_framework.test import force_authenticate\n"
    "{externModelsSegment}"
    "{externSerializersSegment}"
    "from {djangoapp}.models import {Models}\n"
    "from {djangoapp}.api.serializers import {Serializers}\n"
    "from {djangoapp}.api.views import {Views}\n\n"
    "client = RequestsClient()\n\n"
)

test_api_head_extern_models = (
    "from {externapp}.models import {Models}\n"
)

test_api_head_extern_serializers = (
    "from {externapp}.api.serializers import {Serializers}\n"
)

test_api_flat_model_json_key_value = (
    "\n"
    "                \"{field}\":\"{defaultVal}\","
)

test_api_updated_json_key_value = (
    "            \"{modeluuidfield}\":{model}_pk,\n"
    "{fields}"
)

test_api_nested_valid_data = (
    "            \"{nested}\":{{"
    "                {fields}"
    "\n"
    "               }},\n"
)

test_api_updated_json_key = (
    "            \"{nested}\":{{"
    "                {fields}"
    "\n"
    "               }},\n"
)

test_api_json_key_value_line = (
    "            \"{field}\":\"{defaultVal}\",\n"
)

test_api_assert_forignkey_object_counts = (
    "        self.assertEqual({ForeignkeyModel}.objects.count(), 1)\n"
)

test_api_foreignkey_object_get = (
    "        {foreignkeymodel} = str({Model}.objects.get().{foreignkey})\n"
)

test_api_assert_nested_object = (
    "        self.assertEqual({foreignkeymodel}, '<model __str__ value>')\n"
)

test_api_nestedObject_get_pk = (
    "        {foreignkey}_pk = str({ForeignkeyModel}.objects.get().{foreignkey}_id)\n"
)

test_api_nested_object_count = (
    "        self.assertEqual({ForeignkeyModel}.objects.count(), 1)\n"
)

test_api_nested_endpoint = (
    "        self.{nested}_endpoint = ('http://127.0.0.1:8000/api/{plural_nested}/')\n"
)

test_api_is_nested_valid = (
    "        valid_value = {foreignmodel}_pk\n"
    "        instance = {Model}.objects.get({foreignfield}=valid_value)\n\n"
    "        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={{'{foreignfield}':valid_value}}, HTTP_AUTHORIZATION=self.token)\n"
)

test_api_is_not_nested_valid = (
    "        valid_value = self.valid_{model}['<attr>']\n"
    "        instance = {Model}.objects.get(<attr>=valid_value)\n\n"
    "        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={{'<field>':valid_value}}, HTTP_AUTHORIZATION=self.token)\n"
)

test_api_is_nested_get = (
    "        valid_value = {foreignmodel}_pk\n"
    "        instance = {Model}.objects.get({foreignfield}=valid_value)\n\n"
    "        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)\n"
    "        force_authenticate(request, user=self.user)\n"
    "        response = self.view(request, {foreignfield}=instance.pk)\n"
)

test_api_is_not_nested_get = (
    "        valid_value = self.valid_{model}['<attr>']\n"
    "        instance = {Model}.objects.get(<field>=valid_value)\n\n"
    "        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)\n"
    "        force_authenticate(request, user=self.user)\n"
    "        response = self.view(request, <field>=instance.<field>)\n"
)

test_api_view = (
    "class Test{Model}APIView(APITestCase):\n"
    "    def setUp(self):\n"
    "        self.factory = APIRequestFactory()\n"
    "        self.view = {Model}ViewSet.as_view({{'get': 'list', 'post': 'create', 'put': 'update'}})\n"
    "        self.url = ('http://127.0.0.1:8000/api/{plural_model}/')\n"
    "\n"
    "        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')\n"
    "        self.token = Token.objects.create(user=self.user)\n"
    "        self.client.force_login(user=self.user)\n"
    "\n"
    "{nestedEndpoints}"
    "\n"
    "        self.valid_{model} = {{\n"
    "{validFields}"
    "        }}\n\n"
    "    def test_create_{model}(self):\n"
    "        response = self.client.post(self.url, self.valid_{model}, format='json', HTTP_AUTHORIZATION=self.token)\n"
    "{get_foreignkey_objects}"
    "\n"
    "        self.assertEqual(response.status_code, status.HTTP_201_CREATED)\n"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "{assertNestedObjects}\n"
    "    def test_get_single_{model}(self):\n"
    "        post_response = self.client.post(self.url, self.valid_{model}, format='json', HTTP_AUTHORIZATION=self.token)\n"
    "{nestedObject_pks}"
    "\n"
    "{isnestedGetSegment}"
    "        response.render()\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_200_OK)\n"
    "        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))\n\n"
    "    def test_update_{model}(self):\n"
    "        post = self.client.post(self.url, self.valid_{model}, format='json', HTTP_AUTHORIZATION=self.token)\n"
    "        before_valid_value = self.valid_{model}['<attr>']\n"
    "        self.assertEqual({Model}.objects.get().<attr>, before_valid_value)\n\n"
    "        {model}_pk = str({Model}.objects.get().{model}_id)\n"
    "{nestedObject_pks}"
    "\n"
    "        data = {{\n"
    "{new_fields}"
    "        }}\n\n"
    "        request = self.factory.put('api/{plural_model}/', data, format='json')\n"
    "        force_authenticate(request, user=self.user)\n"
    "        response = self.view(request, pk={model}_pk)\n"
    "        response.render()\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_200_OK)\n"
    "{assert_nested_object_counts}"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "        self.assertEqual({Model}.objects.get().<attr>, data['<attr_after>'])\n\n"
    "    def test_delete_{model}(self):\n"
    "        post = self.client.post(self.url, self.valid_{model}, format='json', HTTP_AUTHORIZATION=self.token)\n"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "{nestedObject_pks}"
    "\n"
    "{isNestedValidSegment}"
    "\n"
    "        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)\n"
    "        self.assertEqual({Model}.objects.count(), 0)\n\n\n"
)

test_api_list_create = (
    "class Test{Model}ListCreateAPIView(APITestCase):\n"
    "    def setUp(self):\n"
    "        self.factory = APIRequestFactory()\n"
    "        self.url = reverse('{model}-list')\n"
    "        \"\"\"<ADD DATA INSTANCES HERE>\"\"\"\n\n"
    "    def test_create_{models}(self):\n"
    "        \"\"\"Tests the {model}-list endpoint for the creation of\n"
    "        a multiple entries using the POST method.\n"
    "        \"\"\"\n"
    "        response = self.client.post(self.url,self.<placeholder>,format='json')\n\n"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "        self.assertEqual(response.status_code, status.HTTP_201_CREATED)\n\n"
    "    def test_create_{model}(self):\n"
    "        \"\"\"Tests the {model}-list endpoint for the creation of\n"
    "        a single entry using the POST method.\n"
    "        \"\"\"\n"
    "        response = self.client.post(self.url, self.<placeholder>, format='json')\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_201_CREATED)\n"
    "        self.assertEqual({Model}.objects.get().{lookup_field}, self.<placeholder>['{lookup_field}'])\n\n\n"
)

test_api_retrieve_update = (
    "class Test{Model}RetrieveUpdateDestroyAPIView(APITestCase):\n"
    "    def setUp(self):\n"
    "        self.factory = APIRequestFactory()\n"
    "        self.view = {Model}RetrieveUpdateDestroyAPIView.as_view()\n\n"
    "    def test_get_single_{model}(self):\n"
    "        \"\"\"Tests the {model}-list endpoint for the retrieval of\n"
    "        a single entry using the GET method.\n"
    "        \"\"\"\n"
    "        post_url = reverse('{model}-list')\n"
    "        post_request = self.client.post(post_url, self.<placeholder>, format='json')\n"
    "        a = {Model}.objects.get({lookup_field}='<placeholder>')\n\n"
    "        request = self.factory.get('{model}-detail')\n"
    "        response = self.view(request, {lookup_field}=a.{lookup_field})\n"
    "        response.render()\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_200_OK)\n"
    "        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')\n\n"
    "    def test_update_{model}(self):\n"
    "        \"\"\"Tests the {model}-detail endpoint for the update of\n"
    "        a single entry using the PUT method.\n"
    "        \"\"\"\n"
    "        post_url = reverse('{model}-list')\n"
    "        post_request = self.client.post(post_url, self.<placeholder>, format='json')\n\n"
    "        saved = {Model}.objects.get({lookup_field}=self.<placeholder>['{lookup_field}'])\n"
    "        edited = <self.instance_edited_{model}>\n\n"
    "        put_url = reverse('{model}-detail', kwargs=<{lookup_field}: saved.{lookup_field}>)\n"
    "        response = self.client.put(put_url, edited)\n"
    "        response_data = json.loads(response.content)\n"
    "        self.assertEqual(response.status_code, status.HTTP_200_OK)\n"
    "        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')\n\n"
    "    def test_delete_{model}(self):\n"
    "        \"\"\"Tests the {model}-detail endpoint for the deletion of\n"
    "        a single entry using the DELETE method.\n"
    "        \"\"\"\n"
    "        post_url = reverse('{model}-list')\n"
    "        post_request = self.client.post(post_url, self.<placeholder>, format='json')\n\n"
    "        a = {Model}.objects.get({lookup_field}=self.<placeholder>['{lookup_field}'])\n\n"
    "        request = self.factory.delete('{model}-detail')\n"
    "        response = self.view(request, {lookup_field}=a.{lookup_field})\n"
    "        response.render()\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)\n"
    "        self.assertEqual({Model}.objects.count(), 0)\n\n\n"
)

if __name__ == '__main__':
    thing = test_models_test_field
    print (type(thing), "\n", thing)

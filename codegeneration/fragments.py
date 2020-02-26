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

Notes
-----
    Is this module necessary?
    This module was created provisionally, to support a task.
    It may become a part of the project.

"""

admin_head = (
    "from django.contrib import admin\n"
    "from scraper.models import {modelList}\n\n"
)

admin_class = {
    "@admin.register(JobBoard)\n"
    "class JobBoardAdmin(admin.ModelAdmin):\n"
    "    pass"
}

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


models_model_str_name = (
    "def __str__(self):\n"
    "    return {desc}\n\n"
)

models_model_str_foreignkeys = (
    "def __str__(self):\n"
    "    return \"self.{modelField} on {foreignkey}\"\n\n"
)


urls_register_router = (
    "router.register('api/{plural_model})', {Model}ViewSet)\n"
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


api_serializers_head = (
    "\"\"\"Serializers - {djangoapp}\n"
    "This module contains the serializers for the {djangoapp} application.\n\n"
    "\"\"\"\n"
    "from rest_framework import serializers\n"
    "from django.core.exceptions import ObjectDoesNotExist\n"
    "from {djangoapp}.models import {Models}\n\n"
)


api_serializers_nested_objects = (
    "class {Model}Serializer(serializers.ModelSerializer):\n"
    "{nestedObjects}\n\n"
    "class Meta:\n"
    "    model = {Model}\n"
    "    fields = '__all__'\n\n"
)

api_serializers = (
    "class {Model}Serializer(serializers.ModelSerializer):\n"
    "class Meta:\n"
    "    model = {Model}\n"
    "    fields = '__all__'\n"
)

api_override_create = (
    ""
)


test_models_head = (
    "\"\"\"Models - {djangoapp}\n"
    "This module contains the models for the {djangoapp} application.\n\n"
    "Notes\n"
    "-----\n"
    "    Custom IDs are applied to each model using Python's uuid library\n"
    "\"\"\"\n"
    "from django.db import models\n"
    "import uuid\n"
)


test_models_test_case = (
    "\n\nclass {}TestCase(TestCase):\n"
)


test_models_setUp = (
    "def setUp (self):\n"
    "    self.thing = mommy.make({Model})\n\n"
)

test_models_test_primary_key = (
    "def test_fields_{}(self):\n"
    "    record = {Model}.objects.get({model}_id=self.thing.pk)\n"
    "    self.assertEqual(record.pk, self.thing.pk)\n"
)

test_models_test_is_instance = (
    "def test_is_instance(self):\n"
    "    self.assertTrue(isinstance(self.thing, {}))\n\n"
)

test_models_test_field = (
    "    def test_fields_{field}(self):\n"
    "        {model} = {Model}()\n"
    "        <placeholder>\n"
    "        {model}.{field} = <placeholder>\n"
    "        {model}.save()\n"
    "        record = {Model}.objects.get({field}=<placeholder>)\n"
    "        self.assertEqual(record.{field}, <placeholder>)\n\n"
)


test_models_test_foreign_key = (
    "    def test_fields_{field}(self):\n"
    "        {ffield} = {fModel}()\n"
    "        {ffield}.<placeholder> = <placeholder>\n"
    "        {ffield}.save()\n"
    "        <placeholder>\n"
    "        {model} = {Model}()\n"
    "        {model}.{ffield} = {ffield}\n"
    "        {model}.<placeholder> = <placeholder>\n"
    "        {model}.save()\n"
    "        record = {Model}.objects.get({field}=<placeholder>)\n"
    "        self.assertEqual(record.{field}, <placeholder>)\n\n"
)



########################################
# TEST API                             #
########################################


test_api_head = (
    "\"\"\"Test API\n\n"
    "This module cointains the test cases for the API views of the {djangoapp}\n"
    "Django application.\n\n"
    "Examples\n"
    "    python manage.py test --pattern=\"test_*\" {djangoapp}.tests\n\n"
    "\"\"\"\n"
    "import pprint, time, pytz, json, datetime\n"
    "from django.urls import reverse\n"
    "from rest_framework import status\n"
    "from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient\n"
    "from {djangoapp}.models import {Models}\n"
    "from {djangoapp}.api.serializers import {Serializers}\n"
    "from {djangoapp}.api.views import {Views}\n\n"
    "client = RequestsClient()\n\n"
)

test_api_flat_model_json_key_value = (
    "\n"
    "                {field}:{defaultVal},"
)

test_api_updated_json_key_value = (
    "            {modeluuidfield}:{model},\n"
    "{fields}"
)

test_api_updated_json_key = (
    "            {nested}:"
    "                {fields},\n"
)

test_api_json_key_value_line = (
    "            {field}:{defaultVal},\n"
)

test_api_assert_forignkey_object_counts = (
    "        self.assertEqual({ForeignkeyModel}.objects.count(), 1)\n"
)

test_api_forignkey_object_get = (
    "        {foreignkey} = str({ForeignkeyModel}.objects.get().{foreignkey})\n"
)

test_api_assert_nested_object = (
    "        self.assertEqual({foreignkey}, '<model __str__ value>')\n"
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

test_api_view_nested_model = (
    "class Test{Model}APIView(APITestCase):\n"
    "    def setUp(self):\n"
    "        self.factory = APIRequestFactory()\n"
    "        self.view = {Model}ViewSet.as_view({{'get': 'list', 'post': 'create', 'put': 'update'}})\n"
    "        self.url = ('http://127.0.0.1:8000/api/{plural_model}/')\n"
    "{nestedEndpoints}"
    "\n"
    "        self.valid_{model} = {{\n"
    "{fields}"
    "        }}\n\n"
    "    def test_create_{model}(self):\n"
    "        response = self.client.post(self.url, self.valid_{model}, format='json')\n"
    "{get_foreignkey_objects}"
    "\n"
    "        self.assertEqual(response.status_code, status.HTTP_201_CREATED)\n"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "{assertNestedObjects}\n\n"
    "    def test_update_{model}(self):\n"
    "        post = self.client.post(self.url, self.valid_{model}, format='json')\n"
    "        self.assertEqual({Model}.objects.get().<field>.<attr>, \"<before_value>\")\n\n"
    "        {model}_pk = str({Model}.objects.get().{model}_id)\n"
    "{nestedObject_pks}"
    "\n"
    "        data = {{\n"
    "{new_fields}"
    "        }}\n\n"
    "        request = self.factory.put('api/{plural_model}/', data, format='json')\n"
    "        response = self.view(request, pk={model}_pk)\n"
    "        response.render()\n\n"
    "        self.assertEqual(response.status_code, status.HTTP_200_OK)\n"
    "{assert_nested_object_counts}"
    "        self.assertEqual({Model}.objects.count(), 1)\n"
    "        self.assertEqual({Model}.objects.get().<field>.<attr>, \"<after value>\")\n\n\n"
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

"""Serializers - jobsdatastore

This module contains the serializers for the jobsdatastore application.
"""
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField, UUIDField
from jobsdatastore.models import Company, Technology, CompanyTechnology

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class CompanyTechnologyPostSerializer(serializers.ModelSerializer):
    company = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Company.objects.all())
    technology = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Technology.objects.all())

    class Meta:
        model = CompanyTechnology
        fields = '__all__'


class CompanyTechnologyGetSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    technology = TechnologySerializer()

    class Meta:
        model = CompanyTechnology
        fields = '__all__'

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        technology_data = validated_data.pop('technology')

        try:
            company_instance = Company.objects.get(<chosen_field>=company_data['<chosen_field>'])
        except ObjectDoesNotExist:
            company_instance = Company.objects.create(**company_data)

        try:
            technology_instance = Technology.objects.get(<chosen_field>=technology_data['<chosen_field>'])
        except ObjectDoesNotExist:
            technology_instance = Technology.objects.create(**technology_data)


        companytechnology_instance = CompanyTechnology.objects.create(
                        company=company_instance,
                        technology=technology_instance,
                        **validated_data
                        )
        return companytechnology_instance

    def update(self, instance, validated_data):
        company_data = validated_data.get('company', instance.company)
        technology_data = validated_data.get('technology', instance.technology)

        company = instance.company
        technology = instance.technology

        company.company_id = company_data.get(
            'company_id',
            company.company_id
        )
        company.company_name = company_data.get(
            'company_name',
            company.company_name
        )
        company.hiring_from = company_data.get(
            'hiring_from',
            company.hiring_from
        )
        technology.technology_id = technology_data.get(
            'technology_id',
            technology.technology_id
        )
        technology.technology_name = technology_data.get(
            'technology_name',
            technology.technology_name
        )

        company.save()
        technology.save()
        instance.save()
        return instance



"""Serializers - jobsdatabucket

This module contains the serializers for the jobsdatabucket application.
"""
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField, UUIDField
from django.core.exceptions import ObjectDoesNotExist
from jobsdatastore.models import Technology, Company
from scraper.models import Scrape, ListingTag
from jobsdatastore.api.serializers import TechnologySerializer, CompanySerializer
from scraper.api.serializers import ScrapeSerializer, ListingTagSerializer
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'


class JobPostCompanyPostSerializer(serializers.ModelSerializer):
    job_post = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobPost.objects.all())
    company = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Company.objects.all())

    class Meta:
        model = JobPostCompany
        fields = '__all__'


class JobPostCompanyGetSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    company = CompanySerializer()

    class Meta:
        model = JobPostCompany
        fields = '__all__'

    def create(self, validated_data):
        job_post_data = validated_data.pop('job_post')
        company_data = validated_data.pop('company')

        try:
            job_post_instance = JobPost.objects.get(<chosen_field>=job_post_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_post_instance = JobPost.objects.create(**job_post_data)

        try:
            company_instance = Company.objects.get(<chosen_field>=company_data['<chosen_field>'])
        except ObjectDoesNotExist:
            company_instance = Company.objects.create(**company_data)


        jobpostcompany_instance = JobPostCompany.objects.create(
                        job_post=job_post_instance,
                        company=company_instance,
                        **validated_data
                        )
        return jobpostcompany_instance

    def update(self, instance, validated_data):
        job_post_data = validated_data.get('job_post', instance.job_post)
        company_data = validated_data.get('company', instance.company)

        job_post = instance.job_post
        company = instance.company

        job_post.jobpost_id = job_post_data.get(
            'jobpost_id',
            job_post.jobpost_id
        )
        job_post.job_title = job_post_data.get(
            'job_title',
            job_post.job_title
        )
        job_post.date_posted = job_post_data.get(
            'date_posted',
            job_post.date_posted
        )
        job_post.apply_link = job_post_data.get(
            'apply_link',
            job_post.apply_link
        )
        job_post.job_description = job_post_data.get(
            'job_description',
            job_post.job_description
        )
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

        job_post.save()
        company.save()
        instance.save()
        return instance


class JobPostListingTagPostSerializer(serializers.ModelSerializer):
    job_post = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobPost.objects.all())
    listing_tag = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=ListingTag.objects.all())

    class Meta:
        model = JobPostListingTag
        fields = '__all__'


class JobPostListingTagGetSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    listing_tag = ListingTagSerializer()

    class Meta:
        model = JobPostListingTag
        fields = '__all__'

    def create(self, validated_data):
        job_post_data = validated_data.pop('job_post')
        listing_tag_data = validated_data.pop('listing_tag')

        try:
            job_post_instance = JobPost.objects.get(<chosen_field>=job_post_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_post_instance = JobPost.objects.create(**job_post_data)

        try:
            listing_tag_instance = ListingTag.objects.get(<chosen_field>=listing_tag_data['<chosen_field>'])
        except ObjectDoesNotExist:
            listing_tag_instance = ListingTag.objects.create(**listing_tag_data)


        jobpostlistingtag_instance = JobPostListingTag.objects.create(
                        job_post=job_post_instance,
                        listing_tag=listing_tag_instance,
                        **validated_data
                        )
        return jobpostlistingtag_instance

    def update(self, instance, validated_data):
        job_post_data = validated_data.get('job_post', instance.job_post)
        listing_tag_data = validated_data.get('listing_tag', instance.listing_tag)

        job_post = instance.job_post
        listing_tag = instance.listing_tag

        job_post.jobpost_id = job_post_data.get(
            'jobpost_id',
            job_post.jobpost_id
        )
        job_post.job_title = job_post_data.get(
            'job_title',
            job_post.job_title
        )
        job_post.date_posted = job_post_data.get(
            'date_posted',
            job_post.date_posted
        )
        job_post.apply_link = job_post_data.get(
            'apply_link',
            job_post.apply_link
        )
        job_post.job_description = job_post_data.get(
            'job_description',
            job_post.job_description
        )
        listing_tag.listingtag_id = listing_tag_data.get(
            'listingtag_id',
            listing_tag.listingtag_id
        )
        listing_tag.listingtag_name = listing_tag_data.get(
            'listingtag_name',
            listing_tag.listingtag_name
        )

        job_post.save()
        listing_tag.save()
        instance.save()
        return instance


class JobPostScrapePostSerializer(serializers.ModelSerializer):
    job_post = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobPost.objects.all())
    scrape = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Scrape.objects.all())

    class Meta:
        model = JobPostScrape
        fields = '__all__'


class JobPostScrapeGetSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    scrape = ScrapeSerializer()

    class Meta:
        model = JobPostScrape
        fields = '__all__'

    def create(self, validated_data):
        job_post_data = validated_data.pop('job_post')
        scrape_data = validated_data.pop('scrape')

        try:
            job_post_instance = JobPost.objects.get(<chosen_field>=job_post_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_post_instance = JobPost.objects.create(**job_post_data)

        try:
            scrape_instance = Scrape.objects.get(<chosen_field>=scrape_data['<chosen_field>'])
        except ObjectDoesNotExist:
            scrape_instance = Scrape.objects.create(**scrape_data)


        jobpostscrape_instance = JobPostScrape.objects.create(
                        job_post=job_post_instance,
                        scrape=scrape_instance,
                        **validated_data
                        )
        return jobpostscrape_instance

    def update(self, instance, validated_data):
        job_post_data = validated_data.get('job_post', instance.job_post)
        scrape_data = validated_data.get('scrape', instance.scrape)

        job_post = instance.job_post
        scrape = instance.scrape

        job_post.jobpost_id = job_post_data.get(
            'jobpost_id',
            job_post.jobpost_id
        )
        job_post.job_title = job_post_data.get(
            'job_title',
            job_post.job_title
        )
        job_post.date_posted = job_post_data.get(
            'date_posted',
            job_post.date_posted
        )
        job_post.apply_link = job_post_data.get(
            'apply_link',
            job_post.apply_link
        )
        job_post.job_description = job_post_data.get(
            'job_description',
            job_post.job_description
        )
        scrape.scrape_id = scrape_data.get(
            'scrape_id',
            scrape.scrape_id
        )
        scrape.scrape_datetime = scrape_data.get(
            'scrape_datetime',
            scrape.scrape_datetime
        )
        scrape.entries_scraped = scrape_data.get(
            'entries_scraped',
            scrape.entries_scraped
        )
        scrape.scrape_duration = scrape_data.get(
            'scrape_duration',
            scrape.scrape_duration
        )
        scrape.scrape_success = scrape_data.get(
            'scrape_success',
            scrape.scrape_success
        )

        job_post.save()
        scrape.save()
        instance.save()
        return instance


class JobPostTechnologyPostSerializer(serializers.ModelSerializer):
    job_post = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobPost.objects.all())
    technology = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Technology.objects.all())

    class Meta:
        model = JobPostTechnology
        fields = '__all__'


class JobPostTechnologyGetSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    technology = TechnologySerializer()

    class Meta:
        model = JobPostTechnology
        fields = '__all__'

    def create(self, validated_data):
        job_post_data = validated_data.pop('job_post')
        technology_data = validated_data.pop('technology')

        try:
            job_post_instance = JobPost.objects.get(<chosen_field>=job_post_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_post_instance = JobPost.objects.create(**job_post_data)

        try:
            technology_instance = Technology.objects.get(<chosen_field>=technology_data['<chosen_field>'])
        except ObjectDoesNotExist:
            technology_instance = Technology.objects.create(**technology_data)


        jobposttechnology_instance = JobPostTechnology.objects.create(
                        job_post=job_post_instance,
                        technology=technology_instance,
                        **validated_data
                        )
        return jobposttechnology_instance

    def update(self, instance, validated_data):
        job_post_data = validated_data.get('job_post', instance.job_post)
        technology_data = validated_data.get('technology', instance.technology)

        job_post = instance.job_post
        technology = instance.technology

        job_post.jobpost_id = job_post_data.get(
            'jobpost_id',
            job_post.jobpost_id
        )
        job_post.job_title = job_post_data.get(
            'job_title',
            job_post.job_title
        )
        job_post.date_posted = job_post_data.get(
            'date_posted',
            job_post.date_posted
        )
        job_post.apply_link = job_post_data.get(
            'apply_link',
            job_post.apply_link
        )
        job_post.job_description = job_post_data.get(
            'job_description',
            job_post.job_description
        )
        technology.technology_id = technology_data.get(
            'technology_id',
            technology.technology_id
        )
        technology.technology_name = technology_data.get(
            'technology_name',
            technology.technology_name
        )

        job_post.save()
        technology.save()
        instance.save()
        return instance



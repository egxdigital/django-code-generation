"""Serializers - scraper

This module contains the serializers for the scraper application.
"""
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField, UUIDField
from django.core.exceptions import ObjectDoesNotExist
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag

class JobBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobBoard
        fields = '__all__'


class ListingTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingTag
        fields = '__all__'


class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrape
        fields = '__all__'


class ScrapeJobBoardPostSerializer(serializers.ModelSerializer):
    scrape = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=Scrape.objects.all())
    job_board = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobBoard.objects.all())

    class Meta:
        model = ScrapeJobBoard
        fields = '__all__'


class ScrapeJobBoardGetSerializer(serializers.ModelSerializer):
    scrape = ScrapeSerializer()
    job_board = JobBoardSerializer()

    class Meta:
        model = ScrapeJobBoard
        fields = '__all__'

    def create(self, validated_data):
        scrape_data = validated_data.pop('scrape')
        job_board_data = validated_data.pop('job_board')

        try:
            scrape_instance = Scrape.objects.get(<chosen_field>=scrape_data['<chosen_field>'])
        except ObjectDoesNotExist:
            scrape_instance = Scrape.objects.create(**scrape_data)

        try:
            job_board_instance = JobBoard.objects.get(<chosen_field>=job_board_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_board_instance = JobBoard.objects.create(**job_board_data)


        scrapejobboard_instance = ScrapeJobBoard.objects.create(
                        scrape=scrape_instance,
                        job_board=job_board_instance,
                        **validated_data
                        )
        return scrapejobboard_instance

    def update(self, instance, validated_data):
        scrape_data = validated_data.get('scrape', instance.scrape)
        job_board_data = validated_data.get('job_board', instance.job_board)

        scrape = instance.scrape
        job_board = instance.job_board

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
        job_board.jobboard_id = job_board_data.get(
            'jobboard_id',
            job_board.jobboard_id
        )
        job_board.jobboard_name = job_board_data.get(
            'jobboard_name',
            job_board.jobboard_name
        )
        job_board.home_page = job_board_data.get(
            'home_page',
            job_board.home_page
        )
        job_board.search_page = job_board_data.get(
            'search_page',
            job_board.search_page
        )

        scrape.save()
        job_board.save()
        instance.save()
        return instance


class JobBoardListingTagPostSerializer(serializers.ModelSerializer):
    job_board = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=JobBoard.objects.all())
    listing_tag = PrimaryKeyRelatedField(pk_field=UUIDField(format='hex'), queryset=ListingTag.objects.all())

    class Meta:
        model = JobBoardListingTag
        fields = '__all__'


class JobBoardListingTagGetSerializer(serializers.ModelSerializer):
    job_board = JobBoardSerializer()
    listing_tag = ListingTagSerializer()

    class Meta:
        model = JobBoardListingTag
        fields = '__all__'

    def create(self, validated_data):
        job_board_data = validated_data.pop('job_board')
        listing_tag_data = validated_data.pop('listing_tag')

        try:
            job_board_instance = JobBoard.objects.get(<chosen_field>=job_board_data['<chosen_field>'])
        except ObjectDoesNotExist:
            job_board_instance = JobBoard.objects.create(**job_board_data)

        try:
            listing_tag_instance = ListingTag.objects.get(<chosen_field>=listing_tag_data['<chosen_field>'])
        except ObjectDoesNotExist:
            listing_tag_instance = ListingTag.objects.create(**listing_tag_data)


        jobboardlistingtag_instance = JobBoardListingTag.objects.create(
                        job_board=job_board_instance,
                        listing_tag=listing_tag_instance,
                        **validated_data
                        )
        return jobboardlistingtag_instance

    def update(self, instance, validated_data):
        job_board_data = validated_data.get('job_board', instance.job_board)
        listing_tag_data = validated_data.get('listing_tag', instance.listing_tag)

        job_board = instance.job_board
        listing_tag = instance.listing_tag

        job_board.jobboard_id = job_board_data.get(
            'jobboard_id',
            job_board.jobboard_id
        )
        job_board.jobboard_name = job_board_data.get(
            'jobboard_name',
            job_board.jobboard_name
        )
        job_board.home_page = job_board_data.get(
            'home_page',
            job_board.home_page
        )
        job_board.search_page = job_board_data.get(
            'search_page',
            job_board.search_page
        )
        listing_tag.listingtag_id = listing_tag_data.get(
            'listingtag_id',
            listing_tag.listingtag_id
        )
        listing_tag.listingtag_name = listing_tag_data.get(
            'listingtag_name',
            listing_tag.listingtag_name
        )

        job_board.save()
        listing_tag.save()
        instance.save()
        return instance



class TestJobBoardAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobBoardViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobboards/')

        self.valid_jobboard = {
            jobboard_name:CharField,
            home_page:URLField,
            search_page:URLField,
        }

    def test_create_jobboard(self):
        response = self.client.post(self.url, self.valid_jobboard, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoard.objects.count(), 1)


    def test_update_jobboard(self):
        post = self.client.post(self.url, self.valid_jobboard, format='json')
        self.assertEqual(JobBoard.objects.get().<field>.<attr>, "<before_value>")

        jobboard_pk = str(JobBoard.objects.get().jobboard_id)

        data = {
            jobboard_name:CharField,
            home_page:URLField,
            search_page:URLField,
        }

        request = self.factory.put('api/jobboards/', data, format='json')
        response = self.view(request, pk=jobboard_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(JobBoard.objects.get().<field>.<attr>, "<after value>")


class TestListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/listingtags/')

        self.valid_listingtag = {
            listingtag_name:CharField,
        }

    def test_create_listingtag(self):
        response = self.client.post(self.url, self.valid_listingtag, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ListingTag.objects.count(), 1)


    def test_update_listingtag(self):
        post = self.client.post(self.url, self.valid_listingtag, format='json')
        self.assertEqual(ListingTag.objects.get().<field>.<attr>, "<before_value>")

        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            listingtag_name:CharField,
        }

        request = self.factory.put('api/listingtags/', data, format='json')
        response = self.view(request, pk=listingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(ListingTag.objects.get().<field>.<attr>, "<after value>")


class TestScrapeAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ScrapeViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/scrapes/')

        self.valid_scrape = {
            scrape_date:DateField,
            entries_scraped:IntegerField,
            scrape_duration:DurationField,
            scrape_success:BooleanField,
        }

    def test_create_scrape(self):
        response = self.client.post(self.url, self.valid_scrape, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scrape.objects.count(), 1)


    def test_update_scrape(self):
        post = self.client.post(self.url, self.valid_scrape, format='json')
        self.assertEqual(Scrape.objects.get().<field>.<attr>, "<before_value>")

        scrape_pk = str(Scrape.objects.get().scrape_id)

        data = {
            scrape_date:DateField,
            entries_scraped:IntegerField,
            scrape_duration:DurationField,
            scrape_success:BooleanField,
        }

        request = self.factory.put('api/scrapes/', data, format='json')
        response = self.view(request, pk=scrape_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(Scrape.objects.get().<field>.<attr>, "<after value>")


class TestScrapeJobBoardAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ScrapeJobBoardViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/scrapejobboards/')
        self.scrape_endpoint = ('http://127.0.0.1:8000/api/scrapes/')
        self.jobboard_endpoint = ('http://127.0.0.1:8000/api/jobboards/')

        self.valid_scrapejobboard = {
            scrape:
                scrape_date:DateField,
                entries_scraped:IntegerField,
                scrape_duration:DurationField,
                scrape_success:BooleanField,,
            job_board:
                jobboard_name:CharField,
                home_page:URLField,
                search_page:URLField,,
        }

    def test_create_scrapejobboard(self):
        response = self.client.post(self.url, self.valid_scrapejobboard, format='json')
        scrape = str(Scrape.objects.get().scrape)
        job_board = str(JobBoard.objects.get().job_board)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ScrapeJobBoard.objects.count(), 1)
        self.assertEqual(scrape, '<model __str__ value>')
        self.assertEqual(job_board, '<model __str__ value>')


    def test_update_scrapejobboard(self):
        post = self.client.post(self.url, self.valid_scrapejobboard, format='json')
        self.assertEqual(ScrapeJobBoard.objects.get().<field>.<attr>, "<before_value>")

        scrapejobboard_pk = str(ScrapeJobBoard.objects.get().scrapejobboard_id)
        scrape_pk = str(Scrape.objects.get().scrape_id)
        job_board_pk = str(JobBoard.objects.get().job_board_id)

        data = {
            scrapejobboard_id:scrapejobboard,
            scrape:                
                scrape_date:DateField,
                entries_scraped:IntegerField,
                scrape_duration:DurationField,
                scrape_success:BooleanField,,
            job_board:                
                jobboard_name:CharField,
                home_page:URLField,
                search_page:URLField,,
        }

        request = self.factory.put('api/scrapejobboards/', data, format='json')
        response = self.view(request, pk=scrapejobboard_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(ScrapeJobBoard.objects.count(), 1)
        self.assertEqual(ScrapeJobBoard.objects.get().<field>.<attr>, "<after value>")


class TestJobBoardListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobBoardListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobboardlistingtags/')
        self.jobboard_endpoint = ('http://127.0.0.1:8000/api/jobboards/')
        self.listingtag_endpoint = ('http://127.0.0.1:8000/api/listingtags/')

        self.valid_jobboardlistingtag = {
            job_board:
                jobboard_name:CharField,
                home_page:URLField,
                search_page:URLField,,
            listing_tag:
                listingtag_name:CharField,,
        }

    def test_create_jobboardlistingtag(self):
        response = self.client.post(self.url, self.valid_jobboardlistingtag, format='json')
        job_board = str(JobBoard.objects.get().job_board)
        listing_tag = str(ListingTag.objects.get().listing_tag)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoardListingTag.objects.count(), 1)
        self.assertEqual(job_board, '<model __str__ value>')
        self.assertEqual(listing_tag, '<model __str__ value>')


    def test_update_jobboardlistingtag(self):
        post = self.client.post(self.url, self.valid_jobboardlistingtag, format='json')
        self.assertEqual(JobBoardListingTag.objects.get().<field>.<attr>, "<before_value>")

        jobboardlistingtag_pk = str(JobBoardListingTag.objects.get().jobboardlistingtag_id)
        job_board_pk = str(JobBoard.objects.get().job_board_id)
        listing_tag_pk = str(ListingTag.objects.get().listing_tag_id)

        data = {
            jobboardlistingtag_id:jobboardlistingtag,
            job_board:                
                jobboard_name:CharField,
                home_page:URLField,
                search_page:URLField,,
            listing_tag:                
                listingtag_name:CharField,,
        }

        request = self.factory.put('api/jobboardlistingtags/', data, format='json')
        response = self.view(request, pk=jobboardlistingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(JobBoardListingTag.objects.count(), 1)
        self.assertEqual(JobBoardListingTag.objects.get().<field>.<attr>, "<after value>")



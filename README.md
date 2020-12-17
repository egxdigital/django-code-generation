# django code generation

> Takes an ordered set of n CSVs and produces n Django applications complete with REST API endpoints and tests.


## Description

Generate files for a working Django project complete with a REST API and tests. 


Write your Django models and fields in a spreadsheet!

One CSV file per 'Django app' (a folder within the Django project root)

Endpoint tests are scaffolded for CRUD operations on each model via the REST API.

## Example usage

Prepare a CSV file containing your models and fields.

The CSV file must contain **at least** the following columns:

* DJANGO FIELD
* FIELD NAME

A typical spreadsheet may looklike this one

```
DJANGO FIELD  FIELD NAME
------------  ----------
models.Model  JobBoard
UUIDField     jobboard_id
CharField     jobboard_name
URLField      home_page
URLField      search_page
models.Model  ListingTag
UUIDField     listingtag_id
CharField     listingtag_name
models.Model  Scrape
UUIDField     scrape_id
DateTimeField scrape_datetime
IntegerField  entries_scraped
DurationField scrape_duration
BooleanField  scrape_success
models.Model  ScrapeJobBoard
UUIDField     scrapejobboard_id
ForeignKey    scrape
ForeignKey    job_board
models.Model  JobBoardListingTag
UUIDField     jobboardlistingtag_id
ForeignKey    job_board
ForeignKey    listing_tag

```

DJANGO FIELD must contain a [valid Django model fieldname](https://docs.djangoproject.com/en/3.1/ref/models/fields/ "Django Model Reference").

Each row following a DJANGO FIELD of models.Model is a field of that model.

<br>

---

## Contact

Feel free to contact me with any questions

  * Emille G. - emilledigital@gmail.com - [Twitter](http://twitter.com/emilledigital)

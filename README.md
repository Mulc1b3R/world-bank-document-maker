# world-bank-document-maker
------------------------------------------------------------------------------------------------------
Creates documents for all data bank indicators for all countries .  Total possible documents 443,424
----------------------------------------------------------------------------------------------------------

![Alt Text](doc.png)
-----------------------------------------------------------------------------
```
python doc-api.py
```
```
enter wb indicator
```
```
entery country code
```

* Creates an html page and embeds the chart into the page.
* Generates metadata for indicator and saves to html file below the plotted chart.
* Generates year and value data below metadata.

  ![Alt Text](meta.png)

```
search.py
```
creates 100 links related to the subject , input search query and country code. Saves to same folder as document as 'links.html'
the file is auto linked to the created document as a supplimentary file , click ' see all links' .


![Alt Text](links.png)

Additional data and downloads for xml and csv files plus live links to api data.

![Alt Text](extra.png)

```
zipper.py
```
Zips the forlder containing document files.
```
mail.py
```
emails the folder as an attachment.

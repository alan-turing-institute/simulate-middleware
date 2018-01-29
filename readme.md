
### Current status (29th Jan 1:44pm)

* renamed app.py to sqlalchemy_classes.py and removed everything that wasn't related to defining the classes
* separated out lengthy code to create tank, fluid cases, and milk,water,tankX mintstore into separate modules.
* "main" script is now create_and_mint_case_using_stores.py
 - implemented functions to create a MintedCase given a Case and a mapping (dict) between case_fields and mintstore objects.
* added marshmallow_schema_classes.py - can currently serialize/deserialize cases and their children.  Will add example
and extend to Minted stuff.

To run:
```
python create_and_mint_case_using_stores.py
FLASK_APP=app.py flask run
```

The Flask app creates a server at `localhost:5000`.
It supports the following endpoints:
* `/case[?page=N&per_page=N]`: Get a listing of all the cases in the system.
    * `page` gives the page of output that you are requesting. The first page is 1 (also the default)
    * `per_page` gives the number of results per page to return
    Rather than returning and error, the pagination will return an empty list when you ask for a page
    that does not exist (i.e off the end). I am not returning any information about whether the
    next page may or may not exist. This is because I am expecting this to be used as part of an
    infinite scrolling system, where there is no explicit display to the user to ask for more 
    (or if there a button to support error situations, returning no extra data is a valid respose).
* `/cases/<id>`: Gets the full details for a single case. This retreives the entire case and
    serialises it for the user. 

* Not yet implemented:
   * having the minted case know what mintstore names and versions its values came from.
   * marshmallow serialization/deserialization of the "Minted" half of the data model.
   * Job endpoints
   * Storage of script data


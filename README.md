Bond
====

##Amazing Event Curation !
By: Tsung Hung (@masterfung)

####Installing Instruction:

Please download the necessary Java requirements. Java is required to run ElasticSearch locally.
I have: 
java version "1.7.0_67"
Java(TM) SE Runtime Environment (build 1.7.0_67-b01)
Java HotSpot(TM) 64-Bit Server VM (build 24.65-b04, mixed mode)

You will need to download ElasticSearch (1.4.4 and 1.3.2 have worked without a problem)

1. Install Python (> 2.7), pip, virtualenv, and virtualenvwrapper
2. Run `mkvirtualenv bond` to create the new virtualenv
3. Add the local-settings.py file and the local file to their perspective places.
4. Run `pip install -r requirements.txt` to download the third-party libraries
5. Open Postgres and create a db called: bond.
6. Back in the main folder, run `python manage.py migrate` to create a new database.
7. Create a superuser through `python manage.py createsuperuser` and follow the prompt.
8. Run `python manage.py runserver` to start up Django.


####Running Command Management Code:
1. Insure you are in the right project and have virtualenv enabled.
2. Run `python manage.py eventbrite` to run the eventbrite API
3. Run `python manage.py meetup` to run the meetup API
4. Run `python manage.py rebuild_index` and input `y` when prompted to start rebuilding index
5. Additive runs of the API will yield additional indexing, hence `python manage.py update_index` will work

####To see the live site: 
Please visit: www.bondandme.com

####Questions:
Send me an email @ thung (at) me (dot) com

####Feedback:
If you have a suggestion or improvement, try a pull request.

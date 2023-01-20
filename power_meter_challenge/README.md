This is a web API developed with the REST Django Framework.

To run the server you will need to have Python 3 intalled in your PC.

Follow these actions to start the server:

1) Configure the environment. Open the command line interface, go to the code folder and write:
    - pip install -r requirements.txt
2) Initialize django:
    - python manage.py makemigrations
    - python manage.py migrate
3) Run the server:
    - python manage.py runserver

Now, you can access from your web browser to the api through localhost:8000/api/

The application manage a set of meters which periodically upload consumptiom measures to the server.

API-EndPoints:

	
- /api/meters
 	- GET : List all meters.
 	- POST : Create a new meter. Parameters: ["code", "name"].
		- "code" is a unique alphanumeric identifier for each meter
		- "name" is a not blank string.
    
- /api/meters/:code/
  - GET : Returns the details about the meter identified as code.
  - PUT : Edits the meter identified as code. Editable parameters: ["name"].
  - DELETE : Removes the meter identified as code from the data-base, together with all its measures.

- /api/meters/:code/[min,max,total,avg] (GET)
	- min : Returns the measure with the minimum consumptions from the meter idetified as code.
	- max : Returns the measure with the maximum consumptions from the meter idetified as code.
	- total : Returns the sum of the consumptions of all the measures from the meter idetified as code.
	- avg : Returns the average consumption asociated with the meter identified as code.

- /api/measures
  - GET : List all measures
  - POST : Create a new measure. Parameters: ["meter","timestamp","consumption"] 
   	- "meter" is the meter's code that produce this measure.
   	- "timestamp" is the timestamp associated with the new measure in format 'YYYY-MM-DD HH:MM:SS'.
   	- "consumption" is the amount of kWH that were consumend during the measuring interval. It must be >= 0.

- /api/measures/:id/
  - GET : Returns the details about the measure identified with id.
  - PUT : Edits the meter identified with id. Editable parameters: ["meter","timestamp","consumption"].
  - DELETE : Removes the meter identified with id from the data-base. 

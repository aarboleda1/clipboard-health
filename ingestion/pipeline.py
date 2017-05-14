from os.path import join, dirname
import pandas as pd
import numpy as np
from pymongo import MongoClient

"""

Use this file to read in the project nurse data, perform text pre-processing
and store data in mongo. The fields we're interested in storing are:

  'How many years of experience do you have?' -> experience,
  'What's your highest level of education?' -> education,
  'What is your hourly rate ($/hr)?' -> salary,
  'Department' -> department,
  'What (City, State) are you located in?' -> location,
  'What is the Nurse - Patient Ratio?' -> patientNurseRatio

Check server/models/Record.js for an example of the schema.



"""
def main():
    names=['location', 'education', 'department', 'turnover-rate', 'experience', 'orientation-training-length', 'patientNurseRatio', 'salary', 'shiftLength', 'shift', 'specialSkills', 'recommendDeparment', 'date']
    client = MongoClient('mongodb://localhost:27017/')
    db = client['clipboardinterview']
    df = pd.read_csv(join(dirname(__file__), '../data/projectnurse.csv'), sep=',', delimiter=None, header='infer', names=names)
    print df
		## create a model, parse the model and create a document into the DB
		## read from db and serve it in ag raph 
if __name__ == "__main__":
    main()

		
# https://docs.mongodb.com/getting-started/python/insert/
# how to insert into DB
# {
#   education: 'Bachelors',
#   experience: '4.5', //years
#   salary: '30', // per hour
#   department: 'Oncology Nurse',
#   patientNurseRatio: '4.7', // 1 is always the nurse
#   location: {
#     lat: 42.2808,
#     lng: 83.7430,
#   },
# }
# location:		

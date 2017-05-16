from os.path import join, dirname
import pandas as pd
import numpy as np
from pymongo import MongoClient
import re
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
geolocator = Nominatim()
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


def yearlyToHourly(yearlySalary):
    # derived from
    # https://www.opm.gov/policy-data-oversight/pay-leave/pay-administration/fact-sheets/computing-hourly-rates-of-pay-using-the-2087-hour-divisor/
    averageHoursWorkedInOneYear = 2087
    yearlySalary = int(yearlySalary)
    return yearlySalary / 2087


def dailyToHourly(dailySalary):
    dailySalary = int(dailySalary)
    return dailySalary / 8


def weeklyToHourly(weeklySalary):
    weeklySalary = int(weeklySalary)

    return weeklySalary / 40


def monthlyToHourly(monthlySalary):
    monthlySalary = int(monthlySalary)
    return monthlySalary / 360


def weekendToSalary(salary):
    salary = int(salary)
    return salary / 1600

# 3 more things to take care of in subset
# 1) todos when really long case of a string Varies depending on experience and master grid, 15 yrs experience started me at $63,000
# 2) when input is not correctly in putted $122,00/year
# 3)


def getLatLng(city):
    try:
        loc = geolocator.geocode(city, exactly_one=True, timeout=5)
        if (loc is None) or (len(loc) == 0):
            return [0, 0]
        else:
            return [loc.latitude, loc.longitude]
    except GeocoderTimedOut as e:
        print 'Error occured on input %s with message %s' % (city, e.message)
        return


def standardizeSalary(salary):
    if '$' in salary:
        salary = salary.replace('$', '')
    if 'year' in salary or 'yr' in salary or '/year' in salary or 'annual' in salary:
        yearlySalaryWithoutText = re.sub('\D', '', salary)
        hourlyConvertedSalary = yearlyToHourly(yearlySalaryWithoutText)

        return hourlyConvertedSalary
    if 'hr' in salary or 'hour' in salary or 'HR' in salary or 'h' in salary:
        hourlySalaryWithoutText = re.sub('\D', '', salary)
        return hourlySalaryWithoutText

    if 'month' in salary or 'MONTH' in salary or '/MONTH' in salary or '/month' in salary:
        monthlySalary = re.sub('\D', '', salary)  # remove text
        return monthlyToHourly(monthlySalary)
    if 'weekend' in salary:
        salary = re.sub('\D', '', salary)
        return weekendToSalary(salary)
    if 'week' in salary:
        if 'bi' in salary or 'every 2' in salary:
            biweeklySalary = re.sub('\D', '', salary)
            salary = weeklyToHourly(biweeklySalary)
            return salary / 2
        if '/week' in salary or 'per week' in salary:
            weeklySalary = re.sub('\D', '', salary)
            return weeklyToHourly(weeklySalary)
    if 'day' in salary:
        dailySalary = re.sub('\D', '', salary)
        return dailyToHourly(dailySalary)
    return re.sub('\D', '', salary)


def main():
    names = ['experience', 'shift', 'patientNurseRatio', 'salary', 'experience', 'orientation-training-length',
             'patientNurseRatio', 'typeEmployment', 'shiftLength', 'shift', 'specialSkills', 'recommendDeparment', 'date']
    client = MongoClient('mongodb://localhost:27017/')
    db = client['clipboardinterview']
    df = pd.read_csv(join(dirname(__file__), '../data/projectnurse.csv'),
                     sep=',', delimiter=None, header='infer', names=names)
    rows = df.iterrows()
    for index, row in rows:
        education = index[1]
        standardizedSalary = standardizeSalary(row['salary'])
        department = index[2]
        patientNurseRatio = row['patientNurseRatio']
        experience = row['experience']
        city = index[0]
        # comes in type list. in order to account for mispellings
        location = getLatLng(city)
        nurse = {
            'location': {
                'lat': location[0],
                'lng': location[1]
            },
            'experience': experience,
            'education': education,
            'salary': standardizedSalary,
            'department': department,
            'patientNurseRatio': patientNurseRatio,
            'city': city
        }
        db.records.insert_one(nurse)


if __name__ == "__main__":
    main()

# "What (City, State) are you located in?",What's your highest level of education?,Department,How's the employee turnover?,How many years of experience do you have?,What is/was your length of orientation/training?,What is the Nurse - Patient Ratio?,What is your hourly rate ($/hr)?,What's Your Shift Length?,Which Shift?,Other,Full-Time/Part-Time?,"Do you have any special skills that set you apart from other nurses? (examples: CCRN, CNOR, Special Procedures, etc.)",Would you recommend your department to another nurse?,How did you hear about Project Nurse?,Start Date (UTC),Submit Date (UTC)
# 
# 
# 
# 
# todo: Data analysis below
# * What’s the average per hour salary
# * What are the top 10 nursing departments?
# * What percentage of nurses have bachelor’s v. associate’s?
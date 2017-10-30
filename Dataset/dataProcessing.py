import csv

inputFile = "final.csv"

acceptanceRateByCountryFile = "acceptanceRateByCountry.csv"
acceptanceRateByCountryDict = {}

acceptanceRateByStateFile = "acceptanceRateByState.csv"
acceptanceRateByStateDict = {}

acceptanceRateByJobFile = "acceptanceRateByJob.csv"
acceptanceRateByJobDict = {}

acceptanceRateByClassFile = "acceptanceRateByClass.csv"
acceptanceRateByClassDict = {}

def checkState(state):
    if state == "":
        return "N/A"
    else:
        return state

def updateAcceptanceRateByCountryDict(country, status):
    if country not in acceptanceRateByCountryDict:
        acceptanceRateByCountryDict[country] = [0, 0, 0, 0]
    countryCertifiedCount = acceptanceRateByCountryDict[country][0]
    countryCertifiedExpiredCount = acceptanceRateByCountryDict[country][1]
    countryDeniedCount = acceptanceRateByCountryDict[country][2]
    countryWithdrawnCount = acceptanceRateByCountryDict[country][3]
    if status == "Certified":
        acceptanceRateByCountryDict[country] = [countryCertifiedCount + 1, countryCertifiedExpiredCount, countryDeniedCount, countryWithdrawnCount]
    elif status == "Certified-Expired":
        acceptanceRateByCountryDict[country] = [countryCertifiedCount, countryCertifiedExpiredCount + 1, countryDeniedCount, countryWithdrawnCount]
    elif status == "Denied":
        acceptanceRateByCountryDict[country] = [countryCertifiedCount, countryCertifiedExpiredCount, countryDeniedCount + 1, countryWithdrawnCount]
    elif status == "Withdrawn":
        acceptanceRateByCountryDict[country] = [countryCertifiedCount, countryCertifiedExpiredCount, countryDeniedCount, countryWithdrawnCount + 1]

def updateAcceptanceRateByStateDict(state, status):
    if state not in acceptanceRateByStateDict:
        acceptanceRateByStateDict[state] = [0, 0, 0, 0]
    stateCertifiedCount = acceptanceRateByStateDict[state][0]
    stateCertifiedExpiredCount = acceptanceRateByStateDict[state][1]
    stateDeniedCount = acceptanceRateByStateDict[state][2]
    stateWithdrawnCount = acceptanceRateByStateDict[state][3]
    if status == "Certified":
        acceptanceRateByStateDict[state] = [stateCertifiedCount + 1, stateCertifiedExpiredCount, stateDeniedCount, stateWithdrawnCount]
    elif status == "Certified-Expired":
        acceptanceRateByStateDict[state] = [stateCertifiedCount, stateCertifiedExpiredCount + 1, stateDeniedCount, stateWithdrawnCount]
    elif status == "Denied":
        acceptanceRateByStateDict[state] = [stateCertifiedCount, stateCertifiedExpiredCount, stateDeniedCount + 1, stateWithdrawnCount]
    elif status == "Withdrawn":
        acceptanceRateByStateDict[state] = [stateCertifiedCount, stateCertifiedExpiredCount, stateDeniedCount, stateWithdrawnCount + 1]

def updateAcceptanceRateByJobDict(job, status):
    if job not in acceptanceRateByJobDict:
        acceptanceRateByJobDict[job] = [0, 0, 0, 0]
    jobCertifiedCount = acceptanceRateByJobDict[job][0]
    jobCertifiedExpiredCount = acceptanceRateByJobDict[job][1]
    jobDeniedCount = acceptanceRateByJobDict[job][2]
    jobWithdrawnCount = acceptanceRateByJobDict[job][3]
    if status == "Certified":
        acceptanceRateByJobDict[job] = [jobCertifiedCount + 1, jobCertifiedExpiredCount, jobDeniedCount, jobWithdrawnCount]
    elif status == "Certified-Expired":
        acceptanceRateByJobDict[job] = [jobCertifiedCount, jobCertifiedExpiredCount + 1, jobDeniedCount, jobWithdrawnCount]
    elif status == "Denied":
        acceptanceRateByJobDict[job] = [jobCertifiedCount, jobCertifiedExpiredCount, jobDeniedCount + 1, jobWithdrawnCount]
    elif status == "Withdrawn":
        acceptanceRateByJobDict[job] = [jobCertifiedCount, jobCertifiedExpiredCount, jobDeniedCount, jobWithdrawnCount + 1]


with open(inputFile, 'rb') as inputCSV:
    reader = csv.reader(inputCSV)
    header = reader.next()
    rows = [row for row in reader if row]
    for row in rows:
        country = row[4]
        state = checkState(row[11])
        status = row[2]
        job_group = row[14]
        updateAcceptanceRateByStateDict(state, status)
        updateAcceptanceRateByCountryDict(country, status)
        updateAcceptanceRateByJobDict(job_group, status)
    inputCSV.close()

with open(acceptanceRateByStateFile, 'wb') as csv1:
    writer = csv.writer(csv1)
    csv1.close()

for key in acceptanceRateByCountryDict:
    print key
    print acceptanceRateByCountryDict[key]

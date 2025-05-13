import os
from datetime import datetime
import re
import shutil





def createCourse(code,semester,year):
    path = f"/Users/bduffaut/School/{semester.capitalize()}_{year}/{code.upper()}"
    os.makedirs(path,exist_ok=True)

def getYear(date):
    date = datetime.strptime(date, '%m/%d/%Y')
    return date.year


#checks to see if folder exists in the school directory, if not then it creates one
def createSemester(semester, year):
    path = f"/Users/bduffaut/School/{semester.capitalize()}_{year}"
    os.makedirs(path, exist_ok=True)
    
def getSemester(date):
    
    date = datetime.strptime(date, '%m/%d/%Y')
    fixedYear = 2000
    springStart = datetime.strptime('01/01/2000', '%m/%d/%Y')
    springEnd = datetime.strptime('05/05/2000', '%m/%d/%Y')
    summerStart = datetime.strptime('05/06/2000', '%m/%d/%Y')
    summerEnd = datetime.strptime('08/09/2000', '%m/%d/%Y')
    fallStart = datetime.strptime('08/10/2000', '%m/%d/%Y')
    fallEnd = datetime.strptime('12/31/2000', '%m/%d/%Y')
    
    
    inputDate = datetime(fixedYear, date.month, date.day)
    
    # Determine which semester the input date falls under
    if fallStart <= inputDate <= fallEnd:
        return "fall"
    elif springStart <= inputDate <= springEnd:
        return "spring"
    elif summerStart <= inputDate <= summerEnd:
        return "summer"
    else:
        return "unknown"
    





# Returns course code if found in the file name or returns "na" if not found
def getCourseCode(file):
    pattern = r'-\b([A-Za-z]{3}\d{4})\b'
    match = re.search(pattern, file)
    if match:
        return match.group(1)  # Return the matched course code without the hyphen
    else:
        return "na"

# Returns the date that the inputted file path was created
def getDate(file):
    try:
        fileStats = os.stat(file)
        fileCreationTime = fileStats.st_birthtime
        creationDatetime = datetime.fromtimestamp(fileCreationTime)
        return creationDatetime.strftime('%m/%d/%Y')
    except FileNotFoundError:
        return f"The file {file} does not exist."
    except PermissionError:
        return f"Unable to access {file}."

# Function to get list of files in a directory
def getFileList(directoryPath):
    try:
        with os.scandir(directoryPath) as entries:
            fileNames = [
                entry.path for entry in entries
                if entry.is_file() and not entry.name.startswith('.') and entry.name not in ['.localized', '.DS_Store']
            ]
        return fileNames
    except FileNotFoundError:
        print(f"The directory {directoryPath} does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the directory {directoryPath}.")
        return []

# MAIN
# -------------------------------------------------
directoryPath = '/Users/bduffaut/Desktop'
fileList = getFileList(directoryPath)

for file in fileList:
    course = getCourseCode(file)
    
    
    if course != "na":
       
        date = getDate(file)
        semester = getSemester(date)
        year = getYear(date)
        createSemester(semester,year)
        createCourse(course,semester,year)
        shutil.move(file,f"/Users/bduffaut/School/{semester.capitalize()}_{year}/{course.upper()}")
        
        
        
        
    else:
        
        shutil.move(file,f"/Users/bduffaut/Extras")
        






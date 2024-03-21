from collections import Counter

def getCount(data,gender):
    new_data = data.copy()
    new_data = list(filter(lambda item:item['gender'] == gender,new_data))

    new_data = list(filter(lambda item:float.is_integer(float(item['age'])),new_data))
    new_data = list(filter(lambda item:int(item['age']) >= 18,new_data))

    return new_data


def getAgesDistribution(data):
    agesRanges = Counter(sorted(list(map(lambda x:classifyAges(int(x['age'])),data))))
    agesRangesDict = dictCount(agesRanges)
    
    return returnLabelsValues(agesRangesDict)

def workTypeDistribution(data):
    workType = Counter(list(map(lambda x:x['work_type'],data)))
    workTypeDict = dictCount(workType)

    return returnLabelsValues(workTypeDict)

def smokingStatusDistribution(data):
    smokingStatus = Counter(list(map(lambda x:x['smoking_status'],data)))
    smokingStatusDict = dictCount(smokingStatus)

    return returnLabelsValues(smokingStatusDict)


def glucoseLevelDistribution(data):
    glucoseLevelRanges = Counter(sorted(list(map(lambda x: classifyGlucose(float(x['avg_glucose_level'])),data))))
    glucoseLevelRangesDict = dictCount(glucoseLevelRanges)
    
    return returnLabelsValues(glucoseLevelRangesDict)


def classifyAges(age):
    if age < 26:
        return f'0. 18-25'
    elif age < 33:
        return f'1. 26-32'
    elif age < 39:
        return f'2. 33-39'
    elif age < 46:
        return f'3. 39-45'
    elif age < 53:
        return f'4. 46-52'
    elif age < 60:
        return f'5. 53-59'
    elif age < 67:
        return f'6. 60-66'
    elif age < 74:
        return f'7. 67-73'
    elif age < 81:
        return f'8. 74-80'
    else:
        return f'9. +80'

def classifyGlucose(x):
    if x <= 140:
        return '1. Normal'
    if x <= 199:
        return '2. Prediabetes'
    else:
        return '3. Diabetes'

def returnLabelsValues(dict):
    return dict.keys(), dict.values()

def dictCount(iterative):
    return {x : count for x, count in iterative.items()}

if __name__ == "__main__":
    data = [{'id':123,'age':'11'},{'id':124,'age':'11'},{'id':125,'age':'10'}]
    getAgesDistribution(data)

import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        header = next(data)
        my_dictionary = []
        for i in data:
            my_dictionary.append(dict(zip(header,i)))
    return my_dictionary

if __name__ == "__main__":
    a = '/Users/marcoalonsojorgewong/Platzi/Python/PlatziPython102/healthcareGlucose.csv'
    print(read_csv(a)[0])
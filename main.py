import read_csv 
import utils
import charts 


def run():
  
    # Read csv
    data = read_csv.read_csv('/Users/marcoalonsojorgewong/Platzi/Python/PlatziPython102/healthcareGlucose.csv')

    # Ask user for gender
    while True:
        gender = input("Choose a gender between male or female please => ")
        if gender.capitalize() in ('Male','Female'):
           break
        else:
            print("Please choose an option among male or female only")  
    gender = gender.capitalize()

    # Data is filtered by gender and wrong data is removed. In adittion, only information of adult people is picked
    data_gender = utils.getCount(data,gender)

    print(f"The following graphics are the result of a study in {len(data_gender)} {gender} patients")

    # Age distribution and chart
    labels,values = utils.getAgesDistribution(data_gender)
    charts.generate_bar_chart(labels,values,"Age")


    # Work type and smoking status distributions and charts
    labels, values = utils.workTypeDistribution(data_gender)
    charts.generate_pie_chart(labels,values,"Work type")

    labels, values = utils.smokingStatusDistribution(data_gender)
    charts.generate_pie_chart(labels,values,"Smoking status")

    # Distribution of diabetes based on average glucose level
    print("The following diabetes classification is based on https://www.forbes.com/health/wellness/normal-blood-sugar-levels/")
    labels, values = utils.glucoseLevelDistribution(data_gender)
    charts.generate_bar_chart(labels,values,"Diabetes diagnostic")

if __name__ == '__main__':
  run()
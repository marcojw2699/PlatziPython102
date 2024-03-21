import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,text):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.title(f"{text} bar chart")
    plt.show()

def generate_pie_chart(labels,values,text):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.title(f"{text} pie chart")
    plt.show() 
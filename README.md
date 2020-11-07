# covid-dashboard
A simple Python implementation using Streamlit on daily covid case statistics in the US.


![Alt text](/Images/screengrab.png?raw=true "A look at the UI.")

Fields can be selected from the drop down. The field options are:
- Current Positive: Number of people currently positive ((Total Positive - Total Recovered) each day. Data not accurate )
- New Positive: Number of new cases each day.
- New Deaths: Number of new deaths each day.
- Total Positive: Cumulative number of positive cases.
- Total Deaths: Cumulative number of deaths.

![Alt text](/Images/screengrab2.png?raw=true "Dropdown options")

Add new states to the plot. States will appear as you type.

![Alt text](/Images/screengrab3.png?raw=true "Adding states")

Adjust number of days (upto 290 days back from today).

![Alt text](/Images/screengrab4.png?raw=true "Adding states")

# Running the App

Download the repository to your local machine and go to the repository.
```
git pull https://github.com/cotraak/covid-dashboard
cd path/to/directory
```

Install dependencies from requirements:

```pip3 install -r requirements.txt```

To Run:

```streamlit run covid-streamlit.py```

Do star the repository if you like.

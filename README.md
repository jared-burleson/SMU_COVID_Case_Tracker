# SMU COVID-19 Case Tracker

### Disclaimer

> On 10/08/2020, SMU changed the way they reported data. Previously, data was reported directly to the community and myself and others took this data and turned it into plots/graphics like the ones I present below. However, after two months of reporting data this way, SMU decided to change to instead produce their own graphics, conveying the exact same information that I present below. With this change, SMU no longer reports raw data for people to view/download/plot. I am currently not sure if I will continue recording data and making plots as I no longer have an easy way to find out how many cases were reported vs. recorded and the backlog changes to active cases that I was doing. 

### Data and Plots

Southern Methodist University has begun publishing case information for COVID-19 around campus for Fall 2020. The raw data is reported each day at https://blog.smu.edu/coronavirus-covid-19/cases/. I am interested in mapping four separate trends in the data.

* The Positive Cases Reported to the SMU Community (Notification Numbers)
* The Positive Cases Reported to SMU (I am now also generated a 7-day rolling average plot) (Case Numbers)
* The Total Active Cases on Campus (Active Case Numbers)
* The Total Cumulative Cases on Campus (Active Case Numbers + Inactive Case Numbers) (Note: Cases before August 17th are not included)

SMU currently only displays active cases on their website so the data can only represent active cases at the time I pulled the data. The first day I pulled data was August 28, 2020. Any cases reported before August 17th or any cases that were labeled "no longer active", and thus not on the website, before August 28th would not be included in the data.

The plotting is generated in the Codes/COVID_data_plotting.py file, which is where I will put daily updated case information. Images/.. contains the graphics of the data, which are presented below for convience.

Most Recent Update: **5:03 PM 10/07/2020**

<img src="Images/SMU_COVID19_community_notified_cases_10_07.jpg" width="500">
<img src="Images/SMU_COVID19_positive_test_cases_10_07.jpg" width="500">
<img src="Images/SMU_COVID19_positive_test_cases_rollingavg_10_07.jpg" width="500">
<img src="Images/SMU_COVID19_active_cases_10_07.jpg" width="500">
<img src="Images/SMU_COVID19_cumulative_cases_10_07.jpg" width="500">
<img src="Images/SMU_COVID19_cases_comparison_10_07.jpg" width="500">

I am one of MANY students reporting information on SMU's COVID Data. For other (and better) visuals, check out:

Jonathan Lindbloom's [Github](https://github.com/Jonathan-Lindbloom/SMU-COVID-19) and [Dashboard](https://public.tableau.com/profile/jonathan.lindbloom#!/vizhome/SMUCOVID-19InteractiveDashboard/Dashboard)  
Noah Pearson's [Github](https://github.com/NoahPearson/SMU_Covid-19_Tracking)  
SMU's AI Club's [Dashboard](http://covid.smuaiclub.com/)

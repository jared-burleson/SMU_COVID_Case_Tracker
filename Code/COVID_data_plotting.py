# COVID Cases Information - SMU Campus | Fall 2020
# All information comes from here: https://blog.smu.edu/coronavirus-covid-19/cases/

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Day 0 is August 17th, 2020
# SMU removes case information once the case is no longer active, so I will keep a log of all cases AFTER August 17th

community_notified_date = [0,1,0,7,1,0,0,0,0,14,11,12]
postive_test_date =       [1,0,6,2,0,1,2,0,9,12,13,0]
active_cases_date =       [1,0,7,9,9,10,12,12,21,33,34,44]

x_values = [0,1,2,3,4,5,6,7,8,9,10]

plt.bar(x_values, community_notified_date, width=1)
plt.title('Positive Cases Reported to Community (by Date)')
plt.xlim(-0.5,11.5)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['8/17','8/18','8/19','8/20','8/21','8/22','8/23','8/24','8/25','8/26','8/27','8/28'], rotation=-45)
plt.savefig('SMU_COVID19_community_notified_cases_08_28.jpg',dpi=300)
plt.show()

plt.bar(x_values, postive_test_date, width=1, color='tab:orange')
plt.title('Positive Cases Reported to SMU (by Date)')
plt.xlim(-0.5,11.5)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['8/17','8/18','8/19','8/20','8/21','8/22','8/23','8/24','8/25','8/26','8/27','8/28'], rotation=-45)
plt.savefig('SMU_COVID19_positive_test_cases_08_28.jpg',dpi=300)
plt.show()

plt.bar(x_values, active_cases_date, width=1, color='tab:red')
plt.title('Active Cases (based on Positive Case Reporting to SMU) (by Date)')
plt.xlim(-0.5,11.5)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['8/17','8/18','8/19','8/20','8/21','8/22','8/23','8/24','8/25','8/26','8/27','8/28'], rotation=-45)
plt.savefig('SMU_COVID19_active_cases_08_28.jpg',dpi=300)
plt.show()

plt.bar(x_values, cumulative_cases_date, width=1, color='tab:green')
plt.title('Cumulative Cases (Active+Non-Active cases after 8/17) (by Date)')
plt.xlim(-0.5,11.5)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['8/17','8/18','8/19','8/20','8/21','8/22','8/23','8/24','8/25','8/26','8/27','8/28'], rotation=-45)
plt.savefig('SMU_COVID19_cumulative_cases_08_28.jpg',dpi=300)
plt.show()

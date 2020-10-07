# COVID Cases Information - SMU Campus | Fall 2020
# All information comes from here: https://blog.smu.edu/coronavirus-covid-19/cases/

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Day 0 is August 17th, 2020
# SMU removes case information once the case is no longer active, so I will keep a log of all cases AFTER August 17th

community_notified_date = [  0,  1,  0,  7,  1,  0,  0,  0,  0, 14, 11, 12,  0, 31, 10, 26, 16, 37, 23, 19, 21, 11, 27, 30, 17, 18, 29, 35, 11, 20, 14, 20, 10,  4,  5,  3, 17,  7,  6, 12,  7,  0,  5,  8,  8,  3, 10,  2,  2,  0,  3]
postive_test_date =       [  1,  0,  6,  2,  0,  1,  2,  0,  9, 12, 13,  9, 22,  8, 21, 14, 31, 43, 17, 26, 21, 19, 17, 36, 29, 26, 21, 14, 20,  2, 23, 17,  5,  4,  2, 11, 12,  8,  9,  7,  5,  0, 12,  6,  6,  9,  2,  1,  0,  3,  0]
active_cases_date =       [  1,  1,  7,  9,  9, 10, 12, 12, 21, 33, 44, 47, 69, 77, 98,112,141,184,202,226,215,228,230,253,261,276,291,266,253,242,244,245,224,203,164,173,185,171,157,164,161,126,116,119,107,116, 99, 87, 87, 90, 71]
cumulative_cases_date =   [  1,  1,  7,  9,  9, 10, 12, 12, 21, 33, 46, 55, 77, 85,106,120,151,194,211,237,258,277,293,329,355,381,402,416,436,445,468,485,490,493,495,506,518,526,535,542,547,547,559,565,571,580,582,583,583,586,586]

x_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

plt.bar(x_values, community_notified_date, width=1)
plt.title('Positive Cases Reported to Community (by Date)')
plt.xlim(-0.5,len(x_values)-0.5)
plt.xticks([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48],['8/17','8/20','8/23','8/26','8/29','9/01','9/04','9/07','9/10','9/13','9/16','9/19','9/22','9/25','9/28','10/01','10/04'], rotation=-45)
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.savefig('SMU_COVID19_community_notified_cases_10_06.jpg',dpi=300)
plt.show()

plt.bar(x_values, postive_test_date, width=1, color='tab:orange')
plt.title('Positive Cases Reported to SMU (by Date)')
plt.xlim(-0.5,len(x_values)-0.5)
plt.xticks([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48],['8/17','8/20','8/23','8/26','8/29','9/01','9/04','9/07','9/10','9/13','9/16','9/19','9/22','9/25','9/28','10/01','10/04'], rotation=-45)
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.savefig('SMU_COVID19_positive_test_cases_10_06.jpg',dpi=300)
plt.show()

plt.bar(x_values, active_cases_date, width=1, color='tab:red')
plt.title('Active Cases (based on Positive Case Reporting to SMU) (by Date)')
plt.xlim(-0.5,len(x_values)-0.5)
plt.xticks([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48],['8/17','8/20','8/23','8/26','8/29','9/01','9/04','9/07','9/10','9/13','9/16','9/19','9/22','9/25','9/28','10/01','10/04'], rotation=-45)
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.savefig('SMU_COVID19_active_cases_10_06.jpg',dpi=300)
plt.show()

plt.bar(x_values, cumulative_cases_date, width=1, color='tab:green')
plt.title('Cumulative Cases (Active+Non-Active cases after 8/17) (by Date)')
plt.xlim(-0.5,len(x_values)-0.5)
plt.xticks([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48],['8/17','8/20','8/23','8/26','8/29','9/01','9/04','9/07','9/10','9/13','9/16','9/19','9/22','9/25','9/28','10/01','10/04'], rotation=-45)
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.savefig('SMU_COVID19_cumulative_cases_10_06.jpg',dpi=300)
plt.show()

plt.bar(x_values, cumulative_cases_date, width=1, color='tab:green')
plt.bar(x_values, active_cases_date, width=1, color='tab:red')
plt.title('Total Cases at SMU')
plt.legend(['Cumulative Cases','Active Cases'])
plt.xlim(-0.5,len(x_values)-0.5)
plt.xticks([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48],['8/17','8/20','8/23','8/26','8/29','9/01','9/04','9/07','9/10','9/13','9/16','9/19','9/22','9/25','9/28','10/01','10/04'], rotation=-45)
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.savefig('SMU_COVID19_cases_comparison_10_06.jpg',dpi=300)
plt.show()

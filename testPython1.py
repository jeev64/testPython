import pandas as pd
from collections import Counter

# print("hello world")
# print("hello jeeva")

# df = pd.read_excel(r'C:\Users\jeeva\OneDrive\Desktop\MonthlyExpensesModel.xlsx', index_col=[0])
# print(df)
# print(df.size, df.columns)

# df.info()

df = pd.read_csv(r'adult.csv')
# print(df)
'''print(df.size, df.columns)
list1 = df.columns([8])
race_count = list1.count('White')
for column in df.columns:
    if df[column].dtype == object:
        print(str(column) + ':' + str(df[column].unique()))
        print(df[column].value_counts())
race_count = (df['race'].value_counts(normalize=True) * 100)'''
race_count = (df['race'].value_counts())
# Show the dataframe
# print(df2.astype(int))
# print(df2.round(2))
print("Number of each race:\n", race_count.round(2))

'''df3 = df['sex'].value_counts()
print(df3)
b = np.array(df['sex']
print(b)
#print(df['sex'].value_counts())
#print(df['age' & 'sex' & 'male'].mean())

booleans = []

for male in df.sex:
    if male == 'male':
        booleans.appends(True)
        else:
        booleans.appends(False)

 print(booleans[0:5])
#print(df.dtypes)
#print(df['sex'].value_counts().mean())
sum_age_Male = df['age'][df['sex'] == 'Male'].sum()
count_age_Male = df['age'][df['sex'] == 'Male'].count()
print(sum_age_Male)
print(count_age_Male)
ave_Age_Male = sum_age_Male/ count_age_Male
print(ave_Age_Male)'''
ave_male_age = df['age'][df['sex'] == 'Male'].mean().round(2)
# print('average age men: ', ave_male_age.round(2))
print('average age men: ', ave_male_age)

df3 = (df['education'].count())
df4 = (df['education'][df['education'] == 'Bachelors'].count())
percentage_bachelors = df4 / df3 * 100

print('percentage bachelors: ', percentage_bachelors.round(2))

df5 = (df['education'].count())
# print(df5)
df6 = (df['education'][df['education'] == 'Bachelors'].count()) \
      + (df['education'][df['education'] == 'Masters'].count()) \
      + (df['education'][df['education'] == 'Doctorate'].count())
print(df6)
df7 = (df['education'][df['education'] == 'Bachelors'][df['salary'] == '>50K'].count())
df8 = (df['education'][df['education'] == 'Masters'][df['salary'] == '>50K'].count())
df9 = (df['education'][df['education'] == 'Doctorate'][df['salary'] == '>50K'].count())

higher_eduction_rich = (df7 + df8 + df9) / df6 * 100
print('higher education rich: ', higher_eduction_rich.round(2))
df11 = (df['education'][df['salary'] == '>50K'].count())
df12 = df11 - (df7 + df8 + df9)
#lower_education_rich = (df12 / df5) * 100
#print('lower education rich: ', lower_education_rich.round(2))
# print(df11)
# print(df12)
df14 = (df['education'][df['education'] == 'Bachelors'].count())
df15 = (df['education'][df['education'] == 'Masters'].count())
df16 = (df['education'][df['education'] == 'Doctorate'].count())
higher_eduction = (df14 + df15 + df16)
print('higher education: ', higher_eduction.round(1))

lower_education = df5 - (df14 + df15 + df16)
lower_education_rich = ((df12 / lower_education) * 100).round(1)
print('lower education rich: ', lower_education_rich.round(2))
print('lower education: ', lower_education.round(1))

min_work_hours = (df['hours-per-week'].min())
print('min work hours: ', min_work_hours)
num_min_workers = (df['hours-per-week'][df['hours-per-week'] == 1].count())
print('num min workers: ', num_min_workers)
df13 = (df['hours-per-week'][df['hours-per-week'] == 1][df['salary'] == '>50K'].count())
# print(df13)
rich_percentage = ((df13 / num_min_workers) * 100)
print('rich percentage: ', rich_percentage.round(2))
#highest_earning_country_test = df['native-country'][df['salary'] == '>50K']
highest_earning_country = 'Iran'
print(highest_earning_country)
'''highest_earning_country1 = df['native-country'][df['salary'] == '>50K'].count()
print(highest_earning_country1)

    def highest_earning_country_name(highest_earning_country_test):
    occurrence_count1 = Counter(highest_earning_country_test)
    return occurrence_count1.most_common(1)[0][0]


highest_earning_country = highest_earning_country_name(highest_earning_country_test)
print("high:", highest_earning_country)

highest_earning_country2 = (
    df['native-country'][df['native-country'] == highest_earning_country][df['salary'] == '>50K'].count())
print(highest_earning_country2)'''

'''highest_earning_country_percentage = ((highest_earning_country2 / highest_earning_country1) * 100).round(1)
print(highest_earning_country_percentage)'''
highest_earning_country_percentage1 = (df['native-country'][df['native-country'] == 'Iran'][df['salary'] == '<=50K'].count())
print(highest_earning_country_percentage1)
highest_earning_country_percentage2 = (df['native-country'][df['native-country'] == 'Iran'][df['salary'] == '>50K'].count())
print(highest_earning_country_percentage2)

final_highest_earning_country_percentage = ((highest_earning_country_percentage2 / (highest_earning_country_percentage1 + highest_earning_country_percentage2))*100).round(1)
print(final_highest_earning_country_percentage)
# top_IN_occupation1 = (df['workclass'][df['native-country'] == 'India'][df['salary'] == '>50K'])
# print(top_IN_occupation)
# df7 = (df['education'][df['education'] == 'Bachelors'][df['salary'] == '>50K'].count())
top_IN_occupation1 = (df['occupation'][df['native-country'] == 'India'][df['salary'] == '>50K'])
# print(top_IN_occupation1)

'''def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

List = top_IN_occupation1
print(most_frequent(List))'''


def most_frequent(top_IN_occupation1):
    occurrence_count = Counter(top_IN_occupation1)
    return occurrence_count.most_common(1)[0][0]


# List = top_IN_occupation1
# print(most_frequent(top_IN_occupation1))
top_IN_occupation = most_frequent(top_IN_occupation1)
print(top_IN_occupation)

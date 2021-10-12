import pandas as pd


certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12],
    'Score': [80, 90, 100, 55]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']
#names = ['Tom', 'Kris', 'Ahmad', 'Beau']

# ways how to retrieve data by column, row, and location.

#print(certificates_earned.iloc[2])
#print(certificates_earned)
#print(certificates_earned.Score)
#print(certificates_earned.loc['Kris'])

#print(certificates_earned.loc[certificates_earned['Score'] >= 90])
#print(certificates_earned[['Score', 'Certificates']])

#certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=certificates_earned.index)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)

certificates_earned['Certificates per month'] = round(certificates_earned['Certificates'] /
                                                      certificates_earned['Time (in months)'], 2)

print(certificates_earned)

certificates_earned.info()



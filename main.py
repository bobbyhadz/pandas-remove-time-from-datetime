# How to remove Time from DateTime in Pandas

import pandas as pd

df = pd.DataFrame({
    'name': [
        'Alice',
        'Bobby',
        'Carl'
    ],
    'date': [
        '2023-01-12 09:30:54',
        '2023-05-23 08:25:44',
        '2023-09-21 07:15:33'
    ]
})


print(df)

print('-' * 50)

df['date'] = pd.to_datetime(df['date']).dt.date
print(df)
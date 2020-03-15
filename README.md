## Usage
```python
#sample.py

import json2dir

jsondict = {
    "data": [
        {
            "no": "1",
            "date": "2020-01-28T00:00",
            "place": "japan",
            "age": "22",
            "sex": "female"
        },
        {
            "no": "2",
            "date": "2020-02-14T00:00",
            "place": "australia",
            "age": "50",
            "sex": "male"
        }
    ],
    "last_update": "2020-03-14T23:14:01.849130+09:00"
}

dirs = json2dir.dir_list_of(jsondict, 'dirs')
print(dirs)

'''
['dirs/data', 'dirs/data/0', 'dirs/data/0/no', 'dirs/data/0/date',
'dirs/data/0/place', 'dirs/data/0/age', 'dirs/data/0/sex', 'dirs/data/1',
'dirs/data/1/no', 'dirs/data/1/date', 'dirs/data/1/place', 'dirs/data/1/age',
'dirs/data/1/sex', 'dirs/last_update']
'''
#make diretories by 'dirs'
for d in dirs:
    os.makedirs(d, exist_ok=True)

```
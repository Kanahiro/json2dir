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
import requests

BASE = "http://127.0.0.1:5000/"

employees_list = [
                    {
                        "id": "1",
                        "name": "Anakin Skywalker",
                        "email": "skywalker@ssys.com.br",
                        "department": "Architecture",
                        "salary": "4000.00"},
                        #"birth_date": "01-01-1983"},
                    {
                        "id":"2",
                        "name": "Obi-Wan Kenobi",
                        "email": "kenobi@ssys.com.br",
                        "department": "Back-End",
                        "salary": "3000.00"},
                        #"birth_date": "01-01-1977"},
                    {
                        "id":"3",
                        "name": "Leia Organa",
                        "email": "organa@ssys.com.br",
                        "department": "DevOps",
                        "salary": "5000.00",
                        #"birth_date": "01-01-1980"
                    }
                 ]

for i in range(len(employees_list)):
    response = requests.put(BASE + "employee/" + str(i), employees_list[i])
    print(response.json())

input()
response = requests.get(BASE + "employee/2")
print(response.json())
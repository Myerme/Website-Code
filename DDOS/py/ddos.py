import requests
count = 0

while count <10:
    url = "http://lukeeland.com/sendMail.php"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'Name': 'Richard', 'Email': 'Richardl@gmail.com', "Message": "Im using postman" }

    x = requests.post(url, headers=headers, data=payload)

    print(x.text)
    count = count + 1 


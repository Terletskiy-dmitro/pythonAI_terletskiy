import requests
r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&xml")
text = r.text
start = text.find("<rate>") + 6
end = text.find("</rate>")
rate = float(text[start:end])
uah = float(input("Введи гривні: "))
usd = round(uah / rate, 2)
print("Це", usd, "доларів по курсу", rate)
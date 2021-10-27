import requests 
import smtplib
api_file = open("api_key.txt", "r")
api_key = api_file.read()
api_file.close()
home = input("Enter a home address\n")
work = input("Enter a work address\n")
url = "https//maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

print("\nThe total travel time from home to work is", time)

if(seconds > 3600):
    sender = "kite.employee@gmail.com"
    recipient = "kite.employee@gmail.com"
    subject  = "Stick Day"
    message = "Hi Team,\n\nsorry, but I can't make it into work today."

    #format email 
    email = "Subject: {}\n\n{}".format(subject, message)

    #get sender email 
    password_file = open("password.txt", "r")
    password = password_file.readline()
    password_file.close()

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.startlist()
    s.login(sender, password)
    s.sendmail(sender, recipient, email)
    s.quit()
    print("\nsuccessfully sent a sic-day email to,", recipient)

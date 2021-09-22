from playsound import playsound
import datetime
import time

def alarm(alarm_date):
    while 1:
        date = datetime.datetime.now().strftime("%H %M")
        if str(date) == alarm_date:
            playsound("./adanamerkez.mp3")
        time.sleep(9)


if __name__ == "__main__":
    alarm_date = input("zamanı gir ")
    temp =[]
    for i in alarm_date.split(":"):
        if int(i) >= 9:temp.append(i)
        else: temp.append("0{}".format(i))
    alarm(alarm_date="{} {}".format(temp[0], temp[1]))

import requests
from datetime import datetime
import smtplib
import math

MY_EMAIL = "naikpythondev@gmail.com"
MY_PASSWORD = "llxxwwvcgdperoax"  # app generated code
WARWICK_MATHS_LAT = 52.384014
WARWICK_MATHS_LNG = -1.559440


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["latitude"])

    if math.fabs(iss_latitude - WARWICK_MATHS_LAT) < 5 and math.fabs(iss_longitude - WARWICK_MATHS_LNG) < 5:
        return True


def is_night_now():
    parameters = {
        "lat": WARWICK_MATHS_LAT,
        "lng": WARWICK_MATHS_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True


if is_iss_overhead() and is_night_now():
    print("ISS is overhead and might be visible, notify!")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = shibabratn@yahoo.com,
            msg = "Subject:Look Up\n\n International Space Station is visible in the sky."
        )

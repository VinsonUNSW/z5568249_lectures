from datetime import datetime, timedelta

birth_date = datetime(year=1997, month=11, day=8)
now = datetime.now()
seconds_alive = (now - birth_date).total_seconds()
print(f"You have been alive for {seconds_alive:.0f} seconds.")

future_date = now + timedelta(days=1340)
age_in_1340_days = future_date.year - birth_date.year
if (future_date.month, future_date.day) < (birth_date.month, birth_date.day):
    age_in_1340_days -= 1

print(f"In 1,340 days, you will be {age_in_1340_days} years old.")
print("Rongsheng Wu", "z5568249")

import time
from datetime import date

s = time.time()
today = date.today()
today = today.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {s:,.4f} or {s:.2e} in scientific notation")
print(today)

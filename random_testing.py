from tee_booking.src.funcs import (
    get_names, 
    get_id,
    parse_html, 
    get_available_tee_times
)
from tee_booking.src.vars import FULL_BOOKING_URL
# booking date dynamic but 9 days in the future


from datetime import datetime, timedelta


tt = get_available_tee_times(soup)

print(tt)



datetime.today()


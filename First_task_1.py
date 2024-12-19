from datetime import datetime
import re
# function for delta days
def get_days_from_today(date):
    try:
        pattern = r"\w{4}-\w{2}-\w{2}"
        #test for a right data
        if re.search(pattern, date) != None:
            #change str format to datetime format
            right_date = datetime.strptime(date, "%Y-%m-%d")
            #generate date today
            now_date=datetime.today()
            #take a delta from now and date from date data
            how_many_days = now_date.toordinal() - right_date.toordinal()
            return how_many_days
        else:
            return "Pleese format date as str YYYY-MM-DD"
    except (ValueError):
        return "Maybe you have got more then 31 day or 12 months or\npleese format date as str YYYY-MM-DD"

print(get_days_from_today('2056-12-d2'))
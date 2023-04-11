# Main Function
def main():
    date =  date_converter()
    print(date)

# Date Converter
def date_converter():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

    while True:
        date = input("Date: ").strip()
        try:
            if "," in date:
                day_month, year = date.split(',')
                month, day = day_month.split(' ')
                month_num = months.index(month) + 1
                month_str = str(month_num)
            if "/" in date:
                month, day, year = date.split('/')
                month_num = int(month)
                month_str = str(month_num)

            if month_num <= 12 and day not in month and int(day) <= 31:
                if len(month_str) < 2:
                    month_str = '0' + month_str
                if len(day) < 2:
                    day = '0' + day
                return year + '-' + month_str + '-' + day
        except (ValueError, UnboundLocalError):
            pass

# Call Main
main()
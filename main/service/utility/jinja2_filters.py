import traceback
from datetime import datetime, timedelta
from main.service.utility.logger import log


def get_formated_date_name_filter(date):
    try:
        date = datetime.strptime(date, '%d.%m.%Y').date()
        day_name = {0: 'PONEDELJAK', 1: 'UTORAK', 2: 'SREDA', 3: 'ČETVRTAK',
                    4: 'PETAK', 5: 'SUBOTA', 6: 'NEDELJA'}

        month_name = {1: "JAN", 2: "FEB", 3: "MART", 4: "APR", 5: "MAJ", 6: "JUN",
                      7: "JUL", 8: "AVG", 9: "SEP", 10: "OKT", 11: "NOV", 12: "DEC"}

        day_index = date.weekday()
        month_index = date.month
        today = datetime.now().date()

        formated_date = f'{date.strftime("%d")}. {month_name[month_index]} {date.strftime("%Y")}'

        if date == today:
            return f'DANAS, {formated_date}'
        elif date == today + timedelta(days=1):
            return f'SUTRA, {formated_date}'
        else:
            return f'{day_name[day_index]}, {formated_date}'

    except Exception as e:
        log.error(f"{e}\n{traceback.format_exc()}")
        return date


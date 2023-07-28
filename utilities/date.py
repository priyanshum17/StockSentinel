from dateutil import parser

def datetime_format(datetime_str):
    try:
        dt_obj = parser.parse(datetime_str)

        # (YYYY-MM-DD HH:MM:SS)
        sql_format = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

        return sql_format

    except Exception as e:
        if datetime_str is None or datetime_str == '':
            pass
        else:
            print(f"Error parsing date string: {e}")
            print(datetime_str)
        return None
    


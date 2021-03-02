from datetime import datetime

def get_date(hour: bool) -> list:
    """Get the current date
    Args:
        hour (bool): select if you want the day or the hour

    Returns:
        list: returns the day or the hour
    """
    if hour: # return hour
        today = datetime.today()
        # Day/Hour/Minute
        day = today.strftime("%d")
        hour = today.strftime("%H")
        minute = today.strftime("%M")

        return [day, hour, minute]

    else: # returns day
        today = datetime.now()
        # Day/Month/Year
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        year = str(year)[-2:]
        return [day, month, year]
import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp): #done
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}" 



def convert_date(iso_string): #done
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
    new_date = datetime.strftime(date_object, '%A %d %B %Y')

    return new_date

def convert_f_to_c(temp_in_farenheit): #done
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celsius = (float(temp_in_farenheit) - 32) * (5/9)

    return float(f"{temp_in_celsius:.1f}")


def calculate_mean(weather_data): #done
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(i) for i in weather_data]

    return sum(weather_data) / len(weather_data)


def load_data_from_csv(csv_file): #done
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    rows = []
    with open (csv_file) as grid:
        data_list = list(csv.reader(grid))
        data_list.pop(0)
        for row in data_list:
            if row:
                rows.append([row[0], int(row[1]), int(row[2])])

    return rows

def find_min(weather_data): #done
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    min_num = float(weather_data[0])
    min_index = 0
    for index, n in enumerate(weather_data):
        if float(n) <= min_num:
            min_num = float(n)
            min_index = index

    return min_num, min_index

def find_max(weather_data): #done
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    max_num = float(weather_data[0])
    max_index = 0
    for index, n in enumerate(weather_data):
        if float(n) >= max_num:
            max_num = float(n)
            max_index = index

    return max_num, max_index

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

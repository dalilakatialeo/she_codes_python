

# from datetime import datetime

# date_object = datetime.strptime(iso_string,'%A %d %B %Y')

# # def convert_f_to_c(temp_in_farenheit):
# #     """Converts an temperature from farenheit to celcius.

# # #     Args:
# # #         temp_in_farenheit: float representing a temperature.
# # #     Returns:
# # #         A float representing a temperature in degrees celcius, rounded to 1dp.
# # #     """
# # #     temp_in_celsius = ((temp_in_farenheit) - 32) * (5/9)
# # #     return f"{temp_in_celsius:.1f}"

# # # print(convert_f_to_c(21))

# numbers = ["1","2","3"]

# def calculate_mean(weather_data):
#     """Calculates the mean value from a list of numbers.

#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     """
#     weather_data = [int(i) for i in weather_data]

#     return sum(weather_data) / len(weather_data)

# print(calculate_mean(numbers))

# # def list_mean(list):
# #     return sum(list) / len(list)
# # print(list_mean([10,5,6]))
#     return sum(weather_data) / len(weather_data)

numbers = [49, 57, 56, 55, 53]
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    weather_data = [float(i) for i in weather_data]
    if weather_data == []:
        return ()
    else:
        return min(weather_data), weather_data.index(min(weather_data))

print(find_min(numbers))

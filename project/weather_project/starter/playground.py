# from datetime import datetime

# iso_string = '2021-07-02T07:00:00+08:00'

# date_object = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
# new_date = datetime.strftime(date_object, '%A %d %B %Y')

# print(new_date)

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
# #     return sum(weather_data) / len(weather_data)

# weather_data = [49, 57, 56, 55, 53]
# # def find_min(weather_data):
#   """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
    # if len(weather_data) == 0:
    #     return ()
    # counter = float(weather_data[0])
    # min_weather = 0
    # for index,weather in enumerate(weather_data):
    #     if float(weather) <= counter:
    #         min_weather = index
    #         counter = float(weather)
    # return counter,min_weather
# weather_data = [49, 57, 56, 55, 53]
# def find_min(weather_data):
#     if weather_data == []:
#         return ()
#     else:
#         min_num = weather_data[0]
#         for number in weather_data:
#             if number <= min_num:
#                 min_num = number
#             return min_num, weather_data[min_num]

# print(find_min(weather_data))

# numbers = [6,3,8,1]
# min_num = numbers[0]
# min_index = 0

# if len(numbers) == 0:
#     print()
# else:
#     for index, n in enumerate(numbers):
#         if n <= min_num:
#             min_num = n
#             min_index = index
#     print(min_num, min_index)

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

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

list_of_lists = [
    ["a", 6, 2], #date as string, min as int, max as int
    ["b", 3, 4],
    ["c", 5, 6],
    ["d", 7, 8],
    ["e", 1, 10]
]

if list_of_lists == []:
    print ()

else:
#set min number as first encountered
    min_num_list = []
    min_num = float(list_of_lists[0][1])
    max_num = float(list_of_lists[0][2])
    min_index = 0
    max_index = 0
    for index, row in enumerate(list_of_lists): #iterate over the sublists
       min_num_list.append(row[1])
    print(find_min(min_num_list))

    min_temp, min_pos = find_min(min_num_list)
# print(min_num_list)
    #    if row: #provided that they are a list
    #         for n in row: #for each value in the sublist
    #             # if n != row[0]: #provided that it is not the string at index 0
    #                 if n <= min_num: #if the value is less than or equal to min
    #                     min_num = n #new min will be that value
    #                     min_index = index
    print(f"The lowest temperature will be {min_temp}, and will occur on {min_pos}")

    #                 if i >= max_num:
    #                     max_num = i
    #                     max_index = index
    # print(f"The highest temperature will be {max_num}, and will occur on {list_of_lists[max_index][0]}")

    # list_of_lists = [float(x) for x in list_of_lists]

    # return sum(weather_data) / len(weather_data)
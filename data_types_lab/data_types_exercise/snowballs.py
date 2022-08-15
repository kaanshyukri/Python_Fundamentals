number_of_snow_balls = int(input())
max_number = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
weight_max = 0
time_max = 0
quality_max = 0
for _ in range(number_of_snow_balls):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > max_number:
        max_number = snowball_value
        weight_max = snowball_weight
        time_max = snowball_time
        quality_max = snowball_quality

print(f"{weight_max} : {time_max} = {int(max_number)} ({quality_max})")







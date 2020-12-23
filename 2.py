sec = int(input("Введите количество секунд, которое хотите перевести в формат чч:мм:сс - "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = ((sec % 3600) % 60) % 60

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print(f"Результат: {hours}:{minutes}:{seconds}")

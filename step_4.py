
hour = input(' Saati Giriniz:')
rate = input('Rate Giriniz:')


def computepay(hour, rate):
    hour = int(hour)
    rate = int(rate)
    workingDay = 40

    if hour > workingDay:
        extraWork = (hour - workingDay) * 1.5
        total = (workingDay + int(extraWork)) * 10
        print(total)
    else:
        total = hour * rate

    print(int(total))


computepay(hour, rate)
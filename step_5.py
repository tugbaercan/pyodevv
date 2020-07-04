

def hotel_cost(night):
    amount = (140 * night)
    return amount


def plane_ride_cost(city):
    city = input ("Hangi Şehirde Yaşıyorsunuz?:")
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
            return 222
    if city == "Los Angeles":
        return 475


def rental_car_cost(days):
    day = int(input("Kaç Gün Kalacaksınız?:"))
    daily_total_amount = int(40 * day)

    if day > 7:
        return daily_total_amount - 50
    elif 3 <= day <= 6:
        return daily_total_amount - 20
    else:
        print(daily_total_amount)

def trip_cost (city, days):
    spending_money = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)

    return print(spending_money)






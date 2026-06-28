driver_name1 = "Lewis Hamilton"
lap_1 = 90
lap_2 = 90.67
lap_3 = 91.23

def avg_time(lap1, lap2, lap3):
    return (lap1+lap2+lap3)/3

def final_return(avg, driver_name):
    return driver_name, "s avargae lap time is", avg


print(final_return(avg_time(lap_1,lap_2,lap_3), driver_name1))

# uses a nested function call while keeping variables global - un-needed in such a small program but useful to keep organised in future
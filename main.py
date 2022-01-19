import csv
import math

filename = "shots_data.csv"

def get_info():

    made_corner_3a = 0
    attempted_corner_3a = 0

    made_3a = 0
    attempted_3a = 0

    made_2a = 0
    attempted_2a = 0

    made_corner_3b = 0
    attempted_corner_3b = 0

    made_3b = 0
    attempted_3b = 0

    made_2b = 0
    attempted_2b = 0

    

    with open(filename, 'r') as csvfile:
        csv_read = csv.reader(csvfile, delimiter=',')

        next(csv_read)

        for line in csv_read:
            if str(line[0]) == "Team A":
                if float(line[2]) <= 7.8:
                    if float(line[1]) >= 22.0 or float(line[1]) <= -22.0:
                        if int(line[3]) == 0:
                            attempted_corner_3a = attempted_corner_3a + 1
                        elif int(line[3]) == 1:
                            attempted_corner_3a = attempted_corner_3a + 1
                            made_corner_3a = made_corner_3a + 1
                    elif float(line[1]) < 22.0 or float(line[1]) > -22.0:
                        if int(line[3]) == 0:
                            attempted_2a = attempted_2a + 1
                        elif int(line[3]) == 1:
                            attempted_2a = attempted_2a + 1
                            made_2a = made_2a + 1 
                if float(line[2]) > 7.8:
                    distance_shot= ((((float(line[1])- 0 )**2) + ((float(line[2])-0)**2) )**0.5)
                    if distance_shot > 23.75:
                        if int(line[3]) == 0:
                            attempted_3a = attempted_3a + 1
                        elif int(line[3]) == 1:
                            attempted_3a = attempted_3a + 1
                            made_3a = made_3a + 1
                    if distance_shot < 23.75:
                        if int(line[3]) == 0:
                            attempted_2a = attempted_2a + 1
                        elif int(line[3]) == 0:
                            attempted_2a = attempted_2a + 1
                            made_2a = made_2a + 1
            elif str(line[0]) == "Team B":
                if float(line[2]) <= 7.8:
                    if float(line[1]) >= 22.0 or float(line[1]) <= -22.0:
                        if int(line[3]) == 0:
                            attempted_corner_3b = attempted_corner_3b + 1
                        elif int(line[3]) == 1:
                            attempted_corner_3b = attempted_corner_3b + 1
                            made_corner_3b = made_corner_3b + 1
                    elif float(line[1]) < 22.0 or float(line[1]) > -22.0:
                        if int(line[3]) == 0:
                            attempted_2b = attempted_2b + 1
                        elif int(line[3]) == 1:
                            attempted_2b = attempted_2b + 1
                            made_2b = made_2b + 1 
                if float(line[2]) > 7.8:
                    distance_shot= ((((float(line[1])- 0 )**2) + ((float(line[2])-0)**2) )**0.5)
                    if distance_shot > 23.75:
                        if int(line[3]) == 0:
                            attempted_3b = attempted_3b + 1
                        elif int(line[3]) == 1:
                            attempted_3b = attempted_3b + 1
                            made_3b = made_3b + 1
                    if distance_shot < 23.75:
                        if int(line[3]) == 0:
                            attempted_2b = attempted_2b + 1
                        elif int(line[3]) == 0:
                            attempted_2b = attempted_2b + 1
                            made_2b = made_2b + 1

        fga_a = attempted_3a + attempted_2a + attempted_corner_3a
        total_made_3a = made_3a + made_corner_3a
        shot_corner_3a = (attempted_corner_3a / fga_a)
        shot_3a = (attempted_3a / fga_a)
        shot_2a = (attempted_2a / fga_a)
        
        fga_b = attempted_3b + attempted_2b + attempted_corner_3b
        total_made_3b = made_3b + made_corner_3b
        shot_corner_3b = (attempted_corner_3b / fga_b)
        shot_3b = (attempted_3b / fga_b)
        shot_2b = (attempted_2b / fga_b)

        print("Shot Distribution for the Corner Three on Team A is," + str(shot_corner_3a))
        print("Shot Distribution for the Non-Corner Three on Team A is," + str(shot_3a))
        print("Shot Distribution for 2 Pointers on Team A is," + str(shot_2a))

        print("Shot Distribution for the Corner Three on Team B is," + str(shot_corner_3b))
        print("Shot Distribution for the Non-Corner Three on Team B is," + str(shot_3b))
        print("Shot Distribution for 2 Pointers on Team B is," + str(shot_2b))


        fg_corner_3a = (made_corner_3a + (0.5 * made_corner_3a )) / (attempted_corner_3a)
        fg_3a = (made_3a + (0.5 * made_3a )) /(attempted_3a)
        fg_2a = (made_2a) / (attempted_2a)

        fg_corner_3b = (made_corner_3b + (0.5 * made_corner_3b )) / (attempted_corner_3b)
        fg_3b = (made_3b + (0.5 * made_3b )) /(attempted_3b)
        fg_2b = (made_2b) / (attempted_2b)

        print("eFG for Corner Three on Team A is," + str(fg_corner_3a))
        print("eFG for Non-Corner Three on Team A is," + str(fg_3a))
        print("eFG for Two Pointer on Team A is, " + str(fg_2a))

        print("eFG for Corner Three on Team B is," + str(fg_corner_3b))
        print("eFG for Non-Corner Three on Team B is," + str(fg_3b))
        print("eFG for Two Pointer on Team B is, " + str(fg_2b))
def main():
    get_info()
        
        
if __name__ == "__main__":
    main()
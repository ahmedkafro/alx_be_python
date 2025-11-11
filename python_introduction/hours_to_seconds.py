def convert_hours_to_seconds(hours : int )->int:

     SECONDS_PER_HOUR = 3600
     return hours * SECONDS_PER_HOUR

def main():

    hours = 2  # Number of hours to convert
    seconds = convert_hours_to_seconds(hours)
    print(f"{hours} hour(s) is {seconds} seconds.")


if __name__ == "__main__":
    main()
 
  

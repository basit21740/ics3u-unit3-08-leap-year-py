#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this program tells about leap years


def main():
    # this function determine leap years

    # input
    try:
        year = input("Please enter the year: ")
        year = int(year)

        # process/output
        if year % 400 == 0:
            print(f"{year} is definitely a leap year")
        elif year % 100 == 0:
            print(f"{year} is not a leap year")
        elif year % 4 == 0:
            print(f"{year} is definitely a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        print(f"{year} is not an integer")

    # done
    print("\nDone.")


if __name__ == "__main__":
    main()

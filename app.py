import argparse, importlib, datetime

from utils.file_read import FileReader


def main():
    today = datetime.date.today()

    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument("-y", "--year", dest="year", default=today.year, metavar="year_number", type=int, help="Required, year number of the AoC event")
    parser.add_argument("-d", "--day", dest="day", default=today.day, metavar="day_number", type=int, help="Required, day number of the AoC event")
    parser.add_argument("-p", "--part", dest="part", default=1, metavar="part_number", type=int, help="Required, part number of the day of the AoC event")
    args = parser.parse_args()

    if not 0 < args.day < 26:
        print("day number must be between 1 and 25")
        exit()
    elif args.part not in [1, 2]:
        print("part number must be 1 or 2")
        exit()
    else:
        file_reader = FileReader(args.year, f"{args.day:02d}", args.part)
        file_content = file_reader.read_file()
        
        if file_content:
            solution = importlib.import_module(f"{args.year:04d}.{args.day:02d}.solution").Solution(data=file_content)
            print(f"the answer is {answer}\n" if (answer := solution.solve(part_num=args.part)) is not None else "")

if __name__ == "__main__":
    main()
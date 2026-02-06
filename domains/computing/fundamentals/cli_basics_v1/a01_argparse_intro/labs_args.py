import argparse

def main():
    parser = argparse.ArgumentParser(description="Scholar Ears")
    
    parser.add_argument("--project", required=False, type=str, help="Project Name")
    parser.add_argument("--level", required= False, default=1, type=int, help="Student level")
    parser.add_argument("--xp", required= False, default=0, type=int, help="Student xp")

    args = parser.parse_args()
    print(f"Project: {args.project}, Level: {args.level}")

if __name__== "__main__":
    main()
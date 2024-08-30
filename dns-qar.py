import sys
from App import App

def main():
    
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} `url` `server_to_query`") 
        sys.exit(1)

    app = App(sys.argv[1], sys.argv[2]).run()

if __name__ == '__main__':
    main()

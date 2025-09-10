
import os, sys, time

R = '\033[1;31m'; Y = '\033[1;33m'; W = '\033[1;37m'; RESET = '\033[0m'

def main():
    print(Y + "[*] Checking root permissions..." + RESET)
    time.sleep(1.2)

    
    if hasattr(os, "geteuid"):
        if os.geteuid() == 0:
            print(R + "[✘] Root permission detected! This tool cannot run on rooted environment." + RESET)
        else:
            print(R + "[✘] Root access not found. Exiting." + RESET)
    else:
        print(R + "[✘] Root check failed. Exiting." + RESET)

    time.sleep(1.5)
    sys.exit(1)

if __name__ == "__main__":
    main()
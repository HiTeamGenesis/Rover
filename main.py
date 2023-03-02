import colorama
import logger
import cams


if __name__ == "__main__":
    colorama.init()
    print(colorama.Fore.GREEN + "Starting Rover Modules Core...")

    cams.stream_cams()
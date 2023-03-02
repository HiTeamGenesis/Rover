import colorama
import logger
import cams


if __name__ == "__main__":
    colorama.init()

    logger.success("Starting Rover Modules Core...")
    
    logger.info("Attempting to start camera stream...")
    cams.stream_cams()
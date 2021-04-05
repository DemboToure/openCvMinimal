from logger.log import logger
from video_utils import video_utils 

if __name__ == '__main__' :
    logger.debug("Running...")
    video_utils.read_cam_save(0)

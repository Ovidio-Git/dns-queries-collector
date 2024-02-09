from logging import getLogger, INFO, FileHandler, Formatter

# Confg app logging
logger = getLogger('lumuLogger')
# Set the logger level to INFO
logger.setLevel(INFO) 
# Create a file handler and set the level to INFO
file_handler = FileHandler('./lumu.log')
file_handler.setLevel(INFO)
# Write the logs with the following format: 
# 2021-01-06 14:37:02,228 - lumuLogger - INFO - Data send
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Add the file handler to the logger
logger.addHandler(file_handler)

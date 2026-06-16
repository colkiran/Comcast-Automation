import logging

# configuring the global settings
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is diagnostic message will show up now")
logging.info("The application has officially started....")
logging.warning("Warning: low disk space detected")

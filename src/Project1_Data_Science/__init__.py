import os
import sys
import logging

logging_str = ['%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                '%Y-%m-%d %H:%M:%S']
log_dir = 'logs'
log_filename = os.path.join(log_dir, 'logs.log')    
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    format=logging_str[0],
                    handlers=[logging.FileHandler(log_filename), 
                              logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("Datasciencelogger")

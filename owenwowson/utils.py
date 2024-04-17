#!/usr/bin/env python3

from pathlib import Path
import logging
import sys


def valid_filepath(path: str) -> Path:
	"""Determine whether a provided str is a valid file path, return as a Path object if it does. Fast-fail if not.
	
	Args:
	    path (str): File path for verification
	
	Returns:
	    Path: Verify file path
	"""

	path = Path(path).expanduser()
	if path.is_file():
		return path
	else:
		print(f"Provided filepath: {path} does not exist.")
		sys.exit()


def setup_logger(logger_name, write_log=False, verbose=True):
	# Set up logger
	logger = logging.getLogger(logger_name)
	logger.setLevel(logging.DEBUG)

	# Config debug file
	if write_log:
	    formatter_logfile = logging.Formatter("[%(levelname)s] %(message)s")
	    log_file = logging.FileHandler(f"{logger_name}.log")
	    log_file.setLevel(logging.DEBUG)
	    log_file.setFormatter(formatter_logfile)
	    logger.addHandler(log_file)

	# Config console logger
	formatter_console = logging.Formatter("[%(levelname)s] %(message)s")
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.INFO if not verbose else logging.DEBUG)
	console_handler.setFormatter(formatter_console)
	logger.addHandler(console_handler)

	return logger


LOGGER = setup_logger('OwenWowson')

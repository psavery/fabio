version = "0.0.9"
import logging
logging.basicConfig()
import fabioimage
import openimage
from fabioutils import filename_object, COMPRESSORS, jump_filename, \
        previous_filename, next_filename, deconstruct_filename, \
        extract_filenumber, getnum
from openimage import openimage as open


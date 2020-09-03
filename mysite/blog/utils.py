import datetime
import re
import math
from django.utils.html import strip_tags

def count_words(text_string):
    word_string = strip_tags(text_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count

def get_read_time(text_string):
    count = count_words(text_string)
    read_time_min = math.ceil(count/200.0) #Assuming 200 words per min Reading
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return read_time
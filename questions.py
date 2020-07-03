import xlsxwriter
from rome_prototype import RomePrototype
from update_settings import UpdateSettings

request_data_type = input("What type of data are you looking for? (0 for qualitative and 1 for quantitative)\n")
if int(request_data_type) == 1:
    request_data_dimensions = input("How dimensions is your requested data represented across? (Enter integer)\n")
else:
    request_data_dimensions = 0
request_data_sensitivity = input("What is the sensitivity of this data packet? (0 for low | 3 for very high)\n")

request_channel = input("What channel are you requesting from? (0 for public and 1 for private)\n")
channel_pref = input("What channel would you like to receive the data from? (0 for public and 1 for private)\n")
if channel_pref != "":
    channel_pref_num = input("How strongly do you want to receive your data from this channel? (0 = indifferent | 3 for very strongly)\n")
else:
    channel_pref_num = 0

request_mode = input("What mode are you requesting from? (0 for textual, 1 for visual, and 2 for auditory)\n")
mode_pref = input("What mode would you like to receive the data from? (0 for textual, 1 for visual, and 2 for auditory)\n")
if mode_pref != "":
    mode_pref_num = input("How strongly do you want to receive your data from this mode? (0 = indifferent | 3 for very strongly)\n")
else:
    mode_pref_num = 0

UpdateSettings(request_data_type,
               request_data_dimensions,
               request_data_sensitivity,
               request_channel,
               channel_pref,
               channel_pref_num,
               request_mode,
               mode_pref,
               mode_pref_num)
RomePrototype()

# Module 7 Portfolio Milestone
# CSC500 William Vann

# define dictionaries

room_number_dict = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

instructor_dict = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_time_dict = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# test that keys in dicts are all the same

all_keys_match = (list(room_number_dict.keys()) == list(instructor_dict.keys()) == list(meeting_time_dict.keys()))

if all_keys_match:

    # create a list of keys to test for membership

    shared_keys_list = list(room_number_dict.keys())
    input_val = ''

else:

    # alert user to key problem and quit

    print('Problem with the dict keys ... quitting')
    input_val = 'Q'

# get user input and test for valid course number   
  
while input_val != 'Q':

    input_val = input('Enter a valid course number (e.g. CSC101) or Q to quit:\n')

    # test for valid course number input 
    
    if input_val in shared_keys_list:

        # format output string

        output_string = '|  {}  |  {}  |  {}  |  {}  |'.format( \
            input_val, \
            room_number_dict[input_val], \
            instructor_dict[input_val], \
            meeting_time_dict[input_val])
        
        # output results to user in data table format

        print('-' * len(output_string))
        print(output_string)
        print('-' * len(output_string))
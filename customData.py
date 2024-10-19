from datetime import datetime

def format_date(date_string, current_format):
    date_obj = datetime.strptime(date_string,current_format)
    formatted_date = date_obj.strftime('%d-%m-%y')
    return formatted_date


date_input = input('Enter a date: ')
current_format = input('Enter the currnt format (yyyy-mm-dd or mm-dd-yyyy): ')

if current_format == 'yyyy-mm-dd':
    result = format_date(date_input, '%Y-%m-%d')
elif current_format == 'mm-dd-yyyy':
    result = format_date(date_input, '%m-%d-%Y')
else:
    result = 'Unsupported format.'

print(f'Formated date: {result}')

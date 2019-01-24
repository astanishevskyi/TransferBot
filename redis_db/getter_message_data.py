from datetime import datetime


def get_all(json_dict: dict):

    timestamp = json_dict['channel_post']['date']
    converted_date = datetime.fromtimestamp(timestamp)
    output_data = [converted_date]

    try:

        text = json_dict['channel_post']['text']
        output_data.append(text)

    except KeyError:
        text = 'There is another type of data, not text'
        output_data.append(text)

    try:

        author = json_dict['channel_post']['author_signature']
        output_data.append(author)

    except KeyError:
        author = 'Unknown Author'
        output_data.append(author)

    return output_data

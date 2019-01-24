import redis
from redis_db.getter_message_data import get_all
from redis_db.parser_slack_id import get_link_on_slack
from slack_stuff.slack_main import slack_sender
from redis_db.getter_slack_id import get_slack_id


def redis_main(json_dict: dict):
    """
    Call all functions to set data in redis and send messages in Slack

    Args:
        json_dict: dict with telegram updates

    """

    conn_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)  # creation connection to redis
    redis_cli = redis.Redis(connection_pool=conn_pool)  # creation connection to redis

    try:
        telegram_slack_id = get_link_on_slack(json_dict)
        telegram_channel_id = telegram_slack_id[0]
        slack_channel_id = telegram_slack_id[1]
        redis_cli.set(telegram_channel_id, slack_channel_id)

    except TypeError:
        pass

    message_data = get_all(json_dict)
    slack_id = get_slack_id(json_dict, redis_cli)

    slack_sender(message_data, slack_id)

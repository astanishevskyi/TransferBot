import redis


def get_slack_id(json_dict: dict, redis_cli: redis.Redis):
    """
    Get slack channel id from redis_db

    Args:
        json_dict: dict with telegram updates
        redis_cli: redis client

    Returns:
        str: slack_id

    """

    telegram_id = json_dict['channel_post']['chat']['id']
    slack_id = redis_cli.get(telegram_id)
    return slack_id

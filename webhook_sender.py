from webhooks import webhook
from webhooks.senders import targeted


@webhook(sender_callable=targeted.sender)
def basic(url, wife, husband):
    return packer(husband=husband, wife=wife)


def packer(**kwargs):
    """ return dictionary"""
    return kwargs


if __name__ == '__main__':
    response = basic(
        url="http://httpbin.org/post", husband='Mostafa', wife='Princess'
    )
    print(response)
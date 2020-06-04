# Webhook_Sender
Python + Webhooks Made Easy

You should follow bottom command:

pip install webhooks

Free software: BSD license
Documentation: http://webhooks.rtfd.org.
WARNING This project is in a pre-alpha state. It’s not ready for use on ANYTHING.

# Existing Features
Easy to integrate into any package or project
Comes with several built-in senders for synchronous webhooks.
Comes with a RedisQ-powered asynchronous webhook.
Extendable functionality through the use of custom senders and hash functions.

# Planned Features
Comes with many built-in senders for synchronous and asynchronous webhooks.
Special functions for combining multiple sends of identical payloads going to one target into one.
Follows http://resthooks.org patterns
Great documentation
Compatibility with PyPy

# Usage
Follow these easy steps:

Import the webhook decorator.
Define a function that returns a JSON-serializable dictionary or iterable.
Add the webhook decorator and pass in a sender_callable.
Call the function!
Synchronous example (async examples to come soon):


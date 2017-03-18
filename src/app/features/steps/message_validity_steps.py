from behave import given, when, then

from main.message import Message


@given(u'I have an empty message object')
def step_impl(context):
    context.message = None

@when(u'I create the message object with {msg}')
def step_impl(context, msg):
    context.message = Message()
    context.message.parse_json(msg)

@then(u'I validate that the message {is_valid}')
def step_impl(context, is_valid):
    assert str(context.message.is_valid_message()) == is_valid
from behave import given, when, then

from main.message import Message


@given(u'A regularly functioning system')
def step_impl(context):
    context.message = None

@when(u'I receive a {message}')
def step_impl(context, message):
    context.message = Message()
    context.message.parse_json(message)

@then(u'I can get message body "{body}"')
def step_impl(context, body):
    assert context.message.body == body

@then(u'I can get from "{from_number}"')
def step_impl(context, from_number):
    assert context.message.source_number == from_number

@then(u'I can get to "{to_number}"')
def step_impl(context, to_number):
    assert context.message.destination_number == to_number
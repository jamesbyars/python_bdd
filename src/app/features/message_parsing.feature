Feature: Incoming messages are parsed into a message object

  Scenario Outline: Receive message
    Given A regularly functioning system
    When I receive a <message>
    Then I can get message body "<body>"
      And I can get from "<from_number>"
      And I can get to "<to_number>"

  Examples: Messages from customers
    | message                                              | body             | from_number | to_number |
    | {"body": "Hello world", "from": "123", "to": "456"}  | Hello world      |  123        | 456       |
    | {"body": "123", "from": "567", "to": "789"}          | 123              |  567        | 789       |



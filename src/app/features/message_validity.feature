Feature: Incoming messages are tested for validity

  Scenario Outline: Messages are received by the system are json formats
    Given I have an empty message object
    When I create the message object with <msg>
    Then I validate that the message <is_valid>

  Examples:
    | msg                                                                         | is_valid |
    | {"body": "Hello world", "from": "123"}                                      | False    |
    | {"body": "Hello world", "to": "456"}                                        | False    |
    | {"body": "Hello world"}                                                     | False    |
    | {"from": "123", "to": "456"}                                                | False    |
    | {"from": "123"}                                                             | False    |
    | {"to": "456"}                                                               | False    |
    | {"body": "Hello world", "from": "123", "to": "456"}                         | True     |
    | {"body": "Hello world", "from": "123", "to": "456", "bobby-random": "123"}  | True     |
    | {}                                                                          | False    |
    | {"tom": "sawyer"}                                                           | False    |
    | {"body": "body with lots of, commas, and such!@#&^&#*@(Q", "from": "123", "to": "456"}   | True    |
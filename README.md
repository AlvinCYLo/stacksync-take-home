**Stacksync Take Home**

Test via `docker compose up -d`

Tested locally via Docker and Postman
Did not put together a test suite due to time constraint. If I were to test:

- execute():
    - unsupported HTTP method -> throws an 404
    - bad request (ie no JSON payload) -> exception
    - validate_data() throws an error -> exception correctly returned
    - execute_script() throws an error -> exception correctly returned
    - validate_response() throws an error -> exception correctly returned

- validate_data():
    - missing "script" field in JSON -> throws an exception

- execute_script():
    - no main() function in payload -> exception thrown
    - other libraries used -> exception thrown


- validate_response():
    - invalid json structure response from main() -> exception thrown

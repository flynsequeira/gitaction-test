import os

# Retrieve the environment variable; if it's not set, show a default message.
test_env = os.getenv('TEST_ENV_VAR', 'Variable not found')
testing2 = os.getenv('TEST2', 'No env var for test 2')
print(f"TEST_ENV_VAR: {test_env}")

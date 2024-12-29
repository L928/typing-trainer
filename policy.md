

# design goals
Isolate the applicaiton from the qt framework as much as possible,
for portability and testability.

# TESTING
For TDD and other tests, a custom test framework is used for
simplicity.
A unit test can be included in the module-to-test, thus self-testing.
In that case, call __test if `__name__` == `"__main__"` and implement
the tests in this function. This ensures test discovery working.

# styleguide
|element|styling|example|
|-------|-------|-------|
|indentation | 2 spaces| |
|type names| upper camel case|UpperCamelCase|
|instance names| lower camel case|lowerCamelCase|
|constant (\*) | upper case | UPPER_CASE |

(\*) In python, there is no const keyword. Constants in python are usually
normal variables, unless a special method is used.

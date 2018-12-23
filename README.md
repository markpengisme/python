# Python

## Code style conventions


### Naming

> git repo: `lower-with-dash`

- package: `lower_with_under`(public)
- modules: `lower_with_under` (public), `_lower_with_under` (internal)
- classes: `CapWords` (public), `_CapWords` (internal)
- exceptions: `CapWords` (public)
- functions: `lower_with_under()` (public), `_lower_with_under()` (internal)

- global/class constants: `CAPS_WITH_UNDER` (public), `_CAPS_WITH_UNDER` (private)
- global/class variables: `lower_with_under` (public), `_lower_with_under` (private)
- instance variables: `lower_with_under` (public), `_lower_with_under` (protected), `__lower_with_under` (private)
- method names: `lower_with_under()` (public), `_lower_with_under()` (protected), `__lower_with_under()` (private)
- function/method parameters: `lower_with_under`
- local variables: `lower_with_under` (public)
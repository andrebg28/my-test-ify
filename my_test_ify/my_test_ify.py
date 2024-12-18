from dataclasses import dataclass
from typing import Any, Callable

from .assertive import equals
from .exceptions import TestFunctionError
from .utils import GREEN, RESET, get_summary


@dataclass(init=False)
class Report:
    def __init__(
        self,
        summary: Callable[..., str],
        report: Callable[..., str],
        failure_stack: Callable[..., list[str]],
    ):
        self.summary = summary
        self.report = report
        self.failure_stack = failure_stack

    def print(self):
        print(self.report())
        print(self.failure_stack()[0])
        print(self.summary())

    def print_full_report(self):
        print(self.report())
        for failure in self.failure_stack():
            print(failure)
        print(self.summary())


def my_test_ify(stop_on_failure: bool = False) -> tuple[Callable[..., Any], Report]:
    """_summary_

    Args:
        stop_on_failure (bool, optional): _description_.
        Defaults to False, if True, stops running tests as soon as the first
        error occurs.

    Raises:
        TestFunctionError: _description_

    Returns:
        tuple[Callable[...,Any],Report]: _description_
    """
    _passed_tests_counter = 0
    _failed_tests_counter = 0
    _total_tests_counter = 0
    _failure_message: list[str] = []
    _success_message: list[str] = []
    _stacks: list[str] = []
    _report: Report

    def summary() -> str:
        return get_summary(
            _total_tests_counter, _passed_tests_counter, _failed_tests_counter
        )

    def report() -> str:
        _report = ""
        for msg in _failure_message:
            _report = msg + _report
        for msg in _success_message:
            _report = msg + "\n" + _report
        return _report

    def failure_stack() -> list[str]:
        return _stacks[:] if len(_stacks) > 0 else [f"{GREEN}No failures{RESET}"]

    _report = Report(summary, report, failure_stack)

    def run_test[
        T
    ](
        expected: T,
        result: T,
        description: str = "",
        test_function: Callable[..., Any] = equals,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if not callable(test_function):
            raise TestFunctionError(
                "The provided test function is not a valid function."
            )

        nonlocal _total_tests_counter
        nonlocal _passed_tests_counter
        nonlocal _failed_tests_counter
        nonlocal _success_message
        nonlocal _failure_message
        nonlocal _stacks

        if stop_on_failure and _failed_tests_counter > 0:
            _report.print()

            exit()

        _total_tests_counter += 1

        passed, msg, stack = test_function(
            expected, result, _total_tests_counter, description, *args, **kwargs
        )

        if stack is not None:
            _stacks.append(stack)

        if passed:
            _passed_tests_counter += 1
            _success_message.append(msg)
        else:
            _failed_tests_counter += 1
            _failure_message.append(msg)

    def core[
        T
    ](
        expected: T,
        result: T,
        description: str = "",
        test_function: Callable[..., Any] = equals,
        *args: list[Any],
        **kwargs: dict[str, Any],
    ) -> None:

        run_test(expected, result, description, test_function, *args, **kwargs)

    return core, _report

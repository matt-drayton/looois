#!/bin/python3
"""
Unit tests for the `hello` module.
"""
import pytest

from project.hello import hello, main


class TestHelloManager:
    """Test methods within the `hello` module."""

    def test_hello(self):
        """Test hello() with the default subject ("world")."""
        assert hello() == "Hello, world!"

    def test_hello_input(self):
        """Test hello() with an argument for the subject of the greeting."""
        assert hello("test") == "Hello, test!"

    def test_main(self, capsys):
        """Test when the module is used as a script.

        Args:
            capsys (obj): Use stdout without needing to set/reset the output stream.
        """
        main("main")
        captured = capsys.readouterr()
        assert captured.out == "Hello, main!\n"

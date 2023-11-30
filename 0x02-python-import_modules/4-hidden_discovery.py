#!/usr/bin/python3
import dis

with open("hidden_4.pyc", "rb") as file:
    code = file.read()

dis.dis(code)

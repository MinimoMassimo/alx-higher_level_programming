#!/usr/bin/python3
"""module 7
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    a_list = load_from_json_file("add_item.json")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    a_list = []

for i in range(1, len(sys.argv)):
    a_list.append(sys.argv[i])
save_to_json_file(a_list, "add_item.json")

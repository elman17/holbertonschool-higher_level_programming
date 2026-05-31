#!/usr/bin/python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize to xml"""
    root = ET.Element("data")

    child = ET.SubElement(root, "name")
    child.text = "John"

    tree = ET.ElementTree(root)
    tree.write(filename)

    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        print(child.tag)
        print(child.text)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result

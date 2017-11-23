# ISO4217_numbers_to_codes_swift

The ISO4217 standard defines currencies used throughout the world. Among other properties, the standard assigns codes (e.g. `USD`) and numbers (e.g. `840`) to those currencies. This repo is simply a script that generates a Swift dictionary of the format `[Int32: String]` which contains currency numbers as its keys, and maps them to currency codes.

# How to use

## 1. Provide an XML source if needed
The script uses an XML file as its source. This repo already contains `ISO4217.xml`, downloaded from [here](https://www.currency-iso.org/en/home/tables/table-a1.html). If you need to update the source, replace the XML file, and make sure the tag names in the python script still match the tags used in the XML.

## 2. Run the python script
`make_currencies.py` is a simple XML-parsing script which prints a Swift dictionary. It uses minidom to parse XML, which should be available on most systems. To run it and redirect the output to a file, run

```
python make_currencies.py > currencies.swift
```

You can then paste the contents of `currencies.swift` into your project as needed.
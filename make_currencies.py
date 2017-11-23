from xml.dom import minidom

xmldoc = minidom.parse('ISO4217.xml')
countries = xmldoc.getElementsByTagName('CcyNtry')
numberTagName = 'CcyNbr'  # The tag name for country numbers in the xml
codeTagName = 'Ccy' # The tag name for country codes in the xml
usedCodes = []  # Keep track of which codes have already been added to the dictionary

# Open the dictionary:
print("let currencies: [Int32: String] = [")

for country in countries:
    # Get number and code for country, if any:
    numbers = country.getElementsByTagName(numberTagName)
    codes = country.getElementsByTagName(codeTagName)
    if len(numbers) > 0 and len(codes) > 0:
        numberNodes = numbers[0].childNodes
        codeNodes = codes[0].childNodes
        if len(numberNodes) > 0 and len(codeNodes) > 0:
            number = numberNodes[0].data
            code = codeNodes[0].data
            if not code in usedCodes:
                # Add an entry in the dictionary
                print("\t{}: \"{}\",".format(number, code))
                usedCodes.append(code)

# Close the dictionary:
print("]")

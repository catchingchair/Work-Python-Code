# xml parsing
import xml.dom.minidom # this is a module that lets us operate on a XML document

# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("samplexml.xml") # this will create an in-memory dom object that can be manipulated
print(doc.nodeName)
print(doc.firstChild.tagName)

# print out the document node and the name of the first child string
skills = doc.getElementsByTagName("skill")
print(f"Skill count: {skills.length}")
for skill in skills:
    print(skill.getAttribute("name"))

# create a new XML tag and add it into the document
new_skill = doc.createElement("skill")
new_skill.setAttribute("name","SQL")
doc.firstChild.appendChild(new_skill)

skills = doc.getElementsByTagName("skill")
print(f"Skill count: {skills.length}")
for skill in skills:
    print(skill.getAttribute("name"))

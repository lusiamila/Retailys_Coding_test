import requests
import zipfile
import xml.etree.ElementTree as ET

zip_url = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"

def download_and_extract_zip(zip_url):
    response = requests.get(zip_url)
    if response.status_code == 200:
        with open("astra_export_xml.zip","wb") as zip_file:
            zip_file.write(response.content)
        print("ZIP archive downloaded successfully")

        with zipfile.ZipFile("astra_export_xml.zip","r") as zip_read:
            zip_read.extractall("astra_export_xml")

xml_file_path = "astra_export_xml/export_full.xml"

#task 1
def item_count(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    items = root.findall('.//item')
    item_count = 0
    for item in items:
        item_count += 1
    print(item_count)

#task 2
def items_name(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    items = root.findall('.//item')
    for item in items:
        name = item.get('name')
        print(name)

#task 3
def spare_parts(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    parts = root.findall(".//parts/part[@name='Náhradní díly']/item")
    for part in parts:
        name = part.get('name')
        print(name)

def main():
    zip_url = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"
    download_and_extract_zip(zip_url)
    xml_file_path = "astra_export_xml/export_full.xml"

    print("Please choose the number: 1,2 or 3\n 1 item count\n 2 items names\n 3 spare parts")
    
    choice = int(input("Your choice: "))
    if choice == 1:
        #task 1
        item_count(xml_file_path)
    elif choice == 2:
        #task 2
        items_name(xml_file_path)
    elif choice == 3:
        #task 3
        spare_parts(xml_file_path)
    else:
        print("Error")

if __name__ == "__main__":
    main()
import xml.etree.ElementTree as ET
import re

class XMLHTMLHandler:
    def __init__(self, html_file_path):
        self.html_file_path = html_file_path
        
    def read_xml_from_html(self):
        # Read the HTML file
        with open(self.html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Extract XML content from CDATA section using regex
        cdata_pattern = r'<!$CDATA$(.*?)$$>'
        match = re.search(cdata_pattern, html_content, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        return None
    
    def update_xml_in_html(self, updated_xml):
        # Read current HTML content
        with open(self.html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Create new CDATA section
        new_cdata = f'<![CDATA[{updated_xml}]]>'
        
        # Replace old CDATA section with new one
        cdata_pattern = r'<!$CDATA$(.*?)$$>'
        updated_html = re.sub(cdata_pattern, new_cdata, html_content, flags=re.DOTALL)
        
        # Write updated content back to file
        with open(self.html_file_path, 'w', encoding='utf-8') as file:
            file.write(updated_html)

# Example usage
def main():
    # Create a sample HTML file with embedded XML
    sample_html = """
    <!DOCTYPE html>
    <html>
    <body>
        <div class="xml-data">
            <![CDATA[
            <?xml version="1.0" encoding="UTF-8"?>
            <products>
                <product id="1">
                    <name>Laptop</name>
                    <price>999.99</price>
                </product>
            </products>
            ]]>
        </div>
    </body>
    </html>
    """
    
    # Save sample HTML
    with open('sample.html', 'w', encoding='utf-8') as file:
        file.write(sample_html)
    
    # Create handler instance
    handler = XMLHTMLHandler('sample.html')
    
    # Read XML
    xml_content = handler.read_xml_from_html()
    if xml_content:
        print("Original XML:")
        print(xml_content)
        
        # Parse and modify XML
        root = ET.fromstring(xml_content)
        
        # Add new product
        new_product = ET.SubElement(root, 'product')
        new_product.set('id', '2')
        name = ET.SubElement(new_product, 'name')
        name.text = 'Tablet'
        price = ET.SubElement(new_product, 'price')
        price.text = '299.99'
        
        # Convert modified XML to string
        updated_xml = ET.tostring(root, encoding='unicode', method='xml')
        
        # Update HTML file
        handler.update_xml_in_html(updated_xml)
        print("\nUpdated XML:")
        print(handler.read_xml_from_html())

if __name__ == "__main__":
    main()

"""
handler = XMLHTMLHandler('your_file.html')
xml_content = handler.read_xml_from_html()
# Modify xml_content as needed
handler.update_xml_in_html(modified_xml_content)
"""


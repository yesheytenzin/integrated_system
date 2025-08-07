import xml.etree.ElementTree as ET

def add_books(xml_file, title, author, year, genre):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # creating new book element
        book = ET.Element('book')

        title_element = ET.SubElement(book,'title')
        title_element.text = title

        author_element = ET.SubElement(book,'author')
        author_element.text = author

        year_element = ET.SubElement(book,'year')
        year_element.text = str(year)

        genre_element = ET.SubElement(book,'genre')
        genre_element.text = genre

        root.append(book)

        # xml formatting
        ET.indent(tree, space="    ", level=0)

        # write to xml file
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)

        print(f'Book {title} added Successfully!')
        print()

    except ET.ParseError as e:
        print(f'Failed to parse XML: {e}')

    except FileNotFoundError as e:
        print(f'File {xml_file} not found')


title = input("Enter the title: ")
author = input("Enter the author: ")
year = input("Enter year of publication: ")
genre = input("Enter book genre: ")
print()

add_books('books.xml',title,author,year,genre)






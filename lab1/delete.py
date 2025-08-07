import xml.etree.ElementTree as ET

def delete_book(xml_file, title_to_delete):

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # looping
        for book in root.findall('book'):
            title = book.find('title')

            if title is not None and title.text == title_to_delete:
                root.remove(book)
                print(f'Book {title_to_delete} removed Successfully')
                break
            else:
                print(f'Book {title_to_delete} not found')

        tree.write(xml_file, encoding='utf-8', xml_declaration=True)

    except Exception as e:
        print(f'Error: {e}')

title_delete = input("Enter title to delete: ")
delete_book('books.xml',title_delete)


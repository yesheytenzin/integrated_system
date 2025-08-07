import xml.etree.ElementTree as ET

def parse_books(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for book in root.findall('book'):
            title = book.find('title').text
            author = book.find('author').text
            year = book.find('year').text
            genre = book.find('genre').text

            print(f'Title: {title}')
            print(f'Author: {author}')
            print(f'Year: {year}')
            print(f'Genre: {genre}')
            print('')

    except ET.ParseError as e:
        print(f'Failed to parse XML: {e}')

    except FileNotFoundError:
        print(f'File {xml_file} not found')

# running the parse function
parse_books('books.xml')

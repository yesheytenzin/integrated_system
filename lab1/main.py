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

def test_delete():
    title_delete = input("Enter title to delete: ")
    delete_book('books.xml',title_delete)

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

def test_parse():
    parse_books('books.xml')

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

def test_add():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = input("Enter year of publication: ")
    genre = input("Enter book genre: ")
    print()
    add_books('books.xml',title,author,year,genre)

def select_xml_operation(option):
    match option:
            case 1:
                test_add()
            case 2:
                test_parse()
            case 3:
                test_delete()

selected_option =int(input("1: add, 2: parse, 3: delete: "))
select_xml_operation(selected_option)

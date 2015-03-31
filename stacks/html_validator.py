import argparse
from stack import Stack


def validate_html(html_string):
    tags_stack = Stack()
    valid_html = True

    char_index = 0
    current_tag = ''
    closing_tag = False
    tag_is_writing = False

    while valid_html and len(html_string) > char_index:
        char = html_string[char_index]

        if (len(html_string) - 1) > char_index:
            next_char = html_string[char_index + 1]
        else:
            next_char = None

        if char == '<':
            tag_is_writing = True
        elif char == '/':
            if current_tag == '<':
                # this is a closing tag begins
                closing_tag = True
            elif tag_is_writing and next_char == '>':
                # this is a self closing tag so skip it
                tag_is_writing = False
                current_tag = ''
                char_index += 1
        elif char == '>' and tag_is_writing:
            tag_is_writing = False
            current_tag += char

            if closing_tag:
                if tags_stack.is_empty():
                    valid_html = False
                else:
                    last_tag = tags_stack.pop()
                    print(last_tag, current_tag)
                    if not tags_match(last_tag, current_tag):
                        valid_html = False
            else:
                tags_stack.push(current_tag)

            current_tag = ''
            closing_tag = False

        if tag_is_writing:
            current_tag += char

        char_index += 1

    if valid_html:
        valid_html = tags_stack.is_empty()

    return valid_html


def tags_match(opening_tag, closing_tag):
    return closing_tag == (opening_tag[0] + '/' + opening_tag[1:])

if __name__ == "__main__":
    # test
    simple_html = """
    <html>
       <head>
          <title>
             Example
          </title>
       </head>

       <body>
          <h1>Hello, world</h1>
          <input type="text" name="test" />
       </body>
    </html>
    """
    result = 'valid' if validate_html(simple_html) else 'invalid'
    print('Validation result: {0}'.format(result))

    # read file from command line argument and validate it
    pass

# Functions fo here
def make_statement(statement, decoration, lines=1):
    """Create headings (3 lines), subheadings ( 2 lines) and
    emphasised text / mini-headings ( 1 line_. Only use emoji for
    single line statements)"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

# Main Routine goes here


make_statement(statement="Programing is Fun!", decoration="=", lines=3)
print()
make_statement(statement="Programming is Still Fun!", decoration="*", lines=2)
print()
make_statement(statement= "Emoji in Action", decoration="👾",)

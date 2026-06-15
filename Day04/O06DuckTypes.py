
class File:

    def read(self):
        return "reading from a file...."

class StringIO:
    def read(self):
        return "reading data from a string buffer....."

def read_data(source):
    print(source.read())


file = File()
string_buffer = StringIO()

read_data(file)             # reading data from a file
read_data(string_buffer)    # reading data from a string buffer


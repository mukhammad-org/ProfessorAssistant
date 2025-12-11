import professorassistant
def main():
    infile = open(professorassistant.path,'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)


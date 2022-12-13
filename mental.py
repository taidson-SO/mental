import json
import sys


def main():
    if len(sys.argv) >= 2:
     return sys.argv[1] if sys.argv[1].split(".")[-1] == "json" else sys.argv[1]+".json"
    else:
        return None



class Mental():

    def __init__(self, filename: str=main()):
        print(filename)
        self.tag = ""
        self.nota = ""
        self.filename = filename if filename != None else "mental.json" 
        self.filename = self.__normalize_filename()


    def __normalize_filename(self):
        return self.filename if self.filename.split(".")[-1] == "json" else self.filename+".json"


    def remember(self, tag: str, note: str):
        self.tag = tag
        self.note = note
        self.__save()


    def load_memory(self, filename=None, tag=None):
        
        if filename is None:
            filename = self.filename
            
        try:
            dic = self.__load_dic(filename)
            if tag in dic:
                return {tag:dic[tag]}
            
            elif tag is None:
                return {filename:dic}
            
            else:
                print("tag is not in dictionary")
                return "tag is not in file"
            
        except FileNotFoundError as e:
            print(e)
            return f'File {filename} not found'


    def __save(self):
        dct = self.__get_dct(self.filename)
        self.__create_dic(dct, self.filename)


    def __load_dic(self, filename):
        with open(filename) as read:
            return json.load(read)


    def __get_dct(self, filename):
        try:
            dct = self.__load_dic(filename)
            
            if self.tag in dct:
                dct[self.tag].append(self.note)
            else:
                dct[self.tag] = [self.note]                    
                            
        except FileNotFoundError as e:
            dct = {self.tag:[self.note]}
            
        return dct



    def __create_dic(self, dct, filename):
        with open(filename, "w") as write:
            json.dump(dct, write)


# def __test__(fun):
#     print(fun)


# if __name__ == "__main__":
    
    # obj = Mental(main())
    # __test__(obj.load_memory()) #test to filename default
    # __test__(obj.load_memory("testeMental.json")) #test testeMental.json filename
    # __test__(obj.load_memory("nota.json", "nota")) #test search tag="nota" in nota.json file
    # __test__(obj.load_memory(tag="nota")) #test search tag="nota" in mental.json filename
    # __test__(obj.remember("hoje", "programando em python eu vi uma oportunidade!")) #test default console insert filename
    # __test__(obj.load_memory()) #test to filename default
    


import requests
import sys

class App:
    def __init__(self) -> None:
        if len(sys.argv) == 2:
            self.link:str = str(sys.argv[1])
            self.download(self.link)
            filename: str = str(sys.argv[2])
            with open(filename, "ab") as file:
                file.write(self.response.content)

        else:
            self.link:str= str(input("Link: "))
            self.download(self.link)
            filename = input("Filename(with extension): ")
            with open(filename, "ab") as file:
                file.write(self.response.content)
    
    def download(self, l):
        self.response = requests.get(self.link)
        print(self.response.headers['content-type'])

if __name__ == "__main__":
    app = App()



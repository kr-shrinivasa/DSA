class Movie:
    def __init__(self,l,c,m) -> None:
        self.l=l
        self.c=c
        self.m=m
    def run(self):
        return f"This is a {self.l} movie with {self.c} characters and is {self.m} minutes long."
if __name__ == "__main__":
    m=Movie(input(),int(input()),int(input()))       
    print(m.run())
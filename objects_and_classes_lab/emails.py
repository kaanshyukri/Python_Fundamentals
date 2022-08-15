class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Stent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    tokens = line.split()
    s = tokens[0]
    r = tokens[1]
    c = tokens[2]
    email = Email(s, r, c)
    emails.append(email)
    line = input()

send_emails = list(map(int, input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())

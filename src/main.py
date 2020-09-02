import re

def run():
    file_path = 'src/encoded.txt'
    regex = '[a-z]+'
    pattern = re.compile(regex)
    secret_message = ''

    with open(file_path, 'r', encoding='utf-8') as f:
        
        for line in f.readlines():
            secret_message += ''.join(re.findall(pattern, line))

        # Other way to get the secret message, remember to comment the other loop to make this one work
        """ for i, line in enumerate(f):
            for match in re.finditer(pattern, line):
                secret_message += match.group() """

    f.close()
    
    print(secret_message)


if __name__ == '__main__':
    run()

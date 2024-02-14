import paramiko
import time
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router = {'hostname': '192.168.48.131', 'port': '22', 'username': 'ahmad', 'password': '12345'}
print(f'Connecting To The {router["hostname"]}')

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# ssh_client.connect(hostname='10.149.127.209', port=22, username='ahmad', password='12345',
#                   look_for_keys=False, allow_agent=False )
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')

shell.send('show run \n')

time.sleep(5)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()

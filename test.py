import pynetbox
print('test from git hub')
tnetbox = 'jhfdsghfgsdhgfhsdghfgsdhgfhsdghfg'
nb = pynetbox.api(
            url='https://netbox.cbc-rc.ca/',
            token=tnetbox
        )
nb.http_session.verify = False
devices = nb.dcim.devices.get(name='MTLKJHIU76')
print(devices)

print('test jenkins')


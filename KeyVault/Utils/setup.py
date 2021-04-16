import os
import getpass

print(getpass.getuser())
def setup():
    user = getpass.getuser()
    pathVault = '/home/' + user + '/PyVault/'
    if not os.path.exists(pathVault):
        os.mkdir(pathVault)
    if not os.path.exists(pathVault + 'database/'):
        os.mkdir(pathVault + 'database/')
        print('database conf folder has been created')
    if not os.path.exists(pathVault + 'database/'+ user + '.db'):
        os.mknod(pathVault + 'database/' + user + '.db')
        print('the database has been created')
        
    print(pathVault)

def main():
    setup()
    print('the setup for PyVault is done !!')

if __name__ == "__main__":
    main()
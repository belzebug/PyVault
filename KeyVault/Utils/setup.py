import os
import getpass

print(getpass.getuser())
def setup():
    user = getpass.getuser()
    pathVault = '/home/' + user + '/PyVault/'
    if os.path.exists(pathVault):
        pass
    else:
        os.mkdir(pathVault)
        os.mkdir(pathVault + 'database/')
        os.mknod(pathVault + 'database/' + user + '.db')
    print(pathVault)

def main():
    setup()

if __name__ == "__main__":
    main()
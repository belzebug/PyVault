sudo apt install python-tk
sudo apt install xclip
git clone https://github.com/belzebug/PyVault
mkdir ~/PyVault
cp -avr PyVault/KeyVault ~/PyVault
echo "alias pyvault='python ~/PyVault/KeyVault/main.py'" >> ~/.bashrc
python ~/PyVault/KeyVault/setup.py
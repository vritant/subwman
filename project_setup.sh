if ! rpm -qa | grep -qw npm; then
	    yum install -y npm
fi
npm install npm grunt-cli --save-dev
./install.sh
npm install

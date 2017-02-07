# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

mesg n
 
export WORKON_HOME=/var/www/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh


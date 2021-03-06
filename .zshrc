# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
# if/else is so you can copy settings to root
if [[ $USER == "root" ]]; then
  export ZSH="/root/.oh-my-zsh"
  ZSH_THEME="bira"
else 
  export ZSH="${HOME}/.oh-my-zsh"
  ZSH_THEME="lukerandall"
fi

# set shell
export BROWSER="$(which firefox)"
export EDITOR="vi"
export VISUAL="vi"

# set colored man pages
#export LESS_TERMCAP_mb=$'\e[1;32m'
#export LESS_TERMCAP_md=$'\e[1;32m'
#export LESS_TERMCAP_me=$'\e[0m'
#export LESS_TERMCAP_se=$'\e[0m'
#export LESS_TERMCAP_so=$'\e[01;33m'
#export LESS_TERMCAP_ue=$'\e[0m'
#export LESS_TERMCAP_us=$'\e[1;4;31m'

 HYPHEN_INSENSITIVE="true"

ENABLE_CORRECTION="false"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
 HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  battery
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#
fpath=(~/.zsh.d/ $fpath)

# TMUX
if which tmux >/dev/null 2>&1; then
    #if not inside a tmux session, and if no session is started, start a new session
    if [[ -n $TMUX && $TERM == "screen" ]]; then
      tmux new-session -A -s main
    fi
fi

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# wirguard vpn related
alias rvpn='bash ${HOME}/scripts/resetvpn.sh'
alias dvpn='bash ${HOME}/scripts/downvpn.sh'
alias cvpn='cvpn(){bash ${HOME}/scripts/changevpn.sh $(ls /etc/wireguard/ | cut -f1 -d'.' | fzf) }; cvpn'
alias hvpn='bash ${HOME}/scripts/resetvpnhome.sh'
# networking related
alias pg='ping 1.1.1.1 -c1 && curl ipinfo.io || iwconfig' # internet test
alias st='st(){curl ipinfo.io && speedtest --server $(speedtest --list | grep ")" | fzf | cut -f1 -d")" ) }; st'
alias rdns='f(){dig +short "${1}.in-addr.arpa." PTR }; f' # reverse DNS lookup 
alias getip='dig +short myip.opendns.com @resolver1.opendns.com' # get external ip addr, use with | c for copy
alias getiip='ifconfig | grep "inet " -B1 | grep '\'': flags'\'' | cut -f1 -d'\'':'\'' | fzf --height=7 --reverse | xargs -I {} bash -c '\''ifconfig -a | grep -A1 {} | grep -e "inet "'\'' | xargs echo | awk '\''{print $2}'\'' '
# creates a backup of a file, then edits in vim
alias bvim='bvim(){cp "${1}" "${1}.bak" && vim "${1}"}; bvim' # backup file before vim
# zshrc related
alias getalias='alias | grep -v 'git' | grep -v 'cd' | grep -v 'ls' | fzf  | cut -f2 -d"=" | xargs zsh -c' # get aliases
alias src='source ${HOME}/.zshrc' # sources .zshrc
alias zshrc='vim ${HOME}/.zshrc && source ${HOME}/.zshrc && echo ".zshrc sourced"'
#program shortcuts
alias cat='bat -n --theme=zenburn'
alias bc='bc -q'
alias xi='bash "${HOME}/.xinitrc"' # caps lock binding reset
alias tm='tmux new-session -A -s main'
alias root='sudo su'
alias pick='deepin-picker 2>1' # color picker
alias k='su k'
alias sus='sudo pm-suspend'
alias update='sudo apt update && sudo apt upgrade -y'
alias peco='peco --initial-filter=Regexp' 
alias p2='python2 -q'
alias p3='python3 -q'
alias movie='vlc -f $(find /mnt/gdrive/tdrive/movies/ -type f -iname "*.mkv" | fzf )'

# misc
alias fsoc="cat ${HOME}/scripts/fsoc.ascii | nms -cas -f red"
alias rootupdate='[[ $USER == "root" ]] && zsh /root/.cpdotfiles.sh || echo "run as root."'
alias cleandownloads='bash ${HOME}/scripts/cleandownloads.sh'
alias cheatcp='f(){ cheat $@ | fzf | xclip -i}; f'
alias cheat='f(){ cheat $@ | bat -n --theme=zenburn --color=always -l bash }; f'
alias chee='f(){ /usr/local/bin/cheat -e $@ }; f'
alias c='xclip -i && xclip -o | tr -d '\''\n'\'' | xsel -b'
alias v='xclip -o' #requires x11 forwarding for paste thru ssh
alias killer='f(){ ps -a | fzf  | awk '\''{print $1}'\'' | xargs kill $@ }; f' #quick kill with fzf, takes args
alias rot13='f(){ echo "$@" |  tr "b-za-aB-ZA-A" "a-zA-Z" }; f'
alias ixio='curl -s -F "f:1=<-" ix.io | xclip -i && xclip -o | tr -d '\''\n'\'' | xsel -b && xclip -o' # pastebin + copy to clipboard
alias sprunge='curl -s -F "sprunge=<-" sprunge.us | xclip -i && xclip -o | tr -d '\''\n'\'' | xsel -b && xclip -o' # alt pastebin

# sync files
alias config='/usr/bin/git --git-dir=${HOME}/.cfg/ --work-tree=${HOME}'
alias cpush='/usr/bin/git --git-dir=${HOME}/.cfg/ --work-tree=${HOME} commit -a --allow-empty-message -m "$(fortune)" ; /usr/bin/git --git-dir=${HOME}/.cfg/ --work-tree=${HOME} push'
alias cpull='/usr/bin/git --git-dir=${HOME}/.cfg/ --work-tree=${HOME} pull && source ${HOME}/.zshrc' 

#fzf
alias notes='cd ${HOME}/notes && ${HOME}/notes/.fuz.sh'
alias fzf='fzf --bind '\''ctrl-o:execute(bat --theme=zenburn {}),ctrl-y:execute-silent(echo {} | xclip -i )+abort'\'' ' #ctrl y to copy to clipboard
alias fzfc='fzf  | xclip -i'
alias manf='f(){ man $1 | fzf  --preview "man $1 | grep --color=always -C$(expr `tput lines` / 3) -- {} " --preview-window=up:70% --reverse -m --inline-info }; f'
alias cpterm='echo "export TERM=$TERM; stty rows $(tput lines) cols $(tput cols)" | xsel -b && [[ $(ps -p $$ | grep bash) ]] && echo Terminal info copied to clipboard. || echo "WARNING: not running as bash." '

# oscp
alias enumerateip='f(){ curl -sL ${1}${2} | egrep -o "([a-zA-Z]*\.){1,4}${1}" | sort -u | parallel ping -c1 -W1 {} 2>/dev/null | grep ttl | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort -u };f' 

#bluetooth
alias btconnect='bluetoothctl <<<"connect 64:1C:B0:1B:06:CB"'
alias btdisconnect='bluetoothctl <<<"disconnect 64:1C:B0:1B:06:CB"'

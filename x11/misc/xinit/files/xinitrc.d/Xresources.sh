SYSRESOURCES=/etc/X11/Xresources
USERRESOURCES=$HOME/.Xresources

if [ -f $SYSRESOURCES ]; then
    xrdb -merge $SYSRESOURCES
fi

if [ -f "$USERRESOURCES" ]; then
    xrdb -merge "$USERRESOURCES"
else
	cp $SYSRESOURCES $USERRESOURCES && xrdb -merge "$USERRESOURCES"
fi
#!/bin/bash
convert () {
    for file in $1/*
    do
	basefile=$(basename -- "$file")
	if [[ -d $1/$basefile ]]; then
	    echo $2Accessing $1/$basefile
	    convert $1/$basefile "$2...."
	elif [ ${basefile##*.} == "ui" ]; then
	    echo $2Converting $basefile
	    pyside6-uic $1/$basefile > $1/ui_${basefile%.*}.py
	elif [ ${basefile##*.} == "qrc" ]; then
	    echo $2Converting $basefile
	    pyside6-rcc $1/$basefile -o $1/rc_${basefile%.*}.py
	fi
    done
}
source ../testenv/Scripts/activate
convert "." ""
sleep 2
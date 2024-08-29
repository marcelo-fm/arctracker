#!/bin/bash

cp PKGBUILD PKGBUILD.bkp &&
	cat PKGBUILD |
	sed 's/x86_64/amd64/g' |
		sed 's/makedepends=("go>=1.23.0" "git")//g' >PKGBUILD &&
	makedeb &&
	cp PKGBUILD.bkp PKGBUILD -f

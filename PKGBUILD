# Maintainer: MARCELO MESQUITA <marcelofosmesquita@gmail.com>
pkgname="arctracker"
pkgver="1.1.0"
pkgrel=1
pkgdesc="ArcPy License Tracker"
url="https://github.com/marcelo-fm/arctracker"
arch=("x86_64")
optdepends=("ripgrep>=13.0: better search" "jq>=1.6: better search")
makedepends=("go>=1.23.0" "git")
license=("Apache-2.0")
sha512sums=("SKIP")
source=("$pkgname-$pkgver.tar.gz::https://github.com/marcelo-fm/arctracker/archive/refs/tags/v$pkgver.tar.gz")

build() {
	cd "$pkgname-$pkgver" && go build -o arctracker main.go -tags prod
}

package() {
	cd "$pkgname-$pkgver" && install -Dm755 arctracker "$pkgdir/usr/bin/arctracker"
}

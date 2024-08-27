# Maintainer: MARCELO MESQUITA <marcelofosmesquita@gmail.com>
pkgname="arctracker"
pkgver="1.0.0"
pkgrel=1
pkgdesc="ArcPy License Tracker"
url="https://github.com/marcelo-fm/arctracker"
arch=("x86_64")
depends=("ripgrep>=14.1.0" "jq>=1.7.1")
makedepends=("go>=1.23.0" "git")
license=("Apache-2.0")
sha512sums=("SKIP")
source=("$pgkname-$pkgver.tar.gz::https://github.com/marcelo-fm/arctracker/archive/refs/tags/$pkgver.tar.gz")

build() {
	cd "$pkgname-$pkgver" && go build -o arctracker main.go
}

package() {
	cd "$pkgname-$pkgver" && install -Dm755 arctracker "$pkgdir/usr/bin/arctracker"
}

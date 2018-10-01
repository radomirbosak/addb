# addb #

Anime and drama database. Track your watched episodes locally and comfortably through CLI.


## Usage ##

Show version
```console
$ addb --version
addb 0.0.1
```

Export anime/drama list
```console
$ addb export
{
	"anime": [
		{
			"name": "yamada",
			"full_name": "Yamada-kun and the Seven Witches",
			"status": "watching",
			"progress": 11,
			"watch_url": "https://www9.9anime.is/watch/yamada-kun-and-the-seven-witches.kw99"
		}
	]
}
```

## Installation ##

```console
$ git clone https://github.com/radomirbosak/addb.git
$ cd addb
$ pip3 install .
```

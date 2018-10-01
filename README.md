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

List anime/drama
```console
$ addb
nr.  Name                              Status     Progress
===  ================================  =========  ========
1.   Yamada-kun and the Seven Witches  watching   11
2.   Keijo!!!!!!!!                     watching   4
```

Add new anime/drama
```console
$ addb add yamada \
    --full-name "Yamada-kun and the Seven Witches" \
    --status watching \
    --alias yamadakun --alias yamada-kun \
    --watch-url "https://www1.9anime.to/watch/yamada-kun-and-the-seven-witches.kw99"
```

Open anime/drama in browser
```console
$ addb watch yamada
```

Remove anime/drama from database
```console
$ addb remove yamada-kun
```

Update anime/drama progress
```console
$ addb update yamada
Anime/drama "Yamada-kun and the Seven Witches" is now at episode 12

$ addb update yamada
Anime/drama "Yamada-kun and the Seven Witches" is now at episode 13

$ addb update yamada 4
Anime/drama "Yamada-kun and the Seven Witches" is now at episode 4
```

Edit anime/drama info
```console
$ addb edit yamada --status watched --full-name "Yamada-kun to 7-nin no Majo"
```

## Installation ##

```console
$ git clone https://github.com/radomirbosak/addb.git
$ cd addb
$ pip3 install .
```

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
            "watch_url": "https://..."
        }
    ]
}
```

List anime/drama
```console
$ addb  # or
$ addb list  # or
$ addb list watching
nr.  Name                              Status     Progress
===  ================================  =========  ========
1.   Yamada-kun and the Seven Witches  watching   11
2.   Keijo!!!!!!!!                     watching   4

$ addb list all
nr.  Name                              Status     Progress
===  ================================  =========  ========
1.   Yamada-kun and the Seven Witches  watching   11
2.   Keijo!!!!!!!!                     watching   4
3.   Hataraku Saibou                   watched    13
4.   Kemurikusa                        unwatched  0
```

Use a different database/cache file
```console
$ addb --cache /tmp/dorama
nr.  Name                              Status    Progress
===  ================================  ========  ========
1.   GeGeGe no Nyōbō                   Watching  13
```

Add new anime/drama
```console
$ addb add yamada \
    --full-name "Yamada-kun and the Seven Witches" \
    --status watching \
    --alias yamadakun --alias yamada-kun \
    --watch-url "https://..."
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
$ pip3 install --user .
```

Install bash completion (sudo needed for accessing `/etc/bash_completion.d/`)

```console
$ sudo make completions-install-bash
```

Install fish completion

```console
$ make completions-install-fish
```

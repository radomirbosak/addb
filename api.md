# Proposed addb CLI API

List currently watching anime/drama
```console
$ addb  # or
$ addb list watching

nr.  Name                              Status    Progress
===  ================================  ========  ========
1.   Yamada-kun and the Seven Witches  Watching  11
2.   Keijo!!!!!!!!                     Watching  4
```

Update progress
```console
$ addb update yamada 12  # or
$ addb update yamada +1
nr.  Name                              Status   Progress
===  ================================  =======  ========
1.   Yamada-kun and the Seven Witches  Watched  12
```

Add anime/drama
```console
$ addb add yamada --alias yamadakun --full-name "Yamada-kun and the Seven Witches"
```

Edit anime/drama properties
```console
$ addb edit yamada --watch-url "https://..."
```

Remove anime/drama
```console
$ add remove yamada
```

Open a anime/drama streaming website with specific anime/drama in a web browser
```console
$ addb watch yamada
```

Use a different cache file
```console
$ addb --cache /tmp/dorama
nr.  Name                              Status    Progress
===  ================================  ========  ========
1.   GeGeGe no Nyōbō                   Watching  13
```

Export the database in json format
```console
$ addb export
[
	{
		"name": "yamada",
		"full_name": "Yamada-kun and the Seven Witches",
		"status": "watching",
		"progress": 11,
		"watch_url": "https://..."
	}
]
```
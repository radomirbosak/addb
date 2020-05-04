#
# Completions for the addb command
#

function __fish_addb_no_command_yet
	set -l cmdln (commandline -poc)
	for i in (commandline -poc)
		if contains -- $i export list add watch remove update edit
			return 1
		end
	end
	return 0
end

function __fish_addb_alias_ok
	set -l cmdln (commandline -poc)
	if contains -- $cmdln[-1] watch remove update edit
		return 0
	end
	return 1
end

function __fish_addb_after_status
	set -l cmdln (commandline -poc)
	if contains -- $cmdln[-1] "--status"
		return 0
	end
	return 1
end

complete -c addb -f

complete -c addb -s h -l help --description "Display help and exit" -f
complete -c addb -n '__fish_addb_no_command_yet' -s V -l version --description "Display program version" -f
complete -c addb -n '__fish_addb_no_command_yet' -s C -l cache --description "Specify cache file" -r

complete -c addb -n '__fish_use_subcommand' -a export --description "Export anime/drama database"
complete -c addb -n '__fish_use_subcommand' -a list --description "List anime/dramas in database" -f
complete -c addb -n '__fish_use_subcommand' -xa add --description "Add anime/drama to database"
complete -c addb -n '__fish_use_subcommand' -xa watch --description "Open the anime/drama watch-url in a web browser"
complete -c addb -n '__fish_use_subcommand' -xa remove --description "Remove anime/drama from DB"
complete -c addb -n '__fish_use_subcommand' -xa update --description "Set the number of watched episodes"
complete -c addb -n '__fish_use_subcommand' -xa edit --description "Edit anime/drama properties"

complete -c addb -n '__fish_addb_alias_ok' -a "(command addb list all --raw-alias-list-desc)"

complete -c addb -n 'contains list (commandline -poc)' -a "unwatched watching watched dropped all"
complete -c addb -n 'contains list (commandline -poc)' -l raw-alias-list --description 'Helper function for bash completion'
complete -c addb -n 'contains list (commandline -poc)' -l raw-alias-list-desc --description 'Helper function for fish completion'

complete -c addb -n 'contains add (commandline -poc)' -l full-name --description 'Full anime/drama name'
complete -c addb -n 'contains add (commandline -poc)' -l alias --description 'Alternative name'
complete -c addb -n 'contains add (commandline -poc)' -l status --description 'Anime/drama status'
complete -c addb -n 'contains add (commandline -poc)' -l watch-url --description 'Url with anime/drama stream'
complete -c addb -n 'contains add (commandline -poc)' -l update-episode-urls --description 'Download episode urls'

complete -c addb -n 'contains edit (commandline -poc)' -l full-name --description 'Full anime/drama name'
complete -c addb -n 'contains edit (commandline -poc)' -l alias --description 'Alternative name'
complete -c addb -n 'contains edit (commandline -poc)' -l status --description 'Anime/drama status'
complete -c addb -n 'contains edit (commandline -poc)' -l watch-url --description 'Url with anime/drama stream'
complete -c addb -n 'contains edit (commandline -poc)' -l update-episode-urls --description 'Download episode urls'

complete -c addb -n '__fish_addb_after_status' -a "unwatched watching watched dropped"

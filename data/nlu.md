## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Jarvis
- jarvis
- greetings
- hey jarvis

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- thank you
- that's it

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- great
- yeah

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- C

## intent:create
- create a page on project
- generate a new project
- add
- new
- schedule a deadline

## intent:search
- find the solution
- help me out with
- open the platform
- read for me
- what is the deadline
- when is the meeting
- get me the code
- check for the solution
- search
- bring me the progress
- update
- get
- hey Jarvis, find me the latest commit
- hey jarvis, get [me](search_keys) the update
- fetch [me](search_keys) the solution
- I want
- hey jarvis, help [me](search_keys) with the solution

## intent:searchBitbucket
- hey Jarvis, [find me](search_keys) the latest [commit](bitbucket_action)
- [find me](search_keys) the last update from user on [repo](bitbucket_key)
- [find](search_keys) the list of [watchers](bitbucket_action)
- Jarvis, [find](search_keys) the list of users who have done [commit](bitbucket_action) [since last weekend]{"entity": "duration_keys", "value": "last weekend"}.
- [get me](search_keys) the [code](bitbucket_action).
- bitbucket
- hey jarvis, get [me](search_keys) the list of [watchers](bitbucket_action) on [repo]{"entity": "bitbucket_key", "value": " bitbucket_key"} test under [project test]{"entity": "project_name", "value": "test"}
- hey, [get me](search_keys) the [code](bitbucket_action) on [test](repo_name)
- hey, [get me](search_keys) the [code](bitbucket_action) on [test](repo_name) under [atlassian](project_name).
- hey, [get me](search_keys) the [code](bitbucket_action) on [repository test]{"entity": "repo_name", "value": "test"} [atlassian project]{"entity": "project_name", "value": "atlassian"}.
- Jarvis, [get me](search_keys) the [code](bitbucket_action) on [repository test]{"entity": "repo_name", "value": "test"} under [project atlassian](project_name).
- Jarvis, [get me](search_keys) the latest [commit](bitbucket_action) on branch [master](branch_name).
- [get me](search_keys) the [code](bitbucket_action) from [master](branch_name) branch of [repository](bitbucket_key) [atlassian](repo_name)
- [get me](search_keys) the [code](bitbucket_action) from [master](branch_name) branch of [atlassian repository]{"entity": "repo_name", "value": "atlassian"}
- [get me]{"entity": "search_keys", "value": " search_keys"} the last [commit code](bitbucket_action) on [repo atlassian]{"entity": "repo_name", "value": "atlassian"}
- Good morning Jarvis, please [get me]{"entity": "search_keys", "value": " search_keys"} the list of [watchers](bitbucket_action) on [test3 repository]{"entity": "repo_name", "value": "test3"}
- who did the last [commit](bitbucket_action) on [sih repo]{"entity": "repo_name", "value": "sih"} under [project atlassianwork](project_name)?
- Jarvis, when was the last [commit](bitbucket_action) made on [repo art-2020]{"entity": "repo_name", "value": "art-2020"}
- Jarvis, on [repo art-2020]{"entity": "repo_name", "value": "art-2020"}, when was the last [commit]{"entity": "bitbucket_action", "value": " commit"} made
- [I want](search_keys) to know [who all](search_keys) are [watchers](bitbucket_action) on the [repository atlassianWork]{"entity": "repo_name", "value": "atlassianWork"} under [project art-2020](project_name)
- hey jarvis, [get me]{"entity": "search_keys", "value": " search_keys"} the list of [watchers](bitbucket_action)
- hey jarvis, on [repository robocon]{"entity": "repo_name", "value": "robocon"} who made the last [commit](bitbucket_action)
- [find]{"entity": "search_keys", "value": " search_keys"} the latest update on [repo arcWork]{"entity": "repo_name", "value": "arcWork"}
- [find]{"entity": "search_keys", "value": " search_keys"} the list of [watchers]{"entity": "bitbucket_action", "value": "list of watchers"}
- jarvis, [get me]{"entity": "search_keys", "value": " search_keys"} the last [commit]{"entity": "bitbucket_action", "value": "code"} on [repo sihWork](repo_name)
- hey jarvis, [who](search_keys) did the [last](duration_keys) [commit](bitbucket_action) on [repo trialApp](repo_name)
- jarvis, [get me]{"entity": "search_keys", "value": " search_keys"} the list of [developers]{"entity": "bitbucket_action", "value": "list of watchers"} on [repository]{"entity": "bitbucket_key", "value": "bitbucket_key"}
- [who](search_keys) made the last [commmit](bitbucket_action)

## intent:searchErrors
- hey Jarvis, [find me](search_keys) the [solution to the error](error_keys)
- [Help me](search_keys) out with the [error](error_keys)
- [what is](search_keys) the best answer to the [problem of value error](error_keys)?
- Stackoverflow
- hey, [solve](error_keys) the error for me.
- stackoverflow
- [find me]{"entity": "search_keys", "value": " search_keys"} the optimal [solution to](error_keys) the [error]{"entity": "error_keys", "value": " error"}
- [find]{"entity": "search_keys", "value": " search_keys"} the [solution to](error_keys) [the class not found error](error_action)
- Fetch [me](search_keys) the best [solution to](error_keys) the [invalid input for json error](error_action)
- yes, [i want](search_keys) [solution](error_keys)
- hey, [get me]{"entity": "search_keys", "value": " search_keys"} the [best answer](error_keys) to the [error](error_keys)

## intent:error_action_entry
- [the class not found error](error_action)
- the error is [value not found]{"entity": "error_action", "value": "value not found error"}
- It reads [invalid token error](error_action)
- [floating point error](error_action)
- [no module name flask found](error_action)

## intent:repo_name_entry
- [test](repo_name)
- the repository on target is [webApp](repo_name)
- repo name is [mobileApp](repo_name)
- [webApp](repo_name)

## intent:user_name_entry
- user name is [jamal](user_name)
- [rohit](user_name) is the user name i am looking for
- [Jamal](user_name)
- user is [tanmay](user_name)

## intent:branch_name_entry
- [master](branch_name) is the branch name
- the branch is [version](branch_name)
- [stable](branch_name)
- [master](branch_name)
- [version 2.x](branch_name) branch

## intent:bitbucket_action_entry
- [commit]{"entity": "bitbucket_action", "value": "code"}
- i want the [code](bitbucket_action)
- [watchers](bitbucket_action)
- list of [watchers]{"entity": "bitbucket_action", "value": "list of watchers"}

## intent:update
- add the filter to
- set the deadline to
- change the requirements
- reschedule the meeting
- set a new dependancy
- update
- remove the release note
- postpone
- reschedule the deadline

## synonym: bitbucket_action
- commit
- watchers
- developers
- code
- source code
- list of watchers
- list of users
- list of developers
- users

## synonym: bitbucket_key
- repo
- repository
- bitbucket
- branch
- project

## synonym: duration_keys
- since last weekend
- since
- since yesterday
- over the past month
- overnight
- in fortnight
- the latest

## synonym: error_keys
- error
- solution to the error
- problem
- issue
- answer
- solution

## synonym: search_keys
- get me
- find
- find me
- search
- fetch
- bring
- can you get me
- please update me
- get
- check
- Help me
- what is
- when is
- i want
- who
- who all
- i need

## synonym:"duration_keys","value":"last"
- last

## synonym:arcWork
- repo arcWork

## synonym:art-2020
- repo art-2020

## synonym:atlassian
- atlassian project
- atlassian repository
- repo atlassian

## synonym:atlassianWork
- repository atlassianWork

## synonym:robocon
- repository robocon

## synonym:sih
- sih repo

## synonym:test
- project test
- repository test

## synonym:test3
- test3 repository

## synonym:value not found error
- value not found

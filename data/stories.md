<!-- ## happy path
* greet
  - utter_greet -->
<!-- * mood_great
  - utter_happy -->

<!-- ## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye -->

## say goodbye
* goodbye
  - utter_goodbye

<!-- ## bot challenge
* bot_challenge
  - utter_iamabot -->

## greet path
* greet
  - utter_greet

<!-- ## search path 2
* search 
  - utter_search
  - action_confirm_domain -->

## create path 2
* create 
  - utter_create
  <!-- - action_confirm_domain -->

## update path 2
* update
  - utter_update
  <!-- - action_confirm_domain -->
<!-- 
## search path 1
* greet
  - utter_greet
* search 
  - utter_search
  - action_confirm_domain -->

## update path 1
* greet
  - utter_greet
* update 
  - utter_update
  <!-- - action_confirm_domain -->

## create path 1
* greet
  - utter_greet
* create 
  - utter_create
  <!-- - action_confirm_domain -->
<!-- ## interactive_story_1
* greet
    - utter_greet
* search
    - utter_search -->

## search_bitbucket path 1
* greet
  - utter_greet
* search
  - utter_search
* affirm
  - utter_get_exact_domain
* searchBitbucket
  - bitbucket_form  
  - form{"name":"bitbucket_form"}
  - form{"name": null}
  - utter_slots_values

## search_bitbucket path 2
* greet
  - utter_greet
* searchBitbucket
  - bitbucket_form
  - form{"name":"bitbucket_form"}
  - form{"name": null}
  - utter_slots_values

## search_bitbucket path 3
* searchBitbucket
  - bitbucket_form
  - form{"name":"bitbucket_form"}
  - form{"name": null}
  - utter_slots_values
## search_bitbucket path 4
* greet
  - utter_greet
* search
  - utter_search
* deny
  - utter_rephrase_please

## search_bitbucket path 5
* bitbucket_action_entry
  - bitbucket_form
  - form{"name":"bitbucket_form"}
  - form{"name": null}
  - utter_slots_values

## search_errors path 1
* greet
  - utter_greet
* search
  - utter_search
* affirm
  - utter_get_exact_domain
* searchErrors
  - error_form
  - form{"name":"error_form"}
  - form{"name": null}
  - utter_error_query

## search_errors path 2
* greet
  - utter_greet
* searchErrors
  - error_form
  - form{"name":"error_form"}
  - form{"name": null}
  - utter_error_query

## search_errors path 3
* searchErrors
  - error_form
  - form{"name":"error_form"}
  - form{"name": null}
  - utter_error_query




## search_errors path 4
* greet
  - utter_greet
* search
  - utter_search
* deny
  - utter_rephrase_please

## search_errors path 5
* error_action_entry
  - error_form
  - form{"name":"error_form"}
  - form{"name": null}
  - utter_error_query


## interactive_story_1
* greet
    - utter_greet
* searchBitbucket{"search_keys": " search_keys", "bitbucket_action": "list of watchers"}
    - slot{"bitbucket_action": "list of watchers"}
    - bitbucket_form
    - utter_slots_values
* searchBitbucket{"search_keys": " search_keys", "bitbucket_action": "code", "repo_name": "repo sihWork"}
    - slot{"bitbucket_action": "code"}
    - slot{"repo_name": "repo sihWork"}
    - bitbucket_form
    - form{"name": "bitbucket_form"}
    - slot{"bitbucket_action": "code"}
    - slot{"repo_name": "repo sihWork"}
    - slot{"bitbucket_action": "code"}
    - slot{"repo_name": "repo sihWork"}
    - slot{"requested_slot": "user_name"}
* form: user_name_entry{"user_name": "Jamal"}
    - slot{"user_name": "Jamal"}
    - form: bitbucket_form
    - slot{"user_name": "Jamal"}
    - slot{"requested_slot": "branch_name"}
* form: branch_name_entry{"branch_name": "master"}
    - slot{"branch_name": "master"}
    - form: bitbucket_form
    - slot{"branch_name": "master"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## interactive_story_2
* search{"search_keys": "me"}
    - utter_search
* search
    - utter_search
* affirm
    - utter_get_exact_domain
* searchErrors
    - error_form
    - form{"name": "error_form"}
    - slot{"requested_slot": "error_action"}
* form: error_action_entry{"error_action": "floating point error"}
    - slot{"error_action": "floating point error"}
    - form: error_form
    - slot{"error_action": "floating point error"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_error_query
* searchErrors{"search_keys": "me", "error_keys": "solution to", "error_action": "invalid input for json error"}
    - slot{"error_action": "invalid input for json error"}
    - slot{"error_keys": "solution to"}
    - utter_error_search
    - error_form
    - form{"name": "error_form"}
    - slot{"error_action": "invalid input for json error"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_error_query
* searchBitbucket{"bitbucket_action": "commit", "repo_name": "repo trialApp"}
    - slot{"bitbucket_action": "commit"}
    - slot{"repo_name": "repo trialApp"}
    - bitbucket_form
    - form{"name": "bitbucket_form"}
    - slot{"bitbucket_action": "commit"}
    - slot{"repo_name": "repo trialApp"}
    - slot{"bitbucket_action": "commit"}
    - slot{"repo_name": "repo trialApp"}
    - slot{"requested_slot": "user_name"}
* form: user_name_entry{"user_name": "tanmay"}
    - slot{"user_name": "tanmay"}
    - form: bitbucket_form
    - slot{"user_name": "tanmay"}
    - slot{"requested_slot": "branch_name"}
* form: branch_name_entry{"branch_name": "version 2.x"}
    - slot{"branch_name": "version 2.x"}
    - form: bitbucket_form
    - slot{"branch_name": "version 2.x"}
    - slot{"requested_slot": "duration_key"}
* form: search

## interactive_story_3
* searchBitbucket{"search_keys": " search_keys", "bitbucket_action": "list of watchers", "bitbucket_key": "bitbucket_key"}
    - slot{"bitbucket_action": "list of watchers"}
    - slot{"bitbucket_key": ["bitbucket_key"]}
    - bitbucket_form
    - form{"name": "bitbucket_form"}
    - slot{"bitbucket_action": "list of watchers"}
    - slot{"bitbucket_action": "list of watchers"}
    - slot{"requested_slot": "repo_name"}
* form: repo_name_entry{"repo_name": "test"}
    - slot{"repo_name": "test"}
    - form: bitbucket_form
    - slot{"repo_name": "test"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## interactive_story_4
* searchErrors{"search_keys": " search_keys", "error_keys": "error"}
    - slot{"error_keys": "error"}
    - utter_error_search
    - error_form
    - form{"name": "error_form"}
    - slot{"requested_slot": "error_action"}
* form: error_action_entry{"error_action": "no module name flask found"}
    - slot{"error_action": "no module name flask found"}
    - form: error_form
    - slot{"error_action": "no module name flask found"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_error_query
* searchBitbucket{"search_keys": "who", "bitbucket_action": "commmit"}
    - slot{"bitbucket_action": "commmit"}
    - bitbucket_form
    - form{"name": "bitbucket_form"}
    - slot{"bitbucket_action": "commmit"}
    - slot{"duration_keys": "latest"}
    - slot{"bitbucket_action": "commmit"}
    - slot{"requested_slot": "repo_name"}
* form: repo_name_entry{"repo_name": "webApp"}
    - slot{"repo_name": "webApp"}
    - form: bitbucket_form
    - slot{"repo_name": "webApp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

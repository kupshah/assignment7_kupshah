import gzip
import json


def active_users(filenames_of_monthly_archives):
    user_counts_vive = {}
    user_counts_oc = {}
    for file in filenames_of_monthly_archives:
        print(file)
        users_who_commented_mo_oc = set()
        users_who_commented_mo_vive = set()
        for line in gzip.open(file):
            comment = json.loads(line)
            user = comment['author']
            subreddit = comment['subreddit']
            if subreddit == "oculus":
                users_who_commented_mo_oc.add(user)
            elif subreddit == "Vive":
                users_who_commented_mo_vive.add(user)
            else:
                pass
        user_counts_oc[file] = users_who_commented_mo_oc
        user_counts_vive[file] = users_who_commented_mo_vive
    active_users_obj = {"vive": user_counts_vive, "oculus": user_counts_oc}
    with open('active_users.json', 'w') as f:
        json.dump(str(active_users_obj), f)
    return active_users_obj


def active_users_count(users_dict):
    for subreddit in users_dict.keys():
        for month in users_dict[subreddit]:
            users_dict[subreddit][month] = len(users_dict[subreddit][month])
    with open('active_users_counts.json', 'w') as f:
        json.dump(str(users_dict), f)
    return users_dict


datafiles = ["RC_2018-01.gz", "RC_2018-02.gz", "RC_2018-03.gz", "RC_2018-04.gz", "RC_2018-05.gz", "RC_2018-06.gz",
             "RC_2018-07.gz", "RC_2018-08.gz", "RC_2018-09.gz", "RC_2018-10.gz", "RC_2018-11.gz", "RC_2018-12.gz",
             "RC_2019-01.gz", "RC_2019-03.gz", "RC_2019-03.gz", "RC_2019-04.gz", "RC_2019-05.gz", "RC_2019-06.gz"]
test_data_path = "/l/research/social-media-mining/reddit-sample-1-percent/comments/"
filenames = [test_data_path + filename for filename in datafiles]
print(active_users_count(active_users(filenames)))

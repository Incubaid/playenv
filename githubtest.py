from JumpScale import j

#now we can use the model as follows

# j.db.models.github.repository...

from github import Github

g=Github("062ef45c7a4c2ba877ad8f06378722c5681d7f70")




for repo in g.get_user().get_repos():
    print (repo.name)
    # repo.edit(has_wiki=False)
    from IPython import embed
    print ("DEBUG NOW id")
    embed()
    p
    

# from github3 import login
# gh = login(token="062ef45c7a4c2ba877ad8f06378722c5681d7f70")

# for repo in gh.iter_user_repos(login=login):
#     from IPython import embed
#     print ("DEBUG NOW id")
#     embed()
#     p


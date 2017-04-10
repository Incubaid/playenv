

#click based


#read github.yaml to get info from github
## this github.yaml has
'''
list of url's (account/reponame) to work upon
list of labels which should exist in repo's (others should be deleted), has also color info
list of milestones which should exist
teams & members: describes membership
list of tea
'''

#cmd: secret_set
## ask secret store in redis, use this secret for further api connections
## if not specified for any of the other commands ask secret first

# cmd: issues_get
# args: labels=urgent, ...  only get issues which have one of the specified labels in
# args: milestones=may20,...  only get issues which have one of the specified labels in
## fetch all issues and dump them as yaml (include labels, milestones, assignees, ...)

# cmd: labels_set
## based on labels as mentioned in github.yaml make sure they all exist in each repo which is mentioned in the config file
## remove the ones which are not in the github.yaml file

# cmd: milestones_set
## based on labels as mentioned in github.yaml make sure they all exist in each repo which is mentioned in the config file
## DO NOT remove the ones which already existed on repo's (so it only adds the new ones)

# cmd: membership_set
## based on membership as defined in config file
## make sure the group/members exist in account
## make sure all repos as mentioned in file above are accesible by members

#!/usr/bin/env python

import click
import yaml
import github
import redis

class App:

    def __init__(self, config_file='github.yaml', reset_secret=False):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        if not bool(self.r.get('secret')) or reset_secret:
            self.secret_set()
        else:
            secret = self.r.get('secret').decode()
            self.gh = github.Github(secret)
        with open(config_file) as f:
            self.d = normalize_dict(yaml.load(f.read()))

    def secret_set(self):
        self.r.set('secret', input("please enter the secret: "))
        secret = self.r.get('secret').decode()
        self.gh = github.Github(secret)

    def get_attr_repo(self, attr, org, repo):
        k = {
            "collaborators": "login",
            "milestones": "title",
            "labels": "name"
        }[attr]
        return {i[k]:i for i in self._get_attr_repo(attr, org, repo)}

    def _get_attr_repo(self, attr, org, repo):
        return self.d[org.login][repo.name].get(attr)

    def get_organizations(self):
        return (self.gh.get_organization(o) for o in self.d)

    def get_repos(self, org):
        return (org.get_repo(r) for r in self.d[org.login])

def extend_dict(b, a):
    for i in a:
        if i in b:
            if type(b[i]) is list and type(a[i]) is list:
                b[i].extend(a[i])
        else:
            b[i] = a[i]

def normalize_dict(d):

    if type(d) is not dict:
        return d
    has_children = False
    sps = {sp:d[sp] for sp in ["labels", "milestones", "collaborators"] if sp in d}
    for k in d:
        if k not in sps and type(d[k]) is dict:
            has_children = True
            extend_dict(d[k], sps)
            normalize_dict(d[k])
    if has_children:
        for sp in sps:
            del d[sp]
    return d

def to_dict(d):
    if isinstance(d,(int,str,float)):
        return d
    elif isinstance(d, list):
        return list(map(to_dict, d))
    elif isinstance(d, dict):
        return {to_dict(k):to_dict(v) for k,v in d.items()}
    elif hasattr(d,'__dict__'):
        return to_dict(d.__dict__)
    else:
        return d.__str__()



@click.group()
@click.pass_obj
@click.option('--file', '-f', default='github.yaml')
def cli(ctx, file):
    ctx['app'] = App(config_file=file)

@click.command()
@click.pass_obj
def secret_set(ctx):
    app = ctx['app']
    app.secret_set()

@click.command()
@click.pass_obj
@click.option('--label', '-l', multiple=True)
@click.option('--milestone', '-m')
def issues_get(ctx, label, milestone=None):
    import json
    res = []
    url_parameters = {}
    if label:
        url_parameters["labels"] = ",".join(l for l in label)
    app = ctx['app']
    for org in app.get_organizations():
        for repo in app.get_repos(org):
            if milestone:
                url_parameters["milestone"] = (x._identity for x in repo.get_milestones() if x.title==milestone).__next__()
            res.extend(github.PaginatedList.PaginatedList(
                github.Issue.Issue,
                repo._requester,
                repo.url + "/issues",
                url_parameters
            ))
    print(json.dumps(to_dict(res)))

@click.command()
@click.pass_obj
def labels_set(ctx):
    app = ctx['app']
    for org in app.get_organizations():
        for repo in app.get_repos(org):
            curr_labels = set(label.name for label in repo.get_labels())
            attrs = app.get_attr_repo("labels", org, repo)
            labels = list(set(attrs.keys()) - curr_labels)
            for label in labels:
                repo.create_label(**attrs[label])

@click.command()
@click.pass_obj
def milestones_set(ctx):
    app = ctx['app']
    for org in app.get_organizations():
        for repo in app.get_repos(org):
            curr_milestones = set(milestone.title for milestone in repo.get_milestones())
            attrs = app.get_attr_repo("milestones", org, repo)
            milestones = list(set(attrs.keys()) - curr_milestones)
            for milestone in milestones:
                repo.create_milestone(**attrs[milestone])

@click.command()
@click.pass_obj
def collaborators_set(ctx):
    app = ctx['app']
    for org in app.get_organizations():
        for repo in app.get_repos(org):
            curr_collaborators = set(collaborator.login for collaborator in repo.get_collaborators())
            attrs = app.get_attr_repo("collaborators", org, repo)
            collaborators = list(set(attrs.keys()) - curr_collaborators)
            for collaborator in collaborators:
                repo.add_to_collaborators(attrs[collaborator]['login'])

cli.add_command(secret_set)
cli.add_command(issues_get)
cli.add_command(labels_set)
cli.add_command(milestones_set)
cli.add_command(collaborators_set)

if __name__ == "__main__":
    cli(obj={})
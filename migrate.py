from getopt import getopt
import giteapy
from github import Github
# import json
import sys

# with open('./auth.json', 'r') as f:
#     creds = json.loads(f.read())
#     gh_token = creds['github']['token']
#     gh_org = creds['github']['organization']
#     ga_token = creds['gitea']['token']
# f.close()
gh_token = sys.argv[1]
ga_token = sys.argv[2]
gh_org = sys.argv[3]
ga_url = sys.argv[4]
ga_org = sys.argv[5]

print('Querying github and gitea')
gh = Github(gh_token)
ga_conf = giteapy.Configuration()
ga_conf.api_key['access_token'] = ga_token
ga_conf.host = f"{ga_url}/api/v1"
ga_repoapi = giteapy.RepositoryApi(giteapy.ApiClient(ga_conf))
ga_orgapi = giteapy.OrganizationApi(giteapy.ApiClient(ga_conf))

gh_repos = {}
for repo in gh.get_organization(gh_org).get_repos():
    gh_repos[repo.name] = repo.clone_url

ga_rx = ga_orgapi.org_list_repos(ga_org)
ga_repos = {}
for repo in ga_rx:
    ga_repos[repo.name] = repo.clone_url

unsync = list(set(gh_repos) ^ set(ga_repos))

print(f"Going to mirror\n{unsync}")
migrate = {}
for u in unsync:
    migrate = {
        'auth_token': gh_token,
        'clone_addr': f"https://github.com/{gh_org}/{u}.git",
        'repo_name': u,
        'repo_owner': ga_org,
        'private': True,
        'mirror': True,
        'issues': True,
        'labels': True,
        'milestones': True,
        'pull_requests': True,
        'releases': True,
        'wiki': True
    }
    print(f"Mirroring {u}")
    ga_repoapi.repo_migrate(body=migrate)
print("Mirroring done")

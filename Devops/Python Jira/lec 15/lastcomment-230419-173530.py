from jira import JIRA
user="automation52786@gmail.com"
apikey='f2Nxb496FAgCCQRJM9OC2510'
server = "https://alnafi.atlassian.net"
jira = JIRA(server,basic_auth=(user,apikey))
ticket='AC-2'
issue= jira.issue(ticket)
comments = issue.fields.comment.comments
for comment in comments:
    eng= comment.author.displayName
    if eng == "Kazim Shaikh":
        print(comment.body)
        print(comment.created)



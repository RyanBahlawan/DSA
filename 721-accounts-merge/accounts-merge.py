class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1]*n
        
        #Gets the root
        def find(node):
            root = parent[node]
            if root!=node:
                root = find(parent[node])
                parent[node]=root
            return root
            

        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1==root2:
                return
            if rank[root1]>rank[root2]:
                parent[root2] = root1
                rank[root1]+=rank[root2]
            else:
                parent[root1] = root2
                rank[root2]+=rank[root1]
            return
        
        emailToAccountIdx = defaultdict(int) #email -> accountIdx

        #This populates the email to account index map
        #Any emails that are the same are unioned into the same group
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccountIdx:
                    union(emailToAccountIdx[email], i)
                else:
                    emailToAccountIdx[email] = i

        #Group the emails that are in the same root group
        groupRootEmail = defaultdict(list) #name -> email list

        #group all of the emails based by the acount name
        for email, node in emailToAccountIdx.items():
            root = find(node)
            groupRootEmail[root].append(email)

        res = []
        #Sort the emails then append them to the result
        for key in groupRootEmail.keys():
            name = accounts[key][0]
            emailSorted = sorted(groupRootEmail[key])
            res.append([name]+emailSorted)
        
        return res
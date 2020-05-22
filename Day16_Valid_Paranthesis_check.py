op=0
        cl=0
        st=0
        for i in range(len(s)):
            if (s[i]=='('):
                op+=1
            if(s[i]==')'):
                cl+=1
            if s[i]=='*':
                st+=1
            if (op+st)<cl:
                return False
            else:
                continue
        #print(op,cl)
        op=0
        cl=0
        st=0
        s=s[::-1]
        for i in range(len(s)):
            if (s[i]==')'):
                op+=1
            if(s[i]=='('):
                cl+=1
            if s[i]=='*':
                st+=1
            if (op+st)<cl:
                return False
            else:
                continue
        #print(op,cl)
        return True
        
        
        

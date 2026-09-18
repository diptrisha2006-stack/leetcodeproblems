char* removeOuterParentheses(char* s) {
    char stack[10001];
    int top=-1;
    int i,n;
    int idx=0;
    n=strlen(s);
    char *res=(char *)malloc(n+1);
    for(i=0;i<n;i++)
    {
        if(s[i]=='(')
        {
            if(top>=0)
            {
                res[idx++]='(';
            }
            top++;
            stack[top]='(';
        }
        else
        {
            stack[top--];
            if(top>=0)
            {
                res[idx++]=')';
            }
        }
    }
    res[idx]='\0';
    return res;
}
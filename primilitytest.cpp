// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution{
    public:
        bool isPrime(int N)
    {
        //Your code here
        if(N==1)return false;// since 1 is not a prime
        if(N<=0)return false;
        if(N==2 || N==3)return true;
        if(N%2==0 || N%3 == 0)return false;
        for(int i =5; i*i<= N;i+=6)// these jumps makes the code 3 times more faster than the O(root(N)) algo for primilitytest
        {
            if(N%i == 0 || N%(i+2)==0)
                return false;
        }
        return true;
    }

};

// { Driver Code Starts.

int main()
{
    int T; //testcases
    cin>>T; //input testcases
    while(T--) //while testcase have not been exhausted
    {
        int N;
        cin>>N; //input n
        Solution ob;
        if(ob.isPrime(N)) 
            cout<<"Yes";
        else
            cout<<"No";
            
        cout << endl;
    }
    return 0;
}

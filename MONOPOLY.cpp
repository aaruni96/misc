/*
Code to encrypt the convergence problem

V1.0

Author : Aaruni Kauhsik | http://edufor.me/blog

Bitch, please!

*/
#include<iostream>
#include<math.h>
#include<string.h>

using namespace std;

int conv(char *);

int main()
{
	char inp[256];
	cin>>inp;
	conv(inp);
	cout<<inp<<endl;
	return 0;
}

int conv(char *inp)
{
	int limbo,orig;		//limbo is my temp variable, orig stores the original value
	for(int i=0;i<int(strlen(inp));i++)
	{
		orig=limbo=inp[i]-'A'+1;
		limbo=(limbo*limbo)%('Z'-'A'+1);
		inp[i]=(orig+limbo)%26;
		inp[i]+='A'-1;
		if(inp[i]<65)	//to facilitate the cyclic order of alphabets
		{
			inp[i]='A'+'Z'-inp[i]-1;
		}
	}
	cout<<endl;
	return 0;
}

#include <stdio.h>
#include <math.h>

int Z(int n) 
{
	int i = 0;
	int zeros = 0;
	while (pow(5,i) <= n) 
	{
		zeros += n/pow(5,i);
		i++;
	}
	return zeros;
}

int main() 
{
	int T;
	int N;
	scanf("%d",T);
	while (T>0) 
	{
		scanf("%d",N);
		printf("%d\n",Z(N));
		T--;
	}
	
	return 0;
}
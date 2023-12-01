#include <stdio.h>
#include <stdlib.h> 
#include <string.h>


int main()
{
	//FILE *fptr; 	

	FILE *stream;
        char *line = NULL;
        size_t len = 0;
        ssize_t nread;

	int result; 

	stream = fopen("input.txt","r"); 
	//fptr = fopen("result.txt", "w"); 

	if(NULL == stream) 
	{
		printf("ERROR in main, missing file: input.txt"); 
		return -1; 
	}
 
	int res1; 
	int res2;
	int cnt; 
	int num[10] = {0};  

	while((nread = getline(&line, &len, stream)) != -1)
	{
		cnt = 0;

		for(int a = 0; a < 10; ++a)
		{
			num[a] = 0; 
		}

		printf("%s", line);
		for(int i = 0; i < len; ++i)
		{
			char c = line[i]; 
			int b = c - '0'; 

			if(b >= 0 && b <= 9)
			{
				//printf("%d",b);
				num[cnt] = b; 
				++cnt; 
			}
		}
		
		if(cnt > 1)
		{
			result += 10 * num[0] + num[cnt-1];
			printf("%d%d\n", num[0], num[cnt-1]); 
		}
		else if(cnt)
		{
			result += num[0]*10 + num[0]; 
			printf("%d%d\n",num[0],num[0]); 
		}

		line = NULL; 
		len = 0; 
	}

	printf("%d\n", result); 

	fclose(stream); 
}


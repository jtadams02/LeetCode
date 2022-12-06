#include <stdio.h>         
#include <stdlib.h>  
#include <string.h>


int main(int argc, char* argv[])
{
    FILE *inFile = NULL;
    char *fileName = argv[1];
    inFile=fopen(fileName,"r");
    int outCount = 1;
    while(1)
    {
        if(feof(inFile)){break;}
        char c[100];
        int count=0;
        if(fscanf(inFile,"%s",&c)==1)
        {
            for(int i=0;i<strlen(c);i++)
            {
                count = count +c[i];
            }
            printf("%d: \"%s\" has weight: %d\n", outCount,c,count);
            outCount++;
        }
        
        //printf("%d: \"%s\" has weight: %d\n", outCount,c,count);
        //outCount++;
    }

    /*int count = argc;
    for(int i=1;i<count;i++)
    {
        char *c = argv[i];
        int ascii = 0;
        
        for(int k=0;k<strlen(c);k++)
        {
           // printf("%c\n",c[k]);
           ascii = ascii+c[k];
        }
        printf("\"%s\" has weight: %d\n",c,ascii);
    }*/
}
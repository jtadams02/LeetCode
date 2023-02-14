
#include <stdio.h>         
#include <stdlib.h>                                                         
#include <string.h>


int main(int argc, char* argv[])
{
    int count = argc;
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
    }
}
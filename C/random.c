#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int random_array[10][10][10];
int a, b, c;
int main(void)
{
    for (a = 0; a<10; a++){
        for(b = 0; b<10; b++){
            for (c = 0; c<10; c++){
                random_array[a][b][c] = srand(time = NULL);
            }
        }
    }

    for (a = 0; a<10; a++){
        for(b = 0; b<10; b++){
            for (c = 0; c<10; c++){
                printf("\nrandom_array[%d][%d][%d]: ", a,b,c);
                printf("%d",random_array[a][b][c]);

            }

            printf("PRESS ENTER TO CONTINUE. PRESS CTRL-C TO QUIT.");
            getchar();
        }
    }
    /* code */
}

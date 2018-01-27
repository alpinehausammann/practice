#define CAR_PAYMENT 430
#define RENT 975
#define GAS 200
#define DISCOVER 120
#define HOME_DEPOT 30
#include <stdio.h>


int expenses[] = { CAR_PAYMENT, RENT, GAS, DISCOVER, HOME_DEPOT};
int i;

int main(void){
    int total;
    for (i = 0; i<5; i++){
        total += expenses[i];
    }
    printf("total expenses:$%d",total);
}
